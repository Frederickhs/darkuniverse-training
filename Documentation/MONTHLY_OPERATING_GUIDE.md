# Dark Universe Training Monthly Operating Guide

## Normal monthly sequence

1. Close the Reporting Hub and any generated Excel workbooks.
2. Update the current source exports in the shared input folders.
3. Update the report-specific PQS inputs when those sources have changed.
4. Run **Validate only** from `Setup and Repair Dark Universe Training.bat`.
5. Open the built Reporting Hub.
6. Run each report or select **Run All Reports**.
7. Review the combined result summary.
8. Test Search SSO for one Dark Universe team member.

## Shared input folders

| Source | Folder | Handling |
|---|---|---|
| Line Schedule | `Shared\Input\Line Schedule` | Keep the current official workbook. |
| Qualification exports | `Shared\Input\Qualification` | Replace with current unedited qualification exports. |
| Maximo task exports | `Shared\Input\Tasks` | Place the current rolling task exports here. |
| SuccessFactors Weekly Training | `Shared\Input\SF Report` | Keep the current raw Weekly Training export. Search SSO uses the newest supported workbook. |

## Report-specific inputs

### PM Qualification Activity Tracker

- Animation roster: `Reports\PM Qualification Activity Tracker\Input\Manual roster`
- Permanent cycle evidence: `Reports\PM Qualification Activity Tracker\Data\cycle_history.csv`

**Do not delete `cycle_history.csv`.** The tracker uses the file to preserve completed-cycle evidence after older tasks disappear from newer rolling exports.

### PQS Dark Universe Report

Update the applicable folders under:

- `Reports\PQS Dark Universe Report\Input\Maximo\Operations`
- `Reports\PQS Dark Universe Report\Input\Maximo\Animation`
- `Reports\PQS Dark Universe Report\Input\Rosters`
- `Reports\PQS Dark Universe Report\Input\Supervisors`
- `Reports\PQS Dark Universe Report\Input\Exceptions`

## Search SSO rules

- A person on the current Dark Universe Line Schedule receives Line Schedule, PQS, PM-cycle, and SuccessFactors information.
- A person outside the Line Schedule receives SuccessFactors information only and a non-Dark-Universe message.
- SuccessFactors items are outstanding when `Days Until Due <= 15`.
- If no SuccessFactors items meet that threshold, Search SSO shows **All Good**.
- Working days come from the Line Schedule weekday columns. `OFF` means off; a blank weekday cell means scheduled to work.

## Setup and Repair utility

`Setup and Repair Dark Universe Training.bat` provides:

1. **Validate only**: checks environments, requirements, Python syntax, JSON, required shared inputs, cycle history presence, and the built Hub EXE.
2. **Repair all Python environments**: creates missing environments and installs each project's requirements.
3. **Build Reporting Hub EXE**: closes a running built Hub process and runs the existing Hub build workflow.
4. **Full maintenance**: repairs environments, validates the repository, and builds the Hub if validation passes.

Logs are written to `Maintenance Logs`. The folder should remain excluded from Git.

## Files that must remain private

Do not commit:

- Excel input exports
- Generated outputs
- Archives
- Logs
- Rosters
- Maximo exports
- `.venv` folders
- `cycle_history.csv`

Before every commit, run:

```powershell
git status --short --untracked-files=all
```

## Recovery after moving to another computer

1. Clone the repository.
2. Restore the private input folders and `cycle_history.csv` from the approved local backup.
3. Update the absolute paths in the central configuration if the repository location changed.
4. Run **Repair all Python environments**.
5. Run **Validate only**.
6. Build and test the Reporting Hub EXE.
