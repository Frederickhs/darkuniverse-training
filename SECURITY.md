# Security and Data Handling

## Data Classification

This repository processes operational training data and employee identifiers. Source exports and generated results must remain in approved local storage and must not be committed to Git.

## Never Commit

- Employee rosters
- Line Schedule workbooks
- Qualification exports
- Maximo task exports
- SuccessFactors exports
- Generated reports
- Logs and archives
- `.venv` folders
- PM cycle history
- Built distribution files

## Minimum Exposure

Search SSO intentionally excludes:

- Supervisor information
- Manager information
- HR Box information

Do not add these fields back without a documented operational requirement.

## Git Review

Run before each commit:

```powershell
git status --short --untracked-files=all
```

If a private file appears:

1. Do not commit.
2. Update `.gitignore` if appropriate.
3. Remove the file from the staged set.
4. Confirm Git no longer lists the file.

## Incident Handling

If private data is committed:

1. Stop additional pushes.
2. Notify the repository owner.
3. Remove the file from Git history using an approved process.
4. Treat exposed credentials or sensitive exports according to organizational policy.
