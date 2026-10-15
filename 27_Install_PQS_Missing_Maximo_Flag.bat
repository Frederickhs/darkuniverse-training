@echo off
setlocal
cd /d "%~dp0"
title Install PQS Missing Maximo Flag
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Install_PQS_Missing_Maximo_Flag.ps1"
set "EXIT_CODE=%ERRORLEVEL%"
echo.
if "%EXIT_CODE%"=="0" (echo PQS MISSING MAXIMO UPDATE COMPLETED.) else (echo UPDATE FAILED. Review the error above.)
echo.
pause
exit /b %EXIT_CODE%
