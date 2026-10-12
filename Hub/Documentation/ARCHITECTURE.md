# Architecture

## Overview

The Dark Universe Reporting Hub is a lightweight Windows desktop orchestrator built with tkinter. It provides one interface for three existing report engines while preserving their independence.

## Components

### Configuration Layer

`Config/reports.json` defines Hub settings, report paths, BAT runners, input folders, output folders, archive folders, and run order.

### Configuration Loader

`Scripts/config_loader.py` loads JSON and validates required sections, report fields, and run-order references.

### Folder Manager

`Scripts/folder_manager.py` validates configured folders and opens them in Windows File Explorer. Folder actions are read-only from the Hub's perspective.

### Log Manager

`Scripts/log_manager.py` creates timestamped Hub logs and records launcher-level activity.

### Report Runner

`Scripts/report_runner.py` validates and launches each external BAT runner. It records duration, return code, status, output folder, and details in a structured `ReportResult`.

BAT processes receive no interactive standard input so final `pause` commands do not block Hub automation.

### Desktop Interface

`Scripts/reporting_hub.py` provides report buttons, Run All Reports, folder windows, progress display, confirmation prompts, and combined results.

Report execution occurs in a background thread. tkinter updates are scheduled on the main thread.

## Execution Flow

1. Load and validate configuration.
2. Configure Hub logging.
3. Display the interface.
4. User selects one report or all reports.
5. Hub requests confirmation.
6. Selected report BAT files run sequentially.
7. Each report preserves its own archive and output workflow.
8. Hub records each exit code and duration.
9. Hub continues after failure when configured.
10. Hub presents a combined summary.

## External System Boundary

The Hub does not parse Maximo files, calculate report metrics, build report workbooks, maintain PM history, or create PQS snapshots.

Those functions remain in the independent report projects.

## Failure Model

- Missing project, runner, or output path: FAILED before launch
- BAT exit code `0`: SUCCESS
- Nonzero BAT exit code: FAILED
- Timeout: FAILED
- Windows launch error: FAILED
- One report failure: remaining reports continue by default

## EXE Model

The packaged EXE contains the Hub interface and orchestration code only. It does not package the three report engines or their pandas/openpyxl environments.

The external project paths must remain available according to `Config/reports.json`.
