# Dark Universe Training Reporting System

A centralized local reporting repository for Dark Universe training operations. The project combines a Windows Reporting Hub, operational Excel reports, shared source inputs, Search SSO, and manual PQS PDF generation.

The system runs locally with Python and Excel files. It does not require a hosted service or a live connection to IBM Maximo.

## Main Features

- One Reporting Hub for the active reporting tools
- Run reports individually or use **Run All Reports**
- Search a team member by SSO across current local report data
- Generate Full PQS Venue and Partial Module PDF blue sheets
- Build the Reporting Hub as a Windows EXE
- Use shared input folders across report projects
- Preserve report-specific configuration, output, archive, and logging folders

## Reporting Hub

The Reporting Hub is located in:

```text
Hub
```

### Hub tools

- **PM Qualification Activity Tracker**
- **Qualification Coverage Report**
- **PQS Dark Universe Report**
- **Search SSO**
- **Generate PQS PDF**
- Input, Output, and Log folder shortcuts

### Start the development Hub

Run:

```text
Hub\Run Reporting Hub.bat
```

### Build the Windows EXE

Run:

```text
Hub\Build Reporting Hub.bat
```

The build process includes the Search SSO module, PQS PDF Generator, and both PDF templates.

## Search SSO

Search SSO combines information from the current local reports using SSO or Employee ID.

When the SSO appears on the current Dark Universe Line Schedule, the search can display:

- Profile and Line Schedule information
- PQS module status and progress
- Maximo module status
- Work Order numbers for `INPRG` and `COMP` module records
- PM qualification cycles and task evidence
- SuccessFactors training items

When the SSO does not appear on the current Line Schedule but exists in the SuccessFactors export, Search SSO displays the available SuccessFactors information.

SuccessFactors items are considered outstanding when:

```text
Days Until Due <= 15
```

Supervisor, manager, HR box, and Overhire information are not displayed in Search SSO.

## PQS PDF Generator

The main Hub includes a manual **Generate PQS PDF** tool. Manual entry allows the forms to be used for Dark Universe and other venues.

### Supported forms

- Full PQS Venue Blue Sheet
- Partial Modules Blue Sheet

### Available fields

- Form type
- Technician name
- Technician SSO
- Venue
- Module for Partial Module forms
- Work Order
- RCM Trainer name
- RCM Trainer SSO
- Supervisor name and ID
- Manager name and ID
- Date and time

The default trainer information can be edited before generating the PDF.

### PDF folders

```text
Hub\PDF Templates
Hub\PDF Output
```

Templates:

```text
Full PQS Venue Blue Sheet to Fill.pdf
Partial Modules Blue Sheet to Fill.pdf
```

Generated PDFs are saved locally in `Hub\PDF Output`. Generated output PDFs are excluded from Git.

## Active Reports

### PM Qualification Activity Tracker

Evaluates annual PM activity by qualification using Maximo qualification and task exports.

Key behavior:

- Uses SSO plus qualification as the match
- Counts tasks with `Status = COMP`
- Assigns a valid task only to its correct annual cycle
- Keeps annual cycles tied to the original qualification effective date
- Uses a 30-day Due Soon threshold
- Produces separate venue workbooks
- Separates Animation roster members from the standard Unchained output

Project folder:

```text
Reports\PM Qualification Activity Tracker
```

### Qualification Coverage Report

Compares team members from the current Line Schedule with qualification exports and creates qualification coverage information.

Project folder:

```text
Reports\Qualification Coverage Report
```

### PQS Dark Universe Report

Tracks PQS module completion, progress, readiness, Work Orders, roster information, and Maximo data for Dark Universe.

Project folder:

```text
Reports\PQS Dark Universe Report
```

## Shared Inputs

Shared source files are stored under:

```text
Shared\Input
```

Main shared input folders:

```text
Shared\Input\Line Schedule
Shared\Input\Qualification
Shared\Input\SF Report
Shared\Input\Tasks
```

Report-specific inputs remain inside their report project when they are not shared.

## Repository Structure

```text
Dark Universe Training
├── Hub
│   ├── PDF Output
│   ├── PDF Templates
│   ├── Scripts
│   ├── Build Reporting Hub.bat
│   ├── Run Reporting Hub.bat
│   └── requirements.txt
├── Reports
│   ├── PM Qualification Activity Tracker
│   ├── PQS Dark Universe Report
│   └── Qualification Coverage Report
├── Shared
│   ├── Config
│   └── Input
├── .gitignore
└── README.md
```

## Local Setup

### Requirements

- Windows
- Python
- Microsoft Excel for viewing generated workbooks
- A PDF reader for previewing generated PQS forms

Hub Python packages are listed in:

```text
Hub\requirements.txt
```

Current Hub dependencies include:

- `pyinstaller`
- `openpyxl`
- `pypdf`

### Install Hub dependencies

From the repository root:

```powershell
.\Hub\.venv\Scripts\python.exe -m pip install -r ".\Hub\requirements.txt"
```

## Standard Workflow

1. Place current exports in the correct Shared or report-specific input folders.
2. Start the Reporting Hub.
3. Run the required report or use **Run All Reports**.
4. Review generated workbooks in each report's Output folder.
5. Use Search SSO for team-member-level review.
6. Use Generate PQS PDF when a Full or Partial PQS blue sheet is required.
7. Review report exceptions and logs before using the results operationally.

## Source Data Rules

- Input exports should remain unedited whenever possible.
- SSO or Employee ID is the primary person identifier across reports.
- Previous outputs may be archived before a new report is generated.
- Inputs must remain in their Input folders after processing.
- Live IBM Maximo integration is not required. The current workflow uses downloaded reports.

## Git and Generated Files

The repository excludes generated or local-only content such as:

- Python virtual environments
- Python cache files
- PyInstaller build and distribution folders
- Hub-generated PDF output
- Logs
- Temporary Excel files
- Report outputs, archives, and local input data where configured by `.gitignore`

Before committing changes, review:

```powershell
git status --short
```

## Validation

Before building or committing Python changes, run:

```powershell
.\Hub\.venv\Scripts\python.exe -m py_compile ".\Hub\Scripts\reporting_hub.py" ".\Hub\Scripts\search_sso_hub.py" ".\Hub\Scripts\pqs_pdf_generator.py"
```

Before committing, check whitespace and merge-marker errors:

```powershell
git diff --check
```

## Data Handling

This repository processes employee identifiers, training information, qualification data, schedules, and operational task information. Keep real inputs, generated reports, and PDFs only in approved local or organizational storage locations. Do not commit employee data, operational exports, generated PDFs, credentials, or API keys to Git.
