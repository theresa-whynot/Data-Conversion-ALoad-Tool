# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec for the A-Load Generator desktop app.

Build on Windows:
    pyinstaller --noconfirm desktop_app.spec
"""

from __future__ import annotations

block_cipher = None

from PyInstaller.utils.hooks import collect_all, collect_data_files

datas = [
    ("frontend", "frontend"),
    ("backend", "backend"),
    ("resources", "resources"),
    ("README.md", "."),
    ("requirements.txt", "."),
]

hiddenimports = [
    "streamlit",
    "streamlit.web",
    "streamlit.web.cli",
    "streamlit.runtime",
    "streamlit.runtime.scriptrunner",
    "pandas",
    "openpyxl",
    "numpy",
    "webview",
    "webview.platforms.edgechromium",
    "tkinter",
    "tkinter.filedialog",
    "tkinter.messagebox",
]

binaries = []

# Avoid pulling pythonnet/clr into the default import path when possible.
excludes = [
    "pythonnet",
    "clr",
    "clr_loader",
]

for package in ("streamlit", "altair", "pydeck", "jsonschema", "webview"):
    try:
        pkg_datas, pkg_binaries, pkg_hidden = collect_all(package)
        datas += pkg_datas
        binaries += pkg_binaries
        hiddenimports += pkg_hidden
    except Exception:
        # Optional packages may be absent in some environments.
        pass

try:
    datas += collect_data_files("streamlit")
except Exception:
    pass


a = Analysis(
    ["desktop_launcher.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="ALoadGenerator",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # windowed app; no terminal
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ALoadGenerator",
)
