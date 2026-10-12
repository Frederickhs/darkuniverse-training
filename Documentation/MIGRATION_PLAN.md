# Migration Plan

## Scope

Migrate only these applications:

- PM Qualification Activity Tracker
- Qualification Coverage Report
- PQS Dark Universe Report
- Dark Universe Reporting Hub

SF Weekly Report is excluded.

## Migration rules

1. Preserve each report's business logic.
2. Preserve PM cycle history and PQS snapshots.
3. Do not commit real input, output, archive, log, history, or snapshot data.
4. Use one shared Line Schedule folder.
5. Use one shared qualification folder.
6. Update applications to read shared paths from the master configuration.
7. Validate each report individually before enabling Run All Reports.
8. Keep the old repositories unchanged until the consolidated versions pass validation.

## Planned order

1. Create the master structure.
2. Copy the three report codebases into `Reports`.
3. Copy the Hub codebase into `Hub` and remove SF Weekly Report from configuration.
4. Centralize shared path loading.
5. Migrate private operational folders locally without committing them.
6. Validate individual report runners.
7. Validate the Hub.
8. Commit the consolidated source only after validation.
