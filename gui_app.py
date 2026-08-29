import tkinter as tk
from tkinter import messagebox, ttk
from student_manager import StudentManager


manager = StudentManager()


def register_student_gui():
    name = entry_name.get().strip()
    program = entry_program.get().strip()
    raw_courses = entry_courses.get().strip()
    courses = [c.strip() for c in raw_courses.split(",") if c.strip()]

    if not name or not program:
        messagebox.showwarning(
            "Input Error",
            "Please fill in both Name and Program fields."
        )
        return

    try:
        record = manager.add_student(name, program, courses)
        formatted_id = manager.format_id(record["Student ID"])

        tree.insert(
            "",
            tk.END,
            values=(
                formatted_id,
                name,
                program,
                ", ".join(courses) if courses else "None"
            )
        )

        entry_name.delete(0, tk.END)
        entry_program.delete(0, tk.END)
        entry_courses.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            f"Record initialized.\nAssigned ID: {formatted_id}"
        )

    except ValueError as err:
        messagebox.showerror("Error", str(err))


root = tk.Tk()
root.title("University Academic Records System")
root.geometry("700x450")


# -----------------------------
# Student Registration
# -----------------------------

frame_form = tk.LabelFrame(
    root,
    text="Student Registration",
    padx=10,
    pady=10
)
frame_form.pack(fill="x", padx=15, pady=10)


tk.Label(
    frame_form,
    text="Name:"
).grid(row=0, column=0, sticky="w", pady=2)

entry_name = tk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1, pady=2)


tk.Label(
    frame_form,
    text="Program:"
).grid(row=1, column=0, sticky="w", pady=2)

entry_program = tk.Entry(frame_form, width=40)
entry_program.grid(row=1, column=1, pady=2)


tk.Label(
    frame_form,
    text="Courses (comma-separated):"
).grid(row=2, column=0, sticky="w", pady=2)

entry_courses = tk.Entry(frame_form, width=40)
entry_courses.grid(row=2, column=1, pady=2)


btn_register = tk.Button(
    frame_form,
    text="Register Student",
    command=register_student_gui,
    width=15
)
btn_register.grid(row=3, column=1, sticky="e", pady=5)


# -----------------------------
# Active Student Directory
# -----------------------------

frame_table = tk.LabelFrame(
    root,
    text="Active Student Directory",
    padx=10,
    pady=5
)
frame_table.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5
)


columns = ("ID", "Name", "Program", "Courses")

tree = ttk.Treeview(
    frame_table,
    columns=columns,
    show="headings",
    height=10
)


tree.heading("ID", text="ID Code")
tree.heading("Name", text="Name")
tree.heading("Program", text="Program")
tree.heading("Courses", text="Courses")


tree.column("ID", width=100, anchor="center")
tree.column("Name", width=150)
tree.column("Program", width=150)
tree.column("Courses", width=240)


tree.pack(fill="both", expand=True)


root.mainloop()