@echo off
setlocal
cd /d "%~dp0"
title Install PQS Missing Maximo Flag V3
set "PYTHON_EXE=G:\Dev\darkuniverse-training\Reports\PQS Dark Universe Report\.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" (
  echo Required Python environment not found:
  echo %PYTHON_EXE%
  pause
  exit /b 1
)
"%PYTHON_EXE%" "%~dp0install_missing_maximo_flag.py"
set "EXIT_CODE=%ERRORLEVEL%"
echo.
if "%EXIT_CODE%"=="0" (echo PQS MISSING MAXIMO UPDATE COMPLETED.) else (echo UPDATE FAILED. Review the error above.)
echo.
pause
exit /b %EXIT_CODE%
