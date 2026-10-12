# Operations Runbook

## Daily or Ad Hoc Use

1. Confirm the newest required source files are present.
2. Launch `Hub\dist\Dark Universe Reporting Hub.exe`.
3. Run the required report or select **Run All Reports**.
4. Review the completion summary.
5. Confirm the newest output workbook was created.
6. Use Search SSO as needed.

## Monthly PM Workflow

1. Download the current rolling Maximo task exports without editing them.
2. Replace or update the files in `Shared\Input\Tasks`.
3. Confirm qualification exports are current.
4. Run the PM Qualification Activity Tracker.
5. Confirm `cycle_history.csv` remains in place.
6. Review the Run Summary and Exceptions sheets.

## Search SSO Source Refresh

Search SSO reads:

- Current Line Schedule workbook
- Newest raw SuccessFactors workbook
- Latest generated PQS output
- Latest generated PM output workbooks

Run PQS and PM reports after their sources change so Search SSO reflects the latest generated outputs.

## Build the Hub

1. Close the Hub and Search SSO.
2. End a remaining `Dark Universe Reporting Hub.exe` process if Windows kept it open.
3. Run `Hub\Build Reporting Hub.bat`.
4. Confirm the build reports success.
5. Test the built EXE.

## Build Error: Access Denied

If PyInstaller cannot replace the EXE, close the built Hub. Then run:

```powershell
Stop-Process -Name "Dark Universe Reporting Hub" -Force -ErrorAction SilentlyContinue
```

Run the build again.

## JSON BOM Error

Python files using `encoding="utf-8"` cannot read a JSON file saved with a UTF-8 BOM. Save the JSON as UTF-8 without BOM and validate it before rerunning the application.

## Git Safety Check

```powershell
git status --short --untracked-files=all
```
