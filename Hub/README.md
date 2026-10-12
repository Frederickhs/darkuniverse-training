# Dark Universe Reporting Hub

The Dark Universe Reporting Hub is a Windows desktop launcher that runs three independent Python reporting projects from one interface.

## Current Features

- Run any individual report
- Run all three reports in sequence
- Open configured input folders
- Open report output folders
- Open Reporting Hub logs
- Continue to remaining reports when one report fails
- Display a combined Success, Warning, or Failed summary
- Preserve each report project's existing business logic and workflow
- Support future Windows EXE packaging

## Independent Report Engines

The Hub launches these existing projects:

1. **PM Qualification Activity Tracker**
   - Project: `G:\Dev\Qual Tracker`
   - Runner: `G:\Dev\Qual Tracker\Run_Qualification_Tracker.bat`

2. **Qualification Coverage Report**
   - Project: `G:\Dev\Qualification Report`
   - Runner: `G:\Dev\Qualification Report\Run Qualification Report.bat`

3. **PQS Dark Universe Report**
   - Project: `G:\Dev\PQS Dark Universe Report`
   - Runner: `G:\Dev\PQS Dark Universe Report\Run_PQS_Dark_Universe_Report.bat`

The Hub is an orchestrator only. It does not contain or replace report-specific business logic.

## Architecture

Each report keeps its own:

- Git repository
- Python virtual environment
- Input folders
- Output folders
- Archive behavior
- Configuration
- Logs
- Historical evidence or snapshots
- Excel generation
- Error handling

The Hub launches each existing BAT runner and uses its Windows exit code to determine success or failure.

## Run Order

When **Run All Reports** is selected:

1. PM Qualification Activity Tracker
2. Qualification Coverage Report
3. PQS Dark Universe Report

The Hub waits for each report to finish before starting the next one. By default, a failure does not stop the remaining reports.

## Shared Qualification Source

The shared qualification folder is:

```text
G:\Dev\Qual Tracker\Input\Qualification
```

The Hub must never move, rename, edit, archive, or delete files in this folder.

## Project Structure

```text
Dark Universe Reporting HUB
├── .github
│   └── copilot-instructions.md
├── Config
│   └── reports.json
├── Documentation
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   └── RUNBOOK.md
├── Logs
│   └── .gitkeep
├── Scripts
│   ├── config_loader.py
│   ├── folder_manager.py
│   ├── log_manager.py
│   ├── report_runner.py
│   └── reporting_hub.py
├── Tests
├── .gitignore
├── AGENTS.md
├── AI_WORKFLOW.md
├── CLAUDE.md
├── README.md
├── requirements.txt
├── Build Reporting Hub.bat
└── Run Reporting Hub.bat
```

## Configuration

Central configuration is stored in:

```text
Configeports.json
```

Windows paths in JSON require double backslashes:

```json
"G:\Dev\Qual Tracker"
```

Configurable paths must remain in `reports.json` instead of being duplicated throughout the Python code.

## Development Run

```powershell
.\.venv\Scripts\Activate.ps1
python Scriptseporting_hub.py
```

Before running reports, close all related input and output Excel workbooks.

## Validation Commands

```powershell
python -m json.tool Configeports.json
python Scripts\config_loader.py
python Scriptsolder_manager.py
python Scripts\log_manager.py
python Scriptseport_runner.py
python Scriptseporting_hub.py
```

`report_runner.py` validates the configured project folders, runners, and output folders without executing reports when run directly.

## Logging

The Hub creates timestamped logs in `Logs`. Runtime logs must not be committed.

Logs record application activity, folder shortcuts, report starts, results, durations, exit codes, and Hub errors.

## Tested Workflow

The **Run All Reports** workflow was successfully validated on October 8, 2026. All three report engines completed successfully and the Hub displayed one combined summary.

## Requirements

- Windows 11
- Python 3.14.8 for development
- PyInstaller 6.22.3 for EXE packaging
- Existing report projects in their configured locations

Install development requirements:

```powershell
python -m pip install -r requirements.txt
```

## Privacy

Never commit:

- Employee names
- SSOs or Labor IDs
- Maximo exports
- Qualification or task exports
- Line schedules or rosters
- Generated workbooks
- Archives
- Runtime logs
- Historical cycle evidence
- PQS snapshots
- Virtual environments
- Excel temporary files

Tests must use synthetic data such as `900000001`, `900000002`, and `900000003`.

## Development Rules

1. Do not duplicate report business logic in the Hub.
2. Do not combine the report engines into one large Python file.
3. Do not modify existing report repositories unless explicitly requested.
4. Do not edit or archive source input files.
5. Keep configurable paths in `Configeports.json`.
6. Preserve report independence and continue-after-failure behavior.
7. Test each report individually before testing all reports.
8. Test the Python application before rebuilding the EXE.
9. Confirm private files remain excluded from Git.
10. Do not commit or push automatically.

## Git

Repository:

```text
https://github.com/Frederickhs/dark-universe-reporting-hub.git
```

Default branch: `main`

When Git save instructions are requested, provide one PowerShell line:

```powershell
git add .; git commit -m "Describe the change"; git push
```
