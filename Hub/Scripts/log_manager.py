import logging
import sys
from datetime import datetime
from pathlib import Path


HUB_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOG_FOLDER = HUB_ROOT / "Logs"


def configure_logging(
    log_folder: str | Path = DEFAULT_LOG_FOLDER,
) -> tuple[logging.Logger, Path]:
    """Configure file and console logging for the Reporting Hub."""

    folder = Path(log_folder)

    if not folder.is_absolute():
        folder = HUB_ROOT / folder

    folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = folder / f"reporting_hub_{timestamp}.log"

    logger = logging.getLogger("dark_universe_reporting_hub")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    logger.handlers.clear()

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Dark Universe Reporting Hub logging started.")

    return logger, log_file


def log_report_start(
    logger: logging.Logger,
    report_name: str,
) -> None:
    """Record the start of an individual report."""

    logger.info("REPORT STARTED | %s", report_name)


def log_report_result(
    logger: logging.Logger,
    report_name: str,
    status: str,
    duration_seconds: float,
    details: str = "",
) -> None:
    """Record the final result of an individual report."""

    message = (
        f"REPORT FINISHED | {report_name} | "
        f"Status: {status} | "
        f"Duration: {duration_seconds:.1f} seconds"
    )

    if details:
        message = f"{message} | Details: {details}"

    if status.upper() == "FAILED":
        logger.error(message)
    elif status.upper() == "WARNING":
        logger.warning(message)
    else:
        logger.info(message)


def log_folder_opened(
    logger: logging.Logger,
    button_name: str,
    folder_path: str | Path,
) -> None:
    """Record when a folder shortcut is used."""

    logger.info(
        "FOLDER OPENED | %s | %s",
        button_name,
        folder_path,
    )


def log_error(
    logger: logging.Logger,
    message: str,
) -> None:
    """Record a Hub error."""

    logger.error(message)


if __name__ == "__main__":
    test_logger, test_log_file = configure_logging()

    test_logger.info("Logging validation message.")
    test_logger.warning("Warning validation message.")
    test_logger.error("Error validation message.")

    print()
    print("Logging configured successfully.")
    print(f"Log file: {test_log_file}")