# Copilot Instructions

- Treat SSO as the shared identifier across the repository.
- Preserve the three-report Hub scope.
- Search SSO is a utility, not a report runner.
- Never commit private Excel files, outputs, rosters, Maximo exports, logs, archives, `.venv`, built files, or `cycle_history.csv`.
- Do not change business rules unless the user explicitly requests the change.
- Preserve PM annual-cycle anchoring to the original qualification effective date.
- Preserve completed PM evidence in `cycle_history.csv`.
- Search SSO SF outstanding threshold is `Days Until Due <= 15`.
- Search SSO must show SF-only information for people not on the current Dark Universe Line Schedule.
- `OFF` means a Line Schedule day off; blank weekday cells mean scheduled to work.
- Do not display supervisor, manager, or HR Box in Search SSO.
- Use UTF-8 without BOM for Python-read JSON files.
- Test development mode and the built EXE after Hub packaging changes.
- Before committing, run `git status --short --untracked-files=all`.
