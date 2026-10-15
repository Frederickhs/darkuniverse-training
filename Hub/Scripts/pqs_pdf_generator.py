from __future__ import annotations

import os
import re
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    from PyPDF2 import PdfReader, PdfWriter

IS_FROZEN = getattr(sys, "frozen", False)
RUNTIME_FOLDER = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
HUB_FOLDER = Path(sys.executable).resolve().parent if IS_FROZEN else Path(__file__).resolve().parent.parent
TEMPLATE_FOLDER = RUNTIME_FOLDER / "PDF Templates"
OUTPUT_FOLDER = HUB_FOLDER / "PDF Output"

FULL_TEMPLATE = TEMPLATE_FOLDER / "Full PQS Venue Blue Sheet to Fill.pdf"
PARTIAL_TEMPLATE = TEMPLATE_FOLDER / "Partial Modules Blue Sheet to Fill.pdf"

FORM_FULL = "Full PQS Venue"
FORM_PARTIAL = "Partial Module"

DEFAULT_TRAINER_NAME = "Frederick Herrera"
DEFAULT_TRAINER_SSO = "703153842"


def clean_text(value: str) -> str:
    return " ".join(str(value or "").strip().split())


def combined_name_id(name: str, sso: str) -> str:
    name = clean_text(name)
    sso = clean_text(sso)
    if name and sso:
        return f"{name} / {sso}"
    return name or sso


def safe_filename(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]+', " ", clean_text(value))
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value or "PQS Form"


def fill_pdf(template: Path, output: Path, fields: dict[str, str]) -> None:
    reader = PdfReader(str(template))
    writer = PdfWriter()
    writer.append(reader)

    for page in writer.pages:
        writer.update_page_form_field_values(
            page,
            fields,
            auto_regenerate=False,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as file:
        writer.write(file)


def open_file(path: Path) -> None:
    if os.name != "nt":
        raise RuntimeError("Preview is configured for Windows.")
    os.startfile(str(path))


class PQSPDFGenerator(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("PQS PDF Generator")
        self.geometry("720x690")
        self.minsize(680, 650)
        self.configure(bg="#F4F6F8")

        self.form_type = tk.StringVar(value=FORM_FULL)
        self.technician_name = tk.StringVar()
        self.technician_sso = tk.StringVar()
        self.venue = tk.StringVar()
        self.module = tk.StringVar()
        self.work_order = tk.StringVar()
        self.trainer_name = tk.StringVar(value=DEFAULT_TRAINER_NAME)
        self.trainer_sso = tk.StringVar(value=DEFAULT_TRAINER_SSO)
        self.supervisor = tk.StringVar()
        self.manager = tk.StringVar()
        self.date_time = tk.StringVar()
        self.status = tk.StringVar(value="Ready")
        self.last_output: Path | None = None

        self.build()
        self.form_type.trace_add("write", self.on_form_change)
        self.on_form_change()
        self.after_idle(self.center_window)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() - width) // 2
        y = 20
        self.geometry(f"{width}x{height}{x:+d}{y:+d}")

    def build(self):
        hero = tk.Frame(self, bg="#17365D", padx=24, pady=18)
        hero.pack(fill="x")
        tk.Label(
            hero,
            text="PQS PDF GENERATOR",
            font=("Segoe UI", 20, "bold"),
            bg="#17365D",
            fg="white",
        ).pack(anchor="w")
        tk.Label(
            hero,
            text="Create Full PQS Venue and Partial Module blue sheets",
            font=("Segoe UI", 10),
            bg="#17365D",
            fg="#D9EAF7",
        ).pack(anchor="w")

        body = tk.Frame(self, bg="#F4F6F8", padx=22, pady=18)
        body.pack(fill="both", expand=True)
        body.columnconfigure(1, weight=1)

        row = 0
        self.add_label(body, "Form Type", row)
        form_box = ttk.Combobox(
            body,
            textvariable=self.form_type,
            values=(FORM_FULL, FORM_PARTIAL),
            state="readonly",
        )
        form_box.grid(row=row, column=1, sticky="ew", pady=5)

        row += 1
        self.add_label(body, "Technician Name", row)
        ttk.Entry(body, textvariable=self.technician_name).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Technician SSO", row)
        ttk.Entry(body, textvariable=self.technician_sso).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Venue", row)
        ttk.Entry(body, textvariable=self.venue).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Module", row)
        self.module_entry = ttk.Entry(body, textvariable=self.module)
        self.module_entry.grid(row=row, column=1, sticky="ew", pady=5)

        row += 1
        self.add_label(body, "Work Order", row)
        ttk.Entry(body, textvariable=self.work_order).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        ttk.Separator(body).grid(row=row, column=0, columnspan=2, sticky="ew", pady=12)

        row += 1
        self.add_label(body, "RCM Trainer Name", row)
        ttk.Entry(body, textvariable=self.trainer_name).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "RCM Trainer SSO", row)
        ttk.Entry(body, textvariable=self.trainer_sso).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Supervisor Name / ID", row)
        ttk.Entry(body, textvariable=self.supervisor).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Manager Name / ID", row)
        ttk.Entry(body, textvariable=self.manager).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        self.add_label(body, "Date / Time", row)
        ttk.Entry(body, textvariable=self.date_time).grid(
            row=row, column=1, sticky="ew", pady=5
        )

        row += 1
        actions = tk.Frame(body, bg="#F4F6F8")
        actions.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(18, 8))
        actions.columnconfigure((0, 1), weight=1)
        ttk.Button(actions, text="Generate PDF", command=self.generate).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )
        ttk.Button(actions, text="Preview Last PDF", command=self.preview_last).grid(
            row=0, column=1, sticky="ew", padx=(6, 0)
        )

        row += 1
        tk.Label(
            body,
            textvariable=self.status,
            anchor="w",
            padx=10,
            pady=8,
            bg="#E7E6E6",
            fg="#404040",
        ).grid(row=row, column=0, columnspan=2, sticky="ew", pady=(6, 0))

    @staticmethod
    def add_label(parent, text, row):
        tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg="#F4F6F8",
            fg="#1F1F1F",
        ).grid(row=row, column=0, sticky="w", padx=(0, 16), pady=5)

    def on_form_change(self, *_):
        if self.form_type.get() == FORM_PARTIAL:
            self.module_entry.configure(state="normal")
        else:
            self.module.set("")
            self.module_entry.configure(state="disabled")

    def validate(self) -> bool:
        missing = []
        if not clean_text(self.technician_name.get()):
            missing.append("Technician Name")
        if not clean_text(self.technician_sso.get()):
            missing.append("Technician SSO")
        if not clean_text(self.venue.get()):
            missing.append("Venue")
        if not clean_text(self.work_order.get()):
            missing.append("Work Order")
        if self.form_type.get() == FORM_PARTIAL and not clean_text(self.module.get()):
            missing.append("Module")

        template = FULL_TEMPLATE if self.form_type.get() == FORM_FULL else PARTIAL_TEMPLATE
        if not template.exists():
            messagebox.showerror("PQS PDF Generator", f"Template not found:\n{template}")
            return False

        if missing:
            messagebox.showwarning(
                "PQS PDF Generator",
                "Complete these required fields:\n\n" + "\n".join(missing),
            )
            return False
        return True

    def build_fields(self) -> tuple[Path, dict[str, str], str]:
        technician = combined_name_id(
            self.technician_name.get(), self.technician_sso.get()
        )
        trainer = combined_name_id(self.trainer_name.get(), self.trainer_sso.get())
        venue = clean_text(self.venue.get())
        module = clean_text(self.module.get())
        work_order = clean_text(self.work_order.get())
        supervisor = clean_text(self.supervisor.get())
        manager = clean_text(self.manager.get())
        date_time = clean_text(self.date_time.get())

        if self.form_type.get() == FORM_FULL:
            fields = {
                "WO": work_order,
                "Print RCM Technical Trainer NameTeam Member ID": trainer,
                "Print Technician NameTeam Member ID": technician,
                "Print Venue Name": venue,
                "Date/Time": date_time,
                "Supervisor Name / ID": supervisor,
                "Manager Name/ ID": manager,
            }
            suffix = "Full PQS Venue"
            return FULL_TEMPLATE, fields, suffix

        venue_module = f"{venue} / {module}" if module else venue
        fields = {
            "WO": work_order,
            "Tech Name": technician,
            "RCM Trainer": trainer,
            "Venue Name": venue_module,
            "Date/Time": date_time,
            "Supervisor Name / ID": supervisor,
            "Manager Name / ID": manager,
        }
        suffix = f"Partial PQS {module}" if module else "Partial PQS Module"
        return PARTIAL_TEMPLATE, fields, suffix

    def generate(self):
        if not self.validate():
            return

        try:
            template, fields, suffix = self.build_fields()
            filename = safe_filename(
                f"{self.technician_name.get()} {self.technician_sso.get()} {suffix}"
            ) + ".pdf"
            output = OUTPUT_FOLDER / filename
            fill_pdf(template, output, fields)
            self.last_output = output
            self.status.set(f"Generated: {output.name}")
            messagebox.showinfo(
                "PQS PDF Generator",
                f"PDF generated successfully:\n\n{output}",
            )
        except Exception as error:
            self.status.set("Generation failed")
            messagebox.showerror("PQS PDF Generator", str(error))

    def preview_last(self):
        if not self.last_output or not self.last_output.exists():
            messagebox.showwarning(
                "PQS PDF Generator",
                "Generate a PDF before using Preview Last PDF.",
            )
            return
        try:
            open_file(self.last_output)
        except Exception as error:
            messagebox.showerror("PQS PDF Generator", str(error))


def launch_pqs_pdf_generator(parent=None):
    window = PQSPDFGenerator(parent)
    if parent is not None and parent.state() != "withdrawn":
        window.transient(parent)
    window.deiconify()
    window.lift()
    window.focus_force()
    return window


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    window = launch_pqs_pdf_generator(root)
    root.mainloop()
