# Claude Code Instructions

## Project Purpose

This repository contains the Dark Universe Reporting Hub, a Windows desktop orchestrator for three independent Python reporting projects.

The Hub is not a replacement for the report engines. It launches their existing BAT files, opens configured folders, records Hub-level logs, and presents combined execution results.

## Existing Report Projects

- `G:\Dev\Qual Tracker`
- `G:\Dev\Qualification Report`
- `G:\Dev\PQS Dark Universe Report`

Do not move, merge, copy, or redesign these projects unless the user explicitly requests it.

## Mandatory Architecture Rules

1. Keep all report-specific business logic outside the Hub.
2. Do not combine the three report engines into one Python file.
3. Use each project's existing BAT runner and virtual environment.
4. Keep paths and run order in `Config\reports.json`.
5. Continue remaining reports after one failure unless configuration explicitly disables that behavior.
6. Treat shared qualification inputs as read-only.
7. Never modify source input files from the Hub.
8. Preserve each project's output archiving, history, snapshots, and error handling.

## Current Hub Modules

- `Scripts/config_loader.py`: loads and validates JSON configuration
- `Scripts/folder_manager.py`: validates and opens configured folders
- `Scripts/log_manager.py`: creates timestamped Hub logs
- `Scripts/report_runner.py`: launches independent BAT runners and returns structured results
- `Scripts/reporting_hub.py`: tkinter desktop interface and orchestration

## Development Workflow

Before changing code:

1. Read `README.md`.
2. Read `Documentation/ARCHITECTURE.md`.
3. Inspect `Config/reports.json`.
4. Identify whether the requested change belongs to the Hub or an independent report project.
5. Ask for clarification if ownership is uncertain.

After changing code:

1. Validate JSON.
2. Run module-level validation.
3. Run the Hub as Python.
4. Test folder buttons.
5. Test one report before Run All Reports.
6. Rebuild the EXE only after Python validation passes.

## Validation Commands

```powershell
python -m json.tool Config
eports.json
python Scripts\config_loader.py
python Scripts\Folder_manager.py
python Scripts\log_manager.py
python Scripts
eport_runner.py
python Scripts
eporting_hub.py
```

## Data Protection

Never read private source files unless the task explicitly requires validation. Never place real employee data in code, tests, documentation, logs, screenshots, examples, or Git.

Never commit Input, Output, Archive, Logs, Data, snapshots, historical evidence, `.venv`, build output, or Excel temporary files.

Use synthetic SSOs beginning with `900000` in tests.

## Git Rules

- Do not commit or push automatically.
- Do not rewrite history unless explicitly requested.
- Before suggesting a commit, inspect `git status`.
- When requested, provide one PowerShell command:

```powershell
git add .; git commit -m "Describe the change"; git push
```

## Communication Style

Use clear, direct language. Explain changes one checkpoint at a time. Do not assume missing business rules or paths. Ask before changing an independent report project.
