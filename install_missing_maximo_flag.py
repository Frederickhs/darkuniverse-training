from __future__ import annotations

import py_compile
import shutil
from datetime import datetime
from pathlib import Path

PROJECT = Path(r"G:\Dev\darkuniverse-training\Reports\PQS Dark Universe Report")
SUMMARY = PROJECT / "Scripts" / "employee_summary_processor.py"
RULES = PROJECT / "Documentation" / "BUSINESS_RULES.md"
BACKUP = PROJECT / "Code_Backups" / f"Missing_Maximo_{datetime.now():%Y-%m-%d_%H-%M-%S}"

if not SUMMARY.is_file():
    raise SystemExit(f"Required file not found: {SUMMARY}")

BACKUP.mkdir(parents=True, exist_ok=False)
shutil.copy2(SUMMARY, BACKUP / SUMMARY.name)
if RULES.is_file():
    shutil.copy2(RULES, BACKUP / RULES.name)

text = SUMMARY.read_text(encoding="utf-8-sig")
logic = '''    if not work_orders and any(
        result.result == "No Maximo Record" for result in module_results
    ):
        work_orders = ("Missing Maximo Data",)
'''

if 'work_orders = ("Missing Maximo Data",)' not in text:
    lines = text.splitlines(keepends=True)
    function_start = next(
        (i for i, line in enumerate(lines) if line.startswith("def summarize_venue(")),
        None,
    )
    if function_start is None:
        raise SystemExit("summarize_venue() was not found. No source file was changed.")

    function_end = next(
        (i for i in range(function_start + 1, len(lines)) if lines[i].startswith("def ")),
        len(lines),
    )
    status_index = next(
        (
            i
            for i in range(function_start, function_end)
            if 'status = "COMPLETE" if not incomplete else "INCOMPLETE"' in lines[i]
        ),
        None,
    )
    work_orders_index = next(
        (
            i
            for i in range(function_start, function_end)
            if "work_orders = unique_in_order(" in lines[i]
        ),
        None,
    )
    if work_orders_index is None or status_index is None or work_orders_index >= status_index:
        raise SystemExit(
            "The summarize_venue() anchors were not found in the expected order. "
            "No source file was changed."
        )

    lines.insert(status_index, logic)
    SUMMARY.write_text("".join(lines), encoding="utf-8", newline="")

try:
    py_compile.compile(str(SUMMARY), doraise=True)
except Exception:
    shutil.copy2(BACKUP / SUMMARY.name, SUMMARY)
    raise

verified = SUMMARY.read_text(encoding="utf-8")
if 'work_orders = ("Missing Maximo Data",)' not in verified:
    shutil.copy2(BACKUP / SUMMARY.name, SUMMARY)
    raise SystemExit("Post-install verification failed. Original file restored.")

if RULES.is_file():
    rules = RULES.read_text(encoding="utf-8-sig")
    heading = "## Missing Maximo Display"
    if heading not in rules:
        rules = rules.rstrip() + """

## Missing Maximo Display

- When a current roster employee has no applicable Maximo records for unresolved modules, the applicable venue Work Order(s) field displays `Missing Maximo Data`.
- The module status remains `No Maximo Record`.
- The employee remains in the population sheet, dashboard totals, and employee action list.
"""
        RULES.write_text(rules + "\n", encoding="utf-8")

print("PQS MISSING MAXIMO FLAG INSTALLED.")
print("- Module result: No Maximo Record")
print("- Venue Work Order(s): Missing Maximo Data")
print("- Dashboard action category: No Maximo Record")
print(f"Backup: {BACKUP}")
print("Run the PQS Dark Universe Report and verify a known missing-Maximo SSO.")
