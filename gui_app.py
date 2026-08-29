def run_gui_app(manager):
    import tkinter as tk
    from tkinter import messagebox, ttk
    from student_manager import StudentManager


    manager = StudentManager()


    BG_COLOR = "#F4F6F9"
    CARD_COLOR = "#FFFFFF"
    PRIMARY_COLOR = "#1E3A5F"
    SECONDARY_COLOR = "#2E5D8C"
    ACCENT_COLOR = "#3B82F6"
    TEXT_COLOR = "#1F2937"
    MUTED_TEXT = "#6B7280"
    BORDER_COLOR = "#D1D5DB"
    SUCCESS_COLOR = "#15803D"
    DANGER_COLOR = "#DC2626"
    WARNING_COLOR = "#D97706"


    def refresh_table():
        for item in tree.get_children():
            tree.delete(item)

        for sid, record in manager.get_all_students().items():
            formatted_id = manager.format_id(sid)
            courses = record.get("Subjects", [])

            tree.insert(
                "",
                tk.END,
                values=(
                    formatted_id,
                    record["Name"],
                    record["Course"],
                    len(courses),
                    ", ".join(courses) if courses else "None",
                    record.get("Status", "Active")
                )
            )


    def clear_fields():
        entry_name.delete(0, tk.END)
        entry_program.delete(0, tk.END)
        entry_courses.delete(0, tk.END)

        entry_name.focus()

        status_label.config(
            text="Ready for student registration."
        )


    def register_student_gui():
        name = entry_name.get().strip()
        program = entry_program.get().strip()
        raw_courses = entry_courses.get().strip()

        courses = [
            c.strip()
            for c in raw_courses.split(",")
            if c.strip()
        ]

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

            refresh_table()
            clear_fields()

            status_label.config(
                text=f"✓ Student registered successfully — ID: {formatted_id}"
            )

            messagebox.showinfo(
                "Registration Successful",
                f"Record initialized successfully.\n\n"
                f"Student ID: {formatted_id}\n"
                f"Name: {record['Name']}\n"
                f"Program: {record['Course']}"
            )

        except ValueError as err:
            messagebox.showerror(
                "Registration Error",
                str(err)
            )


    def get_selected_student():
        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Student Selected",
                "Please select a student from the directory first."
            )
            return None

        return tree.item(selected[0], "values")


    def edit_student_gui():
        values = get_selected_student()

        if not values:
            return

        student_id = values[0]

        sid, record = manager.find_record(student_id)

        if not record:
            messagebox.showerror(
                "Error",
                "Student record could not be found."
            )
            return

        entry_name.delete(0, tk.END)
        entry_name.insert(0, record["Name"])

        entry_program.delete(0, tk.END)
        entry_program.insert(0, record["Course"])

        entry_courses.delete(0, tk.END)
        entry_courses.insert(
            0,
            ", ".join(record["Subjects"])
        )

        status_label.config(
            text=f"Editing student {student_id} — modify the fields and click UPDATE STUDENT."
        )

        register_button.config(
            text="UPDATE STUDENT",
            command=lambda: update_student_gui(student_id)
        )

        cancel_edit_button.pack(
            pady=(8, 0)
        )


    def update_student_gui(student_id):
        name = entry_name.get().strip()
        program = entry_program.get().strip()
        raw_courses = entry_courses.get().strip()

        courses = [
            c.strip()
            for c in raw_courses.split(",")
            if c.strip()
        ]

        if not name or not program:
            messagebox.showwarning(
                "Incomplete Information",
                "Please enter both the student's Name and Program."
            )
            return

        try:
            manager.update_student(
                student_id,
                name,
                program,
                courses
            )

            refresh_table()
            cancel_edit()

            status_label.config(
                text=f"✓ Student {student_id} updated successfully."
            )

            messagebox.showinfo(
                "Update Successful",
                "Student record updated successfully."
            )

        except ValueError as err:
            messagebox.showerror(
                "Update Error",
                str(err)
            )


    def cancel_edit():
        clear_fields()

        register_button.config(
            text="REGISTER STUDENT",
            command=register_student_gui
        )

        cancel_edit_button.pack_forget()

        status_label.config(
            text="Ready for student registration."
        )


    def drop_course_gui():
        values = get_selected_student()

        if not values:
            return

        student_id = values[0]

        sid, record = manager.find_record(student_id)

        if not record:
            return

        if not record["Subjects"]:
            messagebox.showinfo(
                "No Courses",
                "This student currently has no enrolled courses."
            )
            return

        dialog = tk.Toplevel(root)

        dialog.title("Drop Course")
        dialog.geometry("400x250")
        dialog.configure(bg=CARD_COLOR)
        dialog.resizable(False, False)

        tk.Label(
            dialog,
            text="Drop Course(s)",
            font=("Segoe UI", 15, "bold"),
            bg=CARD_COLOR,
            fg=PRIMARY_COLOR
        ).pack(pady=(20, 5))

        tk.Label(
            dialog,
            text=f"{record['Name']} ({student_id})",
            font=("Segoe UI", 9),
            bg=CARD_COLOR,
            fg=MUTED_TEXT
        ).pack()

        tk.Label(
            dialog,
            text="Enter course(s) to drop:",
            font=("Segoe UI", 9, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=(20, 5))

        course_entry = tk.Entry(
            dialog,
            font=("Segoe UI", 10),
            width=35
        )
        course_entry.pack()

        tk.Label(
            dialog,
            text="Example: CPE106L-4, MATH165",
            font=("Segoe UI", 8),
            bg=CARD_COLOR,
            fg=MUTED_TEXT
        ).pack(pady=5)

        def confirm_drop_course():
            raw_courses = course_entry.get().strip()

            if not raw_courses:
                messagebox.showwarning(
                    "No Course",
                    "Please enter at least one course.",
                    parent=dialog
                )
                return

            courses = [
                c.strip()
                for c in raw_courses.split(",")
                if c.strip()
            ]

            try:
                updated, count = manager.remove_courses_from_student(
                    student_id,
                    courses
                )

                refresh_table()

                if count == 0:
                    messagebox.showinfo(
                        "No Changes",
                        "None of the specified courses were currently enrolled.",
                        parent=dialog
                    )
                else:
                    messagebox.showinfo(
                        "Course Dropped",
                        f"{count} course(s) dropped successfully.",
                        parent=dialog
                    )

                dialog.destroy()

                status_label.config(
                    text=f"✓ Course record updated for {student_id}."
                )

            except ValueError as err:
                messagebox.showerror(
                    "Error",
                    str(err),
                    parent=dialog
                )

        tk.Button(
            dialog,
            text="DROP COURSE",
            command=confirm_drop_course,
            font=("Segoe UI", 9, "bold"),
            bg=WARNING_COLOR,
            fg="white",
            activebackground="#B45309",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            height=2
        ).pack(pady=15)

        course_entry.focus()


    def drop_student_gui():
        values = get_selected_student()

        if not values:
            return

        student_id = values[0]

        sid, record = manager.find_record(student_id)

        if not record:
            return

        if record.get("Status", "Active") == "Dropped":
            messagebox.showinfo(
                "Already Dropped",
                "This student is already marked as dropped."
            )
            return

        confirm = messagebox.askyesno(
            "Drop Student",
            f"Are you sure you want to mark:\n\n"
            f"{record['Name']}\n"
            f"{student_id}\n\n"
            f"as DROPPED from the university?\n\n"
            f"The student's record will be retained."
        )

        if not confirm:
            return

        try:
            manager.drop_student(student_id)

            refresh_table()

            status_label.config(
                text=f"Student {student_id} has been marked as DROPPED."
            )

            messagebox.showinfo(
                "Student Dropped",
                f"{record['Name']} has been marked as dropped.\n\n"
                f"The academic record has been retained."
            )

        except ValueError as err:
            messagebox.showerror(
                "Error",
                str(err)
            )


    def restore_student_gui():
        values = get_selected_student()

        if not values:
            return

        student_id = values[0]

        sid, record = manager.find_record(student_id)

        if not record:
            return

        if record.get("Status", "Active") == "Active":
            messagebox.showinfo(
                "Already Active",
                "This student is already marked as active."
            )
            return

        confirm = messagebox.askyesno(
            "Restore Student",
            f"Restore {record['Name']} as an active student?"
        )

        if not confirm:
            return

        try:
            manager.restore_student(student_id)

            refresh_table()

            status_label.config(
                text=f"✓ Student {student_id} has been restored."
            )

            messagebox.showinfo(
                "Student Restored",
                f"{record['Name']} is now marked as Active."
            )

        except ValueError as err:
            messagebox.showerror(
                "Error",
                str(err)
            )


    def delete_student_gui():
        values = get_selected_student()

        if not values:
            return

        student_id = values[0]

        sid, record = manager.find_record(student_id)

        if not record:
            return

        confirm = messagebox.askyesno(
            "Permanently Delete Student",
            f"WARNING\n\n"
            f"Are you sure you want to permanently delete:\n\n"
            f"{record['Name']}\n"
            f"{student_id}\n\n"
            f"This action cannot be undone."
        )

        if not confirm:
            return

        try:
            manager.delete_student(student_id)

            refresh_table()

            status_label.config(
                text=f"Student {student_id} permanently deleted."
            )

            messagebox.showinfo(
                "Student Deleted",
                "The student record has been permanently deleted."
            )

        except ValueError as err:
            messagebox.showerror(
                "Error",
                str(err)
            )


    root = tk.Tk()

    root.title("University Academic Records System")
    root.geometry("1050x720")
    root.minsize(900, 650)

    # Start maximized while keeping normal window borders
    root.state("zoomed")

    root.configure(bg=BG_COLOR)


    style = ttk.Style()

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass


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


    style.configure(
        "Vertical.TScrollbar",
        background="#CBD5E1",
        troughcolor=BG_COLOR,
        bordercolor=BG_COLOR,
        arrowcolor=PRIMARY_COLOR
    )


    header = tk.Frame(
        root,
        bg=PRIMARY_COLOR,
        height=100
    )

    header.pack(fill="x")


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

    subtitle_label.pack(anchor="w")


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

    registration_title.pack(anchor="w")


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


    form = tk.Frame(
        registration_card,
        bg=CARD_COLOR
    )

    form.pack(
        fill="x",
        padx=25,
        pady=(0, 20)
    )


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
    ).pack(anchor="w")


    tk.Label(
        name_label_frame,
        text="Ex. Juan Dela Cruz",
        font=("Segoe UI", 8),
        bg=CARD_COLOR,
        fg=MUTED_TEXT
    ).pack(anchor="w")


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
    ).pack(anchor="w")


    tk.Label(
        program_label_frame,
        text="Ex. BS Computer Engineering",
        font=("Segoe UI", 8),
        bg=CARD_COLOR,
        fg=MUTED_TEXT
    ).pack(anchor="w")


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
    ).pack(anchor="w")


    tk.Label(
        courses_label_frame,
        text="Ex. MATH165, CPE106L-4",
        font=("Segoe UI", 8),
        bg=CARD_COLOR,
        fg=MUTED_TEXT
    ).pack(anchor="w")


    tk.Label(
        courses_label_frame,
        text="Separate multiple courses with commas",
        font=("Segoe UI", 8),
        bg=CARD_COLOR,
        fg=MUTED_TEXT
    ).pack(anchor="w")


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


    cancel_edit_button = tk.Button(
        button_frame,
        text="CANCEL EDIT",
        command=cancel_edit,
        font=("Segoe UI", 9),
        bg="#FEE2E2",
        fg=DANGER_COLOR,
        activebackground="#FECACA",
        relief="flat",
        cursor="hand2",
        width=18,
        height=2
    )


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

    directory_title.pack(side="left")


    directory_description = tk.Label(
        directory_header,
        text="Registered student records",
        font=("Segoe UI", 9),
        bg=CARD_COLOR,
        fg=MUTED_TEXT
    )

    directory_description.pack(side="right")


    table_frame = tk.Frame(
        directory_card,
        bg=CARD_COLOR
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(0, 10)
    )


    columns = (
        "ID",
        "Name",
        "Program",
        "Course Count",
        "Courses",
        "Status"
    )


    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


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

    tree.heading(
        "Status",
        text="Status"
    )


    tree.column(
        "ID",
        width=100,
        anchor="center"
    )

    tree.column(
        "Name",
        width=170
    )

    tree.column(
        "Program",
        width=180
    )

    tree.column(
        "Course Count",
        width=80,
        anchor="center"
    )

    tree.column(
        "Courses",
        width=280
    )

    tree.column(
        "Status",
        width=90,
        anchor="center"
    )


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


    actions_frame = tk.Frame(
        directory_card,
        bg=CARD_COLOR
    )

    actions_frame.pack(
        fill="x",
        padx=25,
        pady=(0, 18)
    )


    edit_button = tk.Button(
        actions_frame,
        text="EDIT STUDENT",
        command=edit_student_gui,
        font=("Segoe UI", 9, "bold"),
        bg=ACCENT_COLOR,
        fg="white",
        activebackground=SECONDARY_COLOR,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=16,
        height=2
    )

    edit_button.pack(
        side="left",
        padx=(0, 8)
    )


    drop_course_button = tk.Button(
        actions_frame,
        text="DROP COURSE",
        command=drop_course_gui,
        font=("Segoe UI", 9, "bold"),
        bg=WARNING_COLOR,
        fg="white",
        activebackground="#B45309",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=16,
        height=2
    )

    drop_course_button.pack(
        side="left",
        padx=8
    )


    drop_student_button = tk.Button(
        actions_frame,
        text="DROP STUDENT",
        command=drop_student_gui,
        font=("Segoe UI", 9, "bold"),
        bg="#F97316",
        fg="white",
        activebackground="#C2410C",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=16,
        height=2
    )

    drop_student_button.pack(
        side="left",
        padx=8
    )


    restore_button = tk.Button(
        actions_frame,
        text="RESTORE STUDENT",
        command=restore_student_gui,
        font=("Segoe UI", 9, "bold"),
        bg=SUCCESS_COLOR,
        fg="white",
        activebackground="#166534",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=16,
        height=2
    )

    restore_button.pack(
        side="left",
        padx=8
    )


    delete_button = tk.Button(
        actions_frame,
        text="DELETE RECORD",
        command=delete_student_gui,
        font=("Segoe UI", 9, "bold"),
        bg=DANGER_COLOR,
        fg="white",
        activebackground="#B91C1C",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=16,
        height=2
    )

    delete_button.pack(
        side="left",
        padx=8
    )


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


    refresh_table()

    entry_name.focus()

    root.mainloop()