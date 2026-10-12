# AI-Assisted Development Workflow

## Purpose

This workflow provides a safe process for Claude Code, Codex, GitHub Copilot, and other AI tools working on the Dark Universe Reporting Hub.

## 1. Understand the Request

Determine whether the request affects:

- The Hub
- PM Qualification Activity Tracker
- Qualification Coverage Report
- PQS Dark Universe Report
- More than one repository

If the correct repository is unclear, stop and ask before editing.

## 2. Protect Working Systems

The three report projects are operational. Do not redesign, relocate, or consolidate the report engines as part of a Hub change.

Do not change source data, archive folders, snapshots, historical evidence, or report output files.

## 3. Inspect Before Editing

Review:

- `README.md`
- `Documentation/ARCHITECTURE.md`
- `Config/reports.json`
- Relevant Python modules
- `git status`

Do not rely on assumed filenames or paths. Validate them locally.

## 4. Make the Smallest Safe Change

Prefer targeted changes. Keep common launcher behavior in the Hub and business rules in the report-specific repositories.

Do not create one large Python file. Do not duplicate configuration across modules.

## 5. Validate in Layers

Run non-destructive checks first:

```powershell
python -m json.tool Configeports.json
python Scripts\config_loader.py
python Scriptsolder_manager.py
python Scriptseport_runner.py
```

Then run the UI:

```powershell
python Scriptseporting_hub.py
```

Test folder buttons before running reports. Test one report before Run All Reports.

## 6. EXE Workflow

Only rebuild the EXE after the Python application passes validation.

Verify:

- Startup without VS Code
- Configuration loading
- Folder shortcuts
- Individual report run
- Run All Reports
- Combined summary
- Hub logs
- No interactive BAT pauses

## 7. Privacy Review

Before committing, verify that Git does not include:

- `.venv`
- `Logs`
- `build`
- `dist`
- `__pycache__`
- Real input or output files
- Employee information
- Snapshots or history

## 8. Git Workflow

Do not commit automatically. When requested, provide:

```powershell
git add .; git commit -m "Describe the change"; git push
```

Use a specific commit message describing the validated change.
