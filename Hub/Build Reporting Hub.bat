@echo off
setlocal
title Build Dark Universe Reporting Hub

cd /d "%~dp0"

echo ============================================================
echo BUILD DARK UNIVERSE REPORTING HUB
echo ============================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: The Reporting Hub Python environment was not found.
    echo Expected: %CD%\.venv\Scripts\python.exe
    echo.
    pause
    exit /b 1
)

echo Checking PyInstaller...
".venv\Scripts\python.exe" -m PyInstaller --version
if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller is not installed.
    echo Run:
    echo .venv\Scripts\python.exe -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo Removing previous build files...

if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "Dark Universe Reporting Hub.spec" del /q "Dark Universe Reporting Hub.spec"

echo.
echo Building the Reporting Hub EXE...

".venv\Scripts\python.exe" -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "Dark Universe Reporting Hub" ^
    --paths "Scripts" ^
    "Scripts\reporting_hub.py"

if errorlevel 1 (
    echo.
    echo BUILD FAILED.
    echo Review the error messages above.
    echo.
    pause
    exit /b 1
)

echo.
echo Copying external configuration...

if not exist "dist\Config" mkdir "dist\Config"
copy /y "Config\reports.json" "dist\Config\reports.json" >nul

if errorlevel 1 (
    echo.
    echo BUILD FAILED: reports.json could not be copied.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo BUILD COMPLETED SUCCESSFULLY
echo ============================================================
echo.
echo EXE:
echo %CD%\dist\Dark Universe Reporting Hub.exe
echo.
echo Configuration:
echo %CD%\dist\Config\reports.json
echo.

start "" "%CD%\dist"
pause
endlocal
exit /b 0