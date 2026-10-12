# Contributing

## Scope

Changes should improve the centralized Dark Universe training system without breaking the three validated report workflows.

## Before Starting

1. Pull the latest `main` branch.
2. Confirm the working tree is clean.
3. Read `README.md`, `AGENTS.md`, and the affected project documentation.
4. Confirm private operational files remain covered by `.gitignore`.

## Development

- Use Python from the applicable project `.venv`.
- Keep report projects isolated unless the change is intentionally shared.
- Avoid changing business rules as part of UI or cleanup work.
- Preserve existing input file structures.

## Testing

Test the smallest affected area first.

### Report change

- Run the report individually.
- Verify the expected workbook exists.
- Review status totals and key known records.
- Test the report from the Hub.

### Hub change

- Launch the development Hub.
- Test the changed button or workflow.
- Run one individual report.
- Run All Reports if orchestration changed.

### Search SSO change

Test:

1. A Dark Universe SSO with PQS, PM, and SF data.
2. A non-Dark-Universe SSO with SF data only.
3. An SSO with no outstanding SF items.
4. The built Hub EXE when packaging or imports changed.

## Privacy Review

Before every commit:

```powershell
git status --short --untracked-files=all
```

Do not proceed if Git shows private inputs, outputs, `.venv`, logs, archives, rosters, Maximo exports, or cycle history.

## Commit and Push

Use a specific message:

```powershell
git add .; git commit -m "Describe the validated change"; git push
```
