# Changelog

All notable changes to Dark Universe Training are documented here.

The project uses semantic-style versions for documented releases. Dates should reflect the actual commit or release date when a version is finalized.

## [Unreleased]

### Planned

- Complete and validate the permanent Setup and Repair utility.
- Continue normal operational testing of the built Reporting Hub.
- Revisit wider SuccessFactors integration only after the current baseline remains stable.

### Added

- Root documentation suite for repository operation and maintenance.

## [0.3.0] - 2026-10-12

### Added

- Search SSO in the Reporting Hub.
- Full Dark Universe results for current Line Schedule members.
- SuccessFactors-only results for people outside the Dark Universe Line Schedule.
- First name, last name, SSO, shift, and working-day display.
- Structured PQS module results.
- Structured PM results with one row per cycle and cycle status.
- SuccessFactors outstanding-item display using `Days Until Due <= 15`.
- **All Good** SuccessFactors result when no outstanding items exist.
- EXE-compatible Search SSO integration.

### Changed

- Reduced the Search SSO window size.
- Removed supervisor, manager, and HR Box information from Search SSO.
- Updated working-day logic so `OFF` is excluded and blank weekday cells are treated as working days.
- Updated the Hub build to package Search SSO.

## [0.2.0] - 2026-10-12

### Added

- Central Reporting Hub with three active reports.
- Shared input folders for Line Schedule, qualifications, Maximo tasks, and a reserved SuccessFactors source.
- Central path configuration.
- Hub support for individual report runs and Run All Reports.

### Changed

- Migrated active report code into the master repository.
- Updated report paths to use the centralized repository.
- Preserved private operational inputs outside Git.

### Validated

- PM Qualification Activity Tracker individual run.
- Qualification Coverage Report individual run.
- PQS Dark Universe Report individual run.
- Hub individual report runs.
- Hub Run All Reports with three successful reports.

## [0.1.0] - 2026-10-12

### Added

- Initial master repository foundation.
- Repository-level `.gitignore`.
- Initial structure and migration documentation.
