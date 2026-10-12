@echo off
setlocal
title Dark Universe Reporting Hub

cd /d "%~dp0"

if not exist ".venv\Scripts\pythonw.exe" (
    echo ERROR: The Reporting Hub Python environment was not found.
    echo Expected: %CD%\.venv\Scripts\pythonw.exe
    echo.
    pause
    exit /b 1
)

start "" ".venv\Scripts\pythonw.exe" "Scripts\reporting_hub.py"

endlocal
exit /b 0