# Development Guide

## Environment

Tested development environment:

- Windows 11
- Python 3.14.8
- PyInstaller 6.22.3

## Setup

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python Scriptseporting_hub.py
```

## Validation

```powershell
python -m json.tool Configeports.json
python Scripts\config_loader.py
python Scriptsolder_manager.py
python Scripts\log_manager.py
python Scriptseport_runner.py
```

Direct execution of `report_runner.py` validates paths without running reports.

## Coding Guidelines

- Keep modules focused.
- Use type hints and docstrings.
- Use `pathlib.Path`.
- Keep configuration in JSON.
- Use subprocess argument lists.
- Preserve external process exit codes.
- Do not parse console output as the primary success signal.
- Keep tkinter responsive with background report execution.
- Schedule UI updates through the tkinter main thread.

## Safe Testing Order

1. Validate JSON.
2. Validate configuration loader.
3. Validate folders.
4. Validate runners without execution.
5. Open the Python UI.
6. Test input, output, and log buttons.
7. Run one report.
8. Run each remaining report individually.
9. Run all reports.
10. Build and test the EXE.

## Packaging

Use PyInstaller only after Python validation passes. The final build process should keep `Config/reports.json` external so paths can be updated without rebuilding the EXE.

Generated `build`, `dist`, and `.spec` files are excluded from Git.

## Failure Testing

Failure handling should be tested with a temporary test configuration or a controlled invalid path. Do not rename production folders or alter production inputs for a failure test.

Confirm that:

- The selected report shows FAILED.
- Remaining reports continue.
- Final summary contains all attempted reports.
- The Hub returns to an enabled state.
- The error is recorded in the Hub log.

## Git Checklist

Before a commit:

```powershell
git status
git diff --check
git diff
```

Confirm no logs, caches, employee data, workbooks, archives, snapshots, or virtual environments are staged.
