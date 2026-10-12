# Dark Universe Training

Centralized local reporting system for Dark Universe training operations. The repository combines the Reporting Hub, three operational report projects, shared source inputs, and Search SSO.

## Current Features

- One Reporting Hub for the three active reports
- Run reports individually or with **Run All Reports**
- Search SSO across Line Schedule, PQS, PM-cycle, and SuccessFactors information
- Shared Line Schedule, qualification, Maximo task, and SuccessFactors input folders
- Persistent PM cycle evidence through `cycle_history.csv`
- Local Python environments and a packaged Windows Hub EXE

## Active Reports

1. **PM Qualification Activity Tracker**
   - Evaluates qualification-specific annual PM cycles.
   - Uses completed Maximo tasks and permanent cycle history.
   - Produces separate venue workbooks.

2. **Qualification Coverage Report**
   - Compares current Line Schedule team members with qualification exports.
   - Produces qualification coverage information for Dark Universe.

3. **PQS Dark Universe Report**
   - Tracks PQS module status, progress, readiness, rosters, exceptions, and Maximo information.

## Search SSO

Search SSO is available from the Reporting Hub.

- If an SSO is on the current Dark Universe Line Schedule, Search SSO shows Line Schedule, PQS, PM-cycle, and SuccessFactors information.
- If an SSO is not on the Line Schedule but exists in the current SuccessFactors export, Search SSO shows SuccessFactors information only and identifies the person as not currently listed on the Dark Universe Line Schedule.
- SuccessFactors items are outstanding when `Days Until Due <= 15`.
- If the person has no outstanding SuccessFactors items, Search SSO displays **All Good**.
- Working days are derived from the Line Schedule weekday columns. `OFF` means off; a blank weekday cell means scheduled to work.
- Supervisor, manager, and HR Box details are intentionally excluded from Search SSO.

## Repository Structure

```text
darkuniverse-training/
├── Config/
│   └── shared_paths.json
├── Documentation/
├── Hub/
│   ├── Config/
│   ├── Scripts/
│   └── dist/                       # Local build, excluded from Git
├── Reports/
│   ├── PM Qualification Activity Tracker/
│   ├── Qualification Coverage Report/
│   └── PQS Dark Universe Report/
├── Shared/
│   └── Input/
│       ├── Line Schedule/
│       ├── Qualification/
│       ├── Tasks/
│       └── SF Report/
└── README.md
```

## Private Data

Operational source data and generated files must remain local and excluded from Git, including:

- Excel inputs and outputs
- Maximo exports
- Rosters
- Archives and logs
- `.venv` folders
- PM `cycle_history.csv`
- Built EXE files

Always review the complete untracked-file list before committing:

```powershell
git status --short --untracked-files=all
```

## Normal Use

1. Update the applicable files under `Shared\Input`.
2. Update report-specific PQS or roster inputs when needed.
3. Run the Reporting Hub EXE.
4. Run an individual report or **Run All Reports**.
5. Review the combined result summary.
6. Use Search SSO against the newest source files and generated report outputs.

## Development Launch

```text
Hub\Run Reporting Hub.bat
```

## Build the Hub EXE

Close the development Hub, Search SSO, and any existing built Hub process. Then run:

```text
Hub\Build Reporting Hub.bat
```

Built application:

```text
Hub\dist\Dark Universe Reporting Hub.exe
```

## Documentation

- `Documentation/ARCHITECTURE.md`
- `Documentation/RUNBOOK.md`
- `Documentation/SETUP_AND_RECOVERY.md`
- `Documentation/SEARCH_SSO.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `AGENTS.md`
- `CLAUDE.md`

## Repository

[Dark Universe Training repository](https://github.com/Frederickhs/darkuniverse-training.git)
