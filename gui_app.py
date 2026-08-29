import tkinter as tk
from tkinter import messagebox, ttk
from student_manager import StudentManager


# Student Manager
manager = StudentManager()


# Colors
BG_COLOR = "#F4F6F9"
CARD_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#1E3A5F"
SECONDARY_COLOR = "#2E5D8C"
ACCENT_COLOR = "#3B82F6"
TEXT_COLOR = "#1F2937"
MUTED_TEXT = "#6B7280"
BORDER_COLOR = "#D1D5DB"
SUCCESS_COLOR = "#15803D"


# Functions
def register_student_gui():
    name = entry_name.get().strip()
    program = entry_program.get().strip()
    raw_courses = entry_courses.get().strip()

    courses = [
        c.strip()
        for c in raw_courses.split(",")
        if c.strip()
    ]

    # Validation
    if not name or not program:
        messagebox.showwarning(
            "Incomplete Information",
            "Please enter both the student's Name and Program."
        )
        return

    try:
        record = manager.add_student(
            name,
            program,
            courses
        )

        formatted_id = manager.format_id(
            record["Student ID"]
        )

        # Insert into directory
        tree.insert(
            "",
            tk.END,
            values=(
                formatted_id,
                name,
                program,
                len(courses),
                ", ".join(courses) if courses else "None"
            )
        )

        # Clear input fields
        entry_name.delete(0, tk.END)
        entry_program.delete(0, tk.END)
        entry_courses.delete(0, tk.END)

        # Update status
        status_label.config(
            text=f"✓ Student registered successfully — ID: {formatted_id}"
        )

        messagebox.showinfo(
            "Registration Successful",
            f"Record initialized successfully.\n\n"
            f"Student ID: {formatted_id}\n"
            f"Name: {name}\n"
            f"Program: {program}"
        )

    except ValueError as err:
        messagebox.showerror(
            "Registration Error",
            str(err)
        )


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_program.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    entry_name.focus()

    status_label.config(
        text="Ready for student registration."
    )


# Main Window
root = tk.Tk()

root.title("University Academic Records System")
root.geometry("900x650")
root.minsize(800, 600)
root.configure(bg=BG_COLOR)


# Style
style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass


# Treeview
style.configure(
    "Treeview",
    background=CARD_COLOR,
    foreground=TEXT_COLOR,
    rowheight=36,
    fieldbackground=CARD_COLOR,
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    background=PRIMARY_COLOR,
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[
        ("selected", "#DCEBFA")
    ],
    foreground=[
        ("selected", TEXT_COLOR)
    ]
)


# Scrollbar
style.configure(
    "Vertical.TScrollbar",
    background="#CBD5E1",
    troughcolor=BG_COLOR,
    bordercolor=BG_COLOR,
    arrowcolor=PRIMARY_COLOR
)


# Header
header = tk.Frame(
    root,
    bg=PRIMARY_COLOR,
    height=100
)
header.pack(
    fill="x"
)

header_content = tk.Frame(
    header,
    bg=PRIMARY_COLOR
)
header_content.pack(
    fill="both",
    expand=True,
    padx=30
)


title_label = tk.Label(
    header_content,
    text="UNIVERSITY ACADEMIC RECORDS SYSTEM",
    font=("Segoe UI", 20, "bold"),
    bg=PRIMARY_COLOR,
    fg="white"
)
title_label.pack(
    anchor="w",
    pady=(20, 2)
)


subtitle_label = tk.Label(
    header_content,
    text="Student Registration & Academic Directory",
    font=("Segoe UI", 10),
    bg=PRIMARY_COLOR,
    fg="#D9E6F2"
)
subtitle_label.pack(
    anchor="w"
)


# Content Area
content = tk.Frame(
    root,
    bg=BG_COLOR
)
content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=20
)


# Registration Card
registration_card = tk.Frame(
    content,
    bg=CARD_COLOR,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)
registration_card.pack(
    fill="x",
    pady=(0, 20)
)


# Card Header
card_header = tk.Frame(
    registration_card,
    bg=CARD_COLOR
)
card_header.pack(
    fill="x",
    padx=25,
    pady=(20, 5)
)


registration_title = tk.Label(
    card_header,
    text="Student Registration",
    font=("Segoe UI", 15, "bold"),
    bg=CARD_COLOR,
    fg=PRIMARY_COLOR
)
registration_title.pack(
    anchor="w"
)


registration_subtitle = tk.Label(
    card_header,
    text="Enter the student's academic information below.",
    font=("Segoe UI", 9),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
)
registration_subtitle.pack(
    anchor="w",
    pady=(2, 10)
)


# Form
form = tk.Frame(
    registration_card,
    bg=CARD_COLOR
)
form.pack(
    fill="x",
    padx=25,
    pady=(0, 20)
)


# Name
name_label_frame = tk.Frame(
    form,
    bg=CARD_COLOR
)
name_label_frame.grid(
    row=0,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=5
)

tk.Label(
    name_label_frame,
    text="Student Name",
    font=("Segoe UI", 9, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(
    anchor="w"
)

tk.Label(
    name_label_frame,
    text="Ex. DELA CRUZ, JUAN C.",
    font=("Segoe UI", 8),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
).pack(
    anchor="w"
)


entry_name = tk.Entry(
    form,
    font=("Segoe UI", 10),
    relief="solid",
    bd=1,
    width=35
)
entry_name.grid(
    row=0,
    column=1,
    sticky="ew",
    pady=5
)


# Program
program_label_frame = tk.Frame(
    form,
    bg=CARD_COLOR
)
program_label_frame.grid(
    row=1,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=5
)

tk.Label(
    program_label_frame,
    text="Program",
    font=("Segoe UI", 9, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(
    anchor="w"
)

tk.Label(
    program_label_frame,
    text="Ex. BS Computer Engineering",
    font=("Segoe UI", 8),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
).pack(
    anchor="w"
)


entry_program = tk.Entry(
    form,
    font=("Segoe UI", 10),
    relief="solid",
    bd=1,
    width=35
)
entry_program.grid(
    row=1,
    column=1,
    sticky="ew",
    pady=5
)


# Courses
courses_label_frame = tk.Frame(
    form,
    bg=CARD_COLOR
)
courses_label_frame.grid(
    row=2,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=5
)

tk.Label(
    courses_label_frame,
    text="Courses",
    font=("Segoe UI", 9, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(
    anchor="w"
)

tk.Label(
    courses_label_frame,
    text="Ex. MATH165, CPE106L-4",
    font=("Segoe UI", 8),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
).pack(
    anchor="w"
)

tk.Label(
    courses_label_frame,
    text="Separate multiple courses with commas",
    font=("Segoe UI", 8),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
).pack(
    anchor="w"
)


entry_courses = tk.Entry(
    form,
    font=("Segoe UI", 10),
    relief="solid",
    bd=1,
    width=35
)
entry_courses.grid(
    row=2,
    column=1,
    sticky="ew",
    pady=5
)


form.columnconfigure(
    1,
    weight=1
)


# Buttons
button_frame = tk.Frame(
    form,
    bg=CARD_COLOR
)
button_frame.grid(
    row=0,
    column=2,
    rowspan=3,
    padx=(25, 0)
)


register_button = tk.Button(
    button_frame,
    text="REGISTER STUDENT",
    command=register_student_gui,
    font=("Segoe UI", 9, "bold"),
    bg=ACCENT_COLOR,
    fg="white",
    activebackground=SECONDARY_COLOR,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=18,
    height=2
)
register_button.pack(
    pady=(5, 8)
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR FIELDS",
    command=clear_fields,
    font=("Segoe UI", 9),
    bg="#E5E7EB",
    fg=TEXT_COLOR,
    activebackground="#D1D5DB",
    relief="flat",
    cursor="hand2",
    width=18,
    height=2
)
clear_button.pack()


# Directory Card
directory_card = tk.Frame(
    content,
    bg=CARD_COLOR,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)
directory_card.pack(
    fill="both",
    expand=True
)


# Directory Header
directory_header = tk.Frame(
    directory_card,
    bg=CARD_COLOR
)
directory_header.pack(
    fill="x",
    padx=25,
    pady=(18, 10)
)


directory_title = tk.Label(
    directory_header,
    text="Active Student Directory",
    font=("Segoe UI", 15, "bold"),
    bg=CARD_COLOR,
    fg=PRIMARY_COLOR
)
directory_title.pack(
    side="left"
)


directory_description = tk.Label(
    directory_header,
    text="Registered student records",
    font=("Segoe UI", 9),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
)
directory_description.pack(
    side="right"
)


# Table
table_frame = tk.Frame(
    directory_card,
    bg=CARD_COLOR
)
table_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=(0, 20)
)


columns = (
    "ID",
    "Name",
    "Program",
    "Course Count",
    "Courses"
)


tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)


# Headings
tree.heading(
    "ID",
    text="ID Code"
)

tree.heading(
    "Name",
    text="Name"
)

tree.heading(
    "Program",
    text="Program"
)

tree.heading(
    "Course Count",
    text="Courses"
)

tree.heading(
    "Courses",
    text="Enrolled Courses"
)


# Columns
tree.column(
    "ID",
    width=100,
    anchor="center"
)

tree.column(
    "Name",
    width=180
)

tree.column(
    "Program",
    width=180
)

tree.column(
    "Course Count",
    width=90,
    anchor="center"
)

tree.column(
    "Courses",
    width=280
)


# Scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=scrollbar.set
)


tree.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Status Bar
status_bar = tk.Frame(
    root,
    bg="#E5E7EB",
    height=30
)
status_bar.pack(
    fill="x",
    side="bottom"
)


status_label = tk.Label(
    status_bar,
    text="Ready for student registration.",
    font=("Segoe UI", 8),
    bg="#E5E7EB",
    fg=MUTED_TEXT
)
status_label.pack(
    side="left",
    padx=20,
    pady=6
)


# Start Application
entry_name.focus()

root.mainloop()