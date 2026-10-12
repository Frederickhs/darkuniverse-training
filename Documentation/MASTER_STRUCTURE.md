# Master Repository Structure

```text
darkuniverse-training/
├── Config/
│   └── shared_paths.json
├── Documentation/
├── Hub/
│   ├── Config/
│   ├── Documentation/
│   ├── Logs/
│   └── Scripts/
├── Reports/
│   ├── PM Qualification Activity Tracker/
│   ├── Qualification Coverage Report/
│   └── PQS Dark Universe Report/
└── Shared/
    └── Input/
        ├── Line Schedule/
        └── Qualification/
```

The report folders remain separate applications. Centralization means one repository, one Hub, and one shared path configuration, not one giant Python script.
