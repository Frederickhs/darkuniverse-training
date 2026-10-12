# CLAUDE.md

Project context and working instructions for Claude-compatible coding workflows.

## Project Summary

Dark Universe Training is a Windows-based local Python reporting system. The master repository contains:

- Reporting Hub
- PM Qualification Activity Tracker
- Qualification Coverage Report
- PQS Dark Universe Report
- Search SSO
- Shared input configuration

The system uses local Excel exports. There is no live Maximo integration.

## Current Repository Location

```text
G:\Dev\darkuniverse-training
```

## Current Hub Scope

The Hub runs three reports:

1. PM Qualification Activity Tracker
2. Qualification Coverage Report
3. PQS Dark Universe Report

Search SSO is a Hub utility and must not be added to Run All Reports.

## Search SSO Contract

Search SSO combines:

- Current Line Schedule information
- Latest generated PQS output
- Latest generated PM output workbooks
- Newest raw SuccessFactors workbook in `Shared\Input\SF Report`

Rules:

- Dark Universe Line Schedule member: show all four sources.
- Person outside the Line Schedule: show SF information only.
- Outstanding SF item: `Days Until Due <= 15`.
- No outstanding items: **All Good**.
- `OFF` in the Line Schedule means off.
- Blank weekday cells mean scheduled to work.
- Exclude supervisor, manager, and HR Box information.

## Critical Persistent Data

```text
Reports\PM Qualification Activity Tracker\Data\cycle_history.csv
```

Do not delete, overwrite, normalize, or recreate this file without explicit instruction, a verified backup, and testing.

## Private Data

Never stage or commit:

- Source Excel files
- Generated report workbooks
- Maximo exports
- Rosters
- Logs
- Archives
- `.venv`
- `cycle_history.csv`
- Built EXE files

## Development Commands

Launch the Hub:

```text
Hub\Run Reporting Hub.bat
```

Build the Hub:

```text
Hub\Build Reporting Hub.bat
```

Validate Git contents:

```powershell
git status --short --untracked-files=all
```

## Change Discipline

- Make the smallest change that satisfies the requirement.
- Do not refactor working report logic while changing UI behavior.
- Preserve backward compatibility with existing input structures.
- Validate against real local outputs, not synthetic assumptions.
- Keep documentation synchronized with business-rule changes.
