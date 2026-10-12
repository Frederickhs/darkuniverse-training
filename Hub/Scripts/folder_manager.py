import os
from pathlib import Path
from typing import Any

from config_loader import load_config


def open_folder(folder_path: str | Path) -> None:
    """Open an existing folder in Windows File Explorer."""

    path = Path(folder_path)

    if not path.exists():
        raise FileNotFoundError(
            f"The folder does not exist:\n{path}"
        )

    if not path.is_dir():
        raise NotADirectoryError(
            f"The configured path is not a folder:\n{path}"
        )

    os.startfile(path)


def get_input_folders(
    config: dict[str, Any],
) -> list[dict[str, str]]:
    """Return all configured input folders in display order."""

    input_folders = []

    for report_key in config["run_order"]:
        report = config["reports"][report_key]

        for button_name, folder_path in report["input_folders"].items():
            input_folders.append(
                {
                    "report_key": report_key,
                    "report_name": report["display_name"],
                    "button_name": button_name,
                    "folder_path": folder_path,
                }
            )

    return input_folders


def get_output_folders(
    config: dict[str, Any],
) -> list[dict[str, str]]:
    """Return all configured report output folders."""

    output_folders = []

    for report_key in config["run_order"]:
        report = config["reports"][report_key]

        output_folders.append(
            {
                "report_key": report_key,
                "report_name": report["display_name"],
                "folder_path": report["output_folder"],
            }
        )

    return output_folders


def validate_configured_folders(
    config: dict[str, Any],
) -> list[str]:
    """Return a list of missing configured folders without changing anything."""

    missing_folders = []

    for report_key in config["run_order"]:
        report = config["reports"][report_key]

        folders_to_check = {
            "Project": report["project_folder"],
            "Output": report["output_folder"],
            "Archive": report["archive_folder"],
            **report["input_folders"],
        }

        for folder_name, folder_path in folders_to_check.items():
            if not Path(folder_path).is_dir():
                missing_folders.append(
                    f"{report['display_name']} | "
                    f"{folder_name} | {folder_path}"
                )

    return missing_folders


if __name__ == "__main__":
    try:
        loaded_config = load_config()
        missing = validate_configured_folders(loaded_config)

        if missing:
            print("Missing or invalid configured folders:")

            for item in missing:
                print(f"  - {item}")

            raise SystemExit(1)

        input_count = len(get_input_folders(loaded_config))
        output_count = len(get_output_folders(loaded_config))

        print("Folder configuration validated successfully.")
        print(f"Input folder buttons configured: {input_count}")
        print(f"Output folders configured: {output_count}")

    except (
        FileNotFoundError,
        NotADirectoryError,
        ValueError,
        KeyError,
    ) as error:
        print(f"Folder configuration error:\n{error}")
        raise SystemExit(1) from error