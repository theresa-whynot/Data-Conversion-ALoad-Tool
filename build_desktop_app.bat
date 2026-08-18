@echo off
setlocal

REM Build the A-Load Generator desktop app (Windows).
REM Run from the repo root in Git Bash or Command Prompt:
REM   build_desktop_app.bat

cd /d "%~dp0"

echo.
echo === Installing desktop build dependencies ===
python -m pip install --upgrade pip
python -m pip install -r requirements.txt -r requirements-desktop.txt

echo.
echo === Building ALoadGenerator with PyInstaller ===
python -m PyInstaller --noconfirm desktop_app.spec

if errorlevel 1 (
  echo.
  echo Build failed.
  exit /b 1
)

echo.
echo Build complete.
echo Open this folder and zip it to share the app:
echo   dist\ALoadGenerator\
echo.
echo Users can double-click:
echo   dist\ALoadGenerator\ALoadGenerator.exe
echo.
endlocal
