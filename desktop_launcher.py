"""
Desktop launcher for the A-Load Generator.

Starts Streamlit headlessly and opens the UI in a native window when possible.
Avoids the WinForms/pythonnet backend that breaks in frozen Windows builds.
"""

from __future__ import annotations

import atexit
import os
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path


APP_TITLE = "A-Load Generator"
DEFAULT_PORT = 8501
HOST = "127.0.0.1"


def app_root() -> Path:
    """Resolve project root for source runs and frozen builds."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def main_app_path() -> Path:
    path = app_root() / "frontend" / "main_app.py"
    if not path.is_file():
        raise FileNotFoundError(f"Streamlit app not found: {path}")
    return path


def find_free_port(start_port: int = DEFAULT_PORT) -> int:
    port = start_port
    while port < start_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((HOST, port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("Could not find a free local port for the desktop app.")


def wait_for_server(port: int, timeout_seconds: float = 60.0) -> None:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.0)
            try:
                sock.connect((HOST, port))
                return
            except OSError:
                time.sleep(0.25)
    raise TimeoutError(
        f"Timed out waiting for the A-Load UI on http://{HOST}:{port}"
    )


def run_streamlit_server(script_path: Path, port: int) -> None:
    """Entrypoint used by the frozen child process to serve Streamlit."""
    from streamlit.web import cli as stcli

    sys.argv = [
        "streamlit",
        "run",
        str(script_path),
        f"--server.port={port}",
        "--server.headless=true",
        "--server.address=127.0.0.1",
        "--browser.gatherUsageStats=false",
        "--global.developmentMode=false",
    ]
    raise SystemExit(stcli.main())


def build_streamlit_command(script_path: Path, port: int) -> list[str]:
    streamlit_flags = [
        f"--server.port={port}",
        "--server.headless=true",
        "--server.address=127.0.0.1",
        "--browser.gatherUsageStats=false",
        "--global.developmentMode=false",
    ]

    if getattr(sys, "frozen", False):
        # Re-launch this executable in Streamlit-server mode.
        return [sys.executable, "--streamlit-server", str(script_path), *streamlit_flags]

    return [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(script_path),
        *streamlit_flags,
    ]


def start_streamlit_process(script_path: Path, port: int) -> subprocess.Popen:
    env = os.environ.copy()
    env["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    env["BROWSER"] = "none"

    creationflags = 0
    if os.name == "nt":
        # Avoid popping an extra console window for the Streamlit child process.
        creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)

    return subprocess.Popen(
        build_streamlit_command(script_path, port),
        cwd=str(app_root()),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        creationflags=creationflags,
    )


def stop_process(proc: subprocess.Popen | None) -> None:
    if proc is None:
        return
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def show_error(message: str) -> None:
    """Show a visible error even in windowed/.exe builds."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(APP_TITLE, message)
        root.destroy()
    except Exception:
        print(message, file=sys.stderr)


def launch_browser_fallback(port: int) -> None:
    """
    Open the system browser and keep a small control window open.

    Used when native webview backends are unavailable on the machine.
    """
    import tkinter as tk

    url = f"http://{HOST}:{port}"
    webbrowser.open(url)

    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("420x160")
    root.resizable(False, False)

    label = tk.Label(
        root,
        text=(
            f"{APP_TITLE} is running.\n\n"
            f"Opened in your browser:\n{url}\n\n"
            "Close this window to quit the app."
        ),
        justify="left",
        padx=16,
        pady=16,
    )
    label.pack(fill="both", expand=True)

    button = tk.Button(root, text="Quit", width=12, command=root.destroy)
    button.pack(pady=(0, 16))

    root.mainloop()


def launch_desktop_window(port: int) -> None:
    """
    Open a native desktop window when possible.

    On Windows packaged builds, force Edge WebView2 and avoid the default
    WinForms/pythonnet backend that fails in frozen apps.
    """
    url = f"http://{HOST}:{port}"

    # Force Edge WebView2 before importing webview (avoids winforms/clr).
    if os.name == "nt":
        os.environ["PYWEBVIEW_GUI"] = "edgechromium"

    try:
        import webview

        webview.create_window(
            APP_TITLE,
            url=url,
            width=1200,
            height=900,
            min_size=(900, 700),
        )
        # Explicit gui= keeps packaged Windows builds off WinForms/pythonnet.
        webview.start(gui="edgechromium" if os.name == "nt" else None)
        return
    except Exception:
        # Coworker machines without a working WebView2 backend still get the app.
        launch_browser_fallback(port)


def main() -> int:
    # Frozen child process mode: act as the Streamlit server only.
    if "--streamlit-server" in sys.argv:
        idx = sys.argv.index("--streamlit-server")
        script = Path(sys.argv[idx + 1])
        # Remaining args are already streamlit flags; port is embedded in them.
        port = DEFAULT_PORT
        for arg in sys.argv[idx + 2 :]:
            if arg.startswith("--server.port="):
                port = int(arg.split("=", 1)[1])
                break
        run_streamlit_server(script, port)
        return 0

    proc = None
    try:
        script_path = main_app_path()
        port = find_free_port(DEFAULT_PORT)
        proc = start_streamlit_process(script_path, port)
        atexit.register(stop_process, proc)

        wait_for_server(port)
        launch_desktop_window(port)
    except KeyboardInterrupt:
        pass
    except Exception as exc:  # noqa: BLE001
        show_error(f"{APP_TITLE} failed to start:\n\n{exc}")
        return 1
    finally:
        stop_process(proc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
