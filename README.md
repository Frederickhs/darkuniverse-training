# Dark Universe Training

Central repository for the Dark Universe reporting tools and Reporting Hub.

## Included applications

1. PM Qualification Activity Tracker
2. Qualification Coverage Report
3. PQS Dark Universe Report
4. Dark Universe Reporting Hub

SF Weekly Report is intentionally excluded.

## Design

- Each report keeps its own Python modules and business rules.
- Shared source locations are defined once in `Config/shared_paths.json`.
- Private operational data, generated reports, archives, logs, history, snapshots, and virtual environments are excluded from Git.
- Employee ID / SSO remains the cross-source identity key.

## Local repository

`G:\Dev\darkuniverse-training`

## Repository structure

```text
Config/                 Shared path configuration
Hub/                    Reporting Hub application
Reports/                Three independent report engines
Shared/Input/           Shared Line Schedule and qualification exports
Documentation/          Master architecture and migration records
```

Do not place real employee data in GitHub.
