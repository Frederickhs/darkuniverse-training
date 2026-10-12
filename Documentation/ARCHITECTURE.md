# Architecture

## Overview

Dark Universe Training is a local Windows reporting system centered on SSO as the shared identifier.

```text
Shared Inputs
    ├── Line Schedule
    ├── Qualification exports
    ├── Maximo task exports
    └── SuccessFactors Weekly Training
            |
            v
Reporting Hub
    ├── PM Qualification Activity Tracker
    ├── Qualification Coverage Report
    ├── PQS Dark Universe Report
    └── Search SSO
```

## Components

### Reporting Hub

- Desktop entry point for the system.
- Runs the three active reports.
- Provides Input, Output, Archive, and Log folder access.
- Provides Search SSO.
- Supports a packaged Windows EXE.

### Shared Inputs

- `Line Schedule`: current Dark Universe population, shift, and working-day context.
- `Qualification`: current qualification exports.
- `Tasks`: rolling completed Maximo task exports.
- `SF Report`: current raw SuccessFactors Weekly Training export.

### PM Qualification Activity Tracker

- Calculates annual qualification cycles.
- Matches completed PM tasks to the correct annual cycle.
- Preserves completed-cycle evidence in local history.

### Qualification Coverage Report

- Compares current scheduled team members with qualification exports.

### PQS Dark Universe Report

- Evaluates PQS progress, qualification status, exceptions, and readiness.

### Search SSO

- Uses Line Schedule membership to determine whether Dark Universe-specific sections should display.
- Reads current generated PQS and PM outputs.
- Reads the newest supported SuccessFactors source workbook.

## Data Boundaries

- Git contains code, configuration, and documentation.
- Local private folders contain operational sources and outputs.
- Python environments are local and recreatable.
- Built distributions are local and recreatable.

## Known Constraint

The current configuration uses absolute paths under `G:\Dev\darkuniverse-training`. Moving the repository requires coordinated path updates until path portability is implemented.
