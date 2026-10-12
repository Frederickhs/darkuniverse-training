# Operator Runbook

## Normal Use

1. Update the required source files using the **Input Folders** window.
2. Keep filenames and source formats required by each report project.
3. Close all input and output Excel workbooks.
4. Open the Dark Universe Reporting Hub.
5. Run one report or select **Run All Reports**.
6. Confirm the run.
7. Wait for the combined summary.
8. Use **Output Folders** to review generated workbooks.

## Run All Reports Order

1. PM Qualification Activity Tracker
2. Qualification Coverage Report
3. PQS Dark Universe Report

## Successful Run

A successful result shows:

- Status: SUCCESS for each completed report
- Processing time
- `Completed successfully` on the main window

Each report opens or updates its own output folder according to its existing workflow.

## If a Report Fails

1. Note the failed report and exit code in the Hub summary.
2. Open **Reporting Hub Logs**.
3. Run the failed report's original BAT file directly to see its detailed message.
4. Correct the report-specific input or file-lock issue.
5. Run that report again from the Hub.

The Hub does not replace detailed report-specific diagnostics.

## Common Problems

### Excel workbook is open

Close the workbook in desktop Excel. A report may fail when it cannot archive or replace an existing output safely.

### Required input is missing

Use **Input Folders** and restore the required current workbook. Do not rename files unless the report documentation requires a specific name.

### Report remains running after generation

A BAT may contain an interactive pause. The Hub normally supplies no interactive input so final pause commands return automatically. If a process still remains open, inspect the BAT for other interactive commands.

### Folder button fails

Validate the path in `Configeports.json`, then run:

```powershell
python Scriptsolder_manager.py
```

### Terminal color changes

A report BAT may use the Windows `color` command. This is cosmetic and does not affect output. Normal EXE use does not require a VS Code terminal.

## Source Data Protection

Never use the Hub to move, rename, archive, edit, or delete source input files. The shared qualification folder is read-only to the Hub.

## Escalation Information

When reporting a problem, capture:

- Report name
- Date and time
- Hub status
- Exit code
- Hub log filename
- Direct BAT error text
- Whether any workbook was open

Do not place employee names, SSOs, or source reports in GitHub issues or public messages.
