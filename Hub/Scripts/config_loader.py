import json
import sys
from pathlib import Path
from typing import Any


def get_hub_root() -> Path:
    """Return the application folder for Python and packaged EXE runs."""

    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent.parent


HUB_ROOT = get_hub_root()
CONFIG_FILE = HUB_ROOT / "Config" / "reports.json"


def load_config(config_file: Path = CONFIG_FILE) -> dict[str, Any]:
    """Load and validate the Reporting Hub configuration."""

    if not config_file.exists():
        raise FileNotFoundError(
            f"Configuration file was not found:\n{config_file}"
        )

    try:
        with config_file.open("r", encoding="utf-8") as file:
            config = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"The configuration file contains invalid JSON:\n"
            f"{config_file}\n\n"
            f"Line {error.lineno}, column {error.colno}: {error.msg}"
        ) from error

    validate_config(config)
    return config


def validate_config(config: dict[str, Any]) -> None:
    """Validate the required configuration sections and report settings."""

    required_sections = ["hub", "reports", "run_order"]

    for section in required_sections:
        if section not in config:
            raise ValueError(
                f"Missing required configuration section: {section}"
            )

    if not isinstance(config["reports"], dict) or not config["reports"]:
        raise ValueError(
            "The reports section must contain at least one report."
        )

    if not isinstance(config["run_order"], list):
        raise ValueError("The run_order section must be a list.")

    required_report_fields = [
        "display_name",
        "project_folder",
        "runner",
        "output_folder",
        "archive_folder",
        "input_folders",
    ]

    for report_key, report_config in config["reports"].items():
        for field in required_report_fields:
            if field not in report_config:
                raise ValueError(
                    f"Report '{report_key}' is missing the required "
                    f"field '{field}'."
                )

        if not isinstance(report_config["input_folders"], dict):
            raise ValueError(
                f"Report '{report_key}' has an invalid input_folders section."
            )

    for report_key in config["run_order"]:
        if report_key not in config["reports"]:
            raise ValueError(
                f"Run order references an unknown report: {report_key}"
            )


def get_report_config(
    config: dict[str, Any],
    report_key: str,
) -> dict[str, Any]:
    """Return the configuration for one report."""

    reports = config["reports"]

    if report_key not in reports:
        raise KeyError(f"Unknown report key: {report_key}")

    return reports[report_key]


if __name__ == "__main__":
    try:
        loaded_config = load_config()

        print("Configuration loaded successfully.")
        print(f"Hub: {loaded_config['hub']['name']}")
        print(f"Reports configured: {len(loaded_config['reports'])}")

        for key in loaded_config["run_order"]:
            report = get_report_config(loaded_config, key)
            print(f"  - {report['display_name']}")

    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f"Configuration error:\n{error}")
        raise SystemExit(1) from error