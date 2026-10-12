# Coding Agent Instructions

## Scope

These instructions apply to Codex and any automated coding agent working in the Dark Universe Reporting Hub repository.

## System Boundary

The Hub is a parent orchestrator. The three report engines are external systems:

- PM Qualification Activity Tracker
- Qualification Coverage Report
- PQS Dark Universe Report

Do not absorb their parsing, calculation, Excel, archive, snapshot, or historical-evidence logic into this repository.

## Required Design Principles

- Configuration over duplicated hardcoded paths
- Small focused modules
- Windows path safety
- Structured report results
- Sequential report execution
- Continue-after-failure support
- Background execution so tkinter remains responsive
- No source-input modification
- No employee data in Git

## Change Ownership

A change belongs in the Hub when it affects:

- Launcher interface
- Report selection
- Execution order
- Combined summaries
- Hub logging
- Input or output folder shortcuts
- Central configuration
- EXE packaging

A change belongs in a report project when it affects:

- Report calculations
- Source parsing
- Workbook content or formatting
- Qualification, PM-cycle, or PQS business rules
- Report-specific archive behavior
- Historical evidence or snapshots

Do not edit an external report repository from this repository without explicit user approval.

## Coding Standards

- Use Python type hints.
- Use `pathlib.Path` for paths.
- Use docstrings for public functions and classes.
- Keep UI work on the tkinter main thread.
- Run report processes in a background thread.
- Use subprocess argument lists rather than unsafe command-string construction.
- Preserve report exit codes.
- Return structured results instead of parsing console text for business outcomes.
- Provide clear user-facing error messages.

## Testing

Use synthetic paths and employee identifiers in automated tests. Tests must not launch production reports unless explicitly designated as integration tests.

Minimum validation before completion:

```powershell
python -m json.tool Configeports.json
python Scripts\config_loader.py
python Scriptsolder_manager.py
python Scriptseport_runner.py
```

Run the full UI manually after interface or orchestration changes.

## Security and Privacy

Do not commit or expose:

- Employee names or SSOs
- Maximo files
- Rosters
- Qualification exports
- Task reports
- Generated workbooks
- Archives
- Hub or report logs
- Snapshots or cycle history
- Virtual environments

## Git Restrictions

Never commit, amend, rebase, force-push, or push unless explicitly requested. When the user requests Git save instructions, provide add, commit, and push on one PowerShell line.
