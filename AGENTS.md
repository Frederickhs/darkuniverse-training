# AGENTS.md

Instructions for coding agents working in this repository.

## Repository Purpose

This repository is the central local reporting system for Dark Universe training operations. Changes can affect live operational outputs. Preserve existing business logic unless a requested change explicitly updates that logic.

## Non-Negotiable Rules

1. Never commit private operational data.
2. Never delete or regenerate `cycle_history.csv` without explicit direction and a verified backup.
3. Do not silently change qualification, PQS, PM-cycle, readiness, or SuccessFactors status rules.
4. Preserve absolute-path compatibility with `G:\Dev\darkuniverse-training` until path portability is implemented deliberately.
5. Keep SF Weekly Report generation outside the Hub unless the scope is explicitly expanded. The current Hub uses only Search SSO data-reading functionality.
6. Search SSO must continue to show SF-only results for people outside the current Dark Universe Line Schedule.
7. Supervisor, manager, and HR Box information must remain excluded from Search SSO.
8. The Hub must continue to run exactly three active reports. Search SSO is a Hub utility, not a fourth report.

## Required Workflow

Before changing code:

1. Read the root `README.md`.
2. Read the relevant report README and documentation.
3. Inspect the current source file instead of assuming its structure.
4. Preserve the existing working behavior with a backup or Git checkpoint.

After changing code:

1. Compile changed Python files.
2. Run the affected application in development mode.
3. Test the built EXE when Hub packaging changes.
4. Review `git status --short --untracked-files=all`.
5. Confirm that no private files are staged.

## Business Rules to Preserve

### Search SSO

- Line Schedule member: show Line Schedule, PQS, PM, and SF information.
- Not on Line Schedule but found in SF: show SF only and the non-Dark-Universe notice.
- SF outstanding item: `Days Until Due <= 15`.
- No outstanding SF items: show **All Good**.
- Line Schedule working day: blank weekday cell.
- Line Schedule day off: cell value `OFF`.

### PM Qualification Activity Tracker

- Annual cycles stay permanently tied to the original qualification effective date.
- A task counts only in the cycle containing its completion date.
- Completed-cycle evidence persists through `cycle_history.csv`.
- Mod 0 qualifications remain excluded from PM activity reporting.

## Coding Standards

- Use `pathlib.Path` for Python paths.
- Keep file encodings UTF-8 without BOM for JSON read by Python with `encoding="utf-8"`.
- Keep UI file reading off the Tkinter main thread.
- Return UI updates to the Tkinter thread with `after`.
- Prefer clear functions over large inline blocks.
- Add graceful messages for missing optional data.
- Never expose supervisor, manager, or other unnecessary personal data in Search SSO.

## Packaging

The build entry point is:

```text
Hub\Build Reporting Hub.bat
```

Search SSO must be importable by `reporting_hub.py` and included in the PyInstaller build.

## Git

Use a specific commit message. Before committing:

```powershell
git status --short --untracked-files=all
```

Typical command format:

```powershell
git add .; git commit -m "Describe the validated change"; git push
```
