# Setup and Recovery

## New Computer or Fresh Clone

1. Clone the repository into `G:\Dev\darkuniverse-training`.
2. Restore private inputs from the approved local backup.
3. Restore PM `cycle_history.csv`.
4. Create the four local Python environments.
5. Install each project's `requirements.txt`.
6. Validate JSON configuration files.
7. Test each report individually.
8. Test the development Hub.
9. Build and test the packaged Hub.

## Required Python Environments

- `Hub\.venv`
- `Reports\PM Qualification Activity Tracker\.venv`
- `Reports\Qualification Coverage Report\.venv`
- `Reports\PQS Dark Universe Report\.venv`

## Persistent Files

The most important persistent PM file is:

```text
Reports\PM Qualification Activity Tracker\Data\cycle_history.csv
```

Treat this as operational history, not a recreatable cache.

## Rebuildable Files

The following can be recreated:

- `.venv`
- `__pycache__`
- Hub `build`
- Hub `dist`
- Generated report outputs

## Validation Checklist

- All four Python environments exist.
- `pip check` passes in each environment.
- Python files compile.
- JSON files parse.
- Shared input folders contain current Excel sources.
- PM cycle history exists.
- Three reports run individually.
- Hub Run All Reports succeeds.
- Search SSO passes all three test scenarios.
