import tkinter as tk
from tkinter import messagebox, ttk

students_database = []
student_counter = 1000

def add_student_gui():
    global student_counter
    name = entry_name.get().strip()
    course = entry_course.get().strip()
    subjects_raw = entry_subjects.get().strip()
    
    if not name or not course:
        messagebox.showwarning("Input Error", "Please fill in both Name and Course fields.")
        return
    
    student_counter += 1
    student_id = (2026, student_counter)
    subjects = [s.strip() for s in subjects_raw.split(",") if s.strip()]
    
    student_record = {
        "Name": name,
        "Course": course,
        "Student ID": student_id,
        "Subjects": subjects
    }
    
    students_database.append(student_record)
    
    formatted_id = f"{student_id[0]}-{student_id[1]}"
    subjects_display = ", ".join(subjects) if subjects else "None"
    
    tree.insert("", tk.END, values=(formatted_id, name, course, subjects_display))
    
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_subjects.delete(0, tk.END)
    
    messagebox.showinfo("Success", f"Student added with ID: {formatted_id}")

root = tk.Tk()
root.title("Student Information Management System")
root.geometry("650x450")

frame_form = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
frame_form.pack(fill="x", padx=15, pady=10)

tk.Label(frame_form, text="Student Name:").grid(row=0, column=0, sticky="w", pady=2)
entry_name = tk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1, pady=2)

tk.Label(frame_form, text="Course:").grid(row=1, column=0, sticky="w", pady=2)
entry_course = tk.Entry(frame_form, width=40)
entry_course.grid(row=1, column=1, pady=2)

tk.Label(frame_form, text="Subjects (comma-separated):").grid(row=2, column=0, sticky="w", pady=2)
entry_subjects = tk.Entry(frame_form, width=40)
entry_subjects.grid(row=2, column=1, pady=2)

btn_add = tk.Button(frame_form, text="Add Student", command=add_student_gui, width=15)
btn_add.grid(row=3, column=1, sticky="e", pady=5)

frame_table = tk.Frame(root, padx=10, pady=5)
frame_table.pack(fill="both", expand=True, padx=15, pady=5)

columns = ("ID", "Name", "Course", "Subjects")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

tree.heading("ID", text="Student ID")
tree.heading("Name", text="Name")
tree.heading("Course", text="Course")
tree.heading("Subjects", text="Subjects")

tree.column("ID", width=90, anchor="center")
tree.column("Name", width=140)
tree.column("Course", width=140)
tree.column("Subjects", width=220)

tree.pack(fill="both", expand=True)

root.mainloop()