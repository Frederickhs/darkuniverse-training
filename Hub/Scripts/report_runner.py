import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from config_loader import get_report_config, load_config


@dataclass
class ReportResult:
    """Store the result of one report execution."""

    report_key: str
    report_name: str
    status: str
    duration_seconds: float
    return_code: int | None
    output_folder: str
    details: str


def validate_report_runner(
    config: dict[str, Any],
    report_key: str,
) -> list[str]:
    """Validate one reporthout executing it."""

    report = get_report_config(config, report_key)
    errors = []

    project_folder = Path(report["project_folder"])
    runner = Path(report["runner"])
    output_folder = Path(report["output_folder"])

    if not project_folder.is_dir():
        errors.append(
            f"Project folder was not found: {project_folder}"
        )

    if not runner.is_file():
        errors.append(
            f"Report runner was not found: {runner}"
        )

    if runner.suffix.lower() not in {".bat", ".cmd", ".py"}:
        errors.append(
            f"Unsupported runner type: {runner.suffix}"
        )

    if not output_folder.is_dir():
        errors.append(
            f"Output folder was not found: {output_folder}"
        )

    return errors


def run_report(
    config: dict[str, Any],
    report_key: str,
    timeout_seconds: int | None = None,
) -> ReportResult:
    """Run one independently configured report."""

    report = get_report_config(config, report_key)
    report_name = report["display_name"]
    project_folder = Path(report["project_folder"])
    runner = Path(report["runner"])

    validation_errors = validate_report_runner(
        config,
        report_key,
    )

    if validation_errors:
        return ReportResult(
            report_key=report_key,
            report_name=report_name,
            status="FAILED",
            duration_seconds=0.0,
            return_code=None,
            output_folder=report["output_folder"],
            details=" | ".join(validation_errors),
        )

    start_time = time.perf_counter()

    try:
        if runner.suffix.lower() in {".bat", ".cmd"}:
            command = [
                "cmd.exe",
                "/d",
                "/c",
                str(runner),
            ]
        else:
            command = [
                sys.executable,
                str(runner),
            ]

        completed_process = subprocess.run(
            command,
            cwd=project_folder,
            check=False,
            timeout=timeout_seconds,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        duration = time.perf_counter() - start_time

        captured_output = completed_process.stdout.strip()

        if completed_process.returncode == 0:
            status = "SUCCESS"
            details = "Report runner completed successfully."
        else:
            status = "FAILED"

            output_lines = captured_output.splitlines()
            output_tail = "\n".join(output_lines[-15:])

            details = (
                "Report runner returned exit code "
                f"{completed_process.returncode}."
            )

            if output_tail:
                details = (
                    f"{details}\n\n"
                    f"Report output:\n{output_tail}"
                )

        return ReportResult(
            report_key=report_key,
            report_name=report_name,
            status=status,
            duration_seconds=duration,
            return_code=completed_process.returncode,
            output_folder=report["output_folder"],
            details=details,
        )

    except subprocess.TimeoutExpired:
        duration = time.perf_counter() - start_time

        return ReportResult(
            report_key=report_key,
            report_name=report_name,
            status="FAILED",
            duration_seconds=duration,
            return_code=None,
            output_folder=report["output_folder"],
            details=(
                "The report exceeded the configured time limit."
            ),
        )

    except OSError as error:
        duration = time.perf_counter() - start_time

        return ReportResult(
            report_key=report_key,
            report_name=report_name,
            status="FAILED",
            duration_seconds=duration,
            return_code=None,
            output_folder=report["output_folder"],
            details=f"Windows could not start the report: {error}",
        )


def validate_all_reports(
    config: dict[str, Any],
) -> dict[str, list[str]]:
    """Validate every configured report without running anything."""

    results = {}

    for report_key in config["run_order"]:
        results[report_key] = validate_report_runner(
            config,
            report_key,
        )

    return results


if __name__ == "__main__":
    loaded_config = load_config()
    validation_results = validate_all_reports(loaded_config)

    validation_failed = False

    print("Validating configured report runners...")
    print()

    for key in loaded_config["run_order"]:
        report_config = get_report_config(
            loaded_config,
            key,
        )
        errors = validation_results[key]

        if errors:
            validation_failed = True
            print(f"FAILED: {report_config['display_name']}")

            for error_message in errors:
                print(f"  - {error_message}")
        else:
            print(f"READY: {report_config['display_name']}")
            print(f"  Runner: {report_config['runner']}")
            print(f"  Output: {report_config['output_folder']}")

        print()

    if validation_failed:
        print("One or more report runners failed validation.")
        raise SystemExit(1)

    print("All report runners are ready.")
    print("No reports were executed during this validation.")