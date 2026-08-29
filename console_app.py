from student_manager import StudentManager

def run_console_app(manager: StudentManager):
    def register_ui():
        print("\n" + "=" * 40)
        print("      STUDENT REGISTRATION MODULE")
        print("=" * 40)
        
        name = input("Enter Name: ").strip()
        program = input("Enter Program: ").strip()
        raw_courses = input("Enter Courses (comma-separated): ")
        courses = [c.strip() for c in raw_courses.split(",") if c.strip()]
        
        try:
            record = manager.add_student(name, program, courses)
            formatted_id = manager.format_id(record["Student ID"])
            print(f"\n[SUCCESS] Record initialized. Assigned ID: {formatted_id}")
        except ValueError as err:
            print(f"\n[ERROR] {err}")

    def manage_courses_ui():
        print("\n" + "=" * 40)
        print("      MANAGE ENROLLED COURSES")
        print("=" * 40)
        
        identifier = input("Enter Student ID or Name: ").strip()
        sid, record = manager.find_record(identifier)
        
        if not record:
            print(f"\n[ERROR] No record found matching: '{identifier}'.")
            return
            
        print(f"\nStudent Found : {record['Name']} ({manager.format_id(record['Student ID'])})")
        print(f"Current Enrolled: {', '.join(record['Subjects']) if record['Subjects'] else 'None'}")
        
        raw_courses = input("\nEnter Updated Courses (comma-separated): ")
        new_courses = [c.strip() for c in raw_courses.split(",") if c.strip()]
        
        try:
            updated = manager.update_student_courses(identifier, new_courses)
            print(f"\n[SUCCESS] Courses successfully updated for {updated['Name']}.")
            print(f"Updated Enrolled: {', '.join(updated['Subjects']) if updated['Subjects'] else 'None'}")
        except ValueError as err:
            print(f"\n[ERROR] {err}")

    def display_ui():
        print("\n" + "=" * 40)
        print("       ACTIVE STUDENT DIRECTORY")
        print("=" * 40)
        
        records = manager.get_all_students()
        if not records:
            print("No student records currently stored.")
            return
            
        for sid, data in records.items():
            formatted_id = manager.format_id(sid)
            courses_count = len(data["Subjects"])
            courses_str = ", ".join(data["Subjects"]) if courses_count > 0 else "None"
            
            print(f"\nID Code   : {formatted_id}")
            print(f"Name      : {data['Name']}")
            print(f"Program   : {data['Course']}")
            print(f"Courses   : {courses_count} Enrolled -> {courses_str}")
            print("-" * 40)

    def search_ui():
        print("\n" + "=" * 40)
        print("           SEARCH DIRECTORY")
        print("=" * 40)
        
        query = input("Enter Student ID or Name: ").strip()
        matches = manager.search_student(query)
        
        if not matches:
            print("\n[NOTICE] No matching student record located.")
            return
            
        for data in matches:
            formatted_id = manager.format_id(data["Student ID"])
            courses_str = ", ".join(data["Subjects"]) if data["Subjects"] else "None"
            print("\n[MATCH FOUND]")
            print(f"ID Code   : {formatted_id}")
            print(f"Name      : {data['Name']}")
            print(f"Program   : {data['Course']}")
            print(f"Courses   : {courses_str}")
<<<<<<< HEAD

    def clear_ui():
        print("\n" + "=" * 40)
        print("        RESET DATABASE FILE")
        print("=" * 40)
        confirm = input("Are you sure you want to clear all stored JSON records? (y/n): ").strip().lower()
        if confirm == 'y':
            manager.clear_database()
            print("\n[SUCCESS] Database cleared and JSON file reset.")
        else:
            print("\n[CANCELLED] Database reset aborted.")
=======
>>>>>>> 42c39107a86d2a516b0a40215e9d68923d6e3420

    while True:
        print("\n" + "#" * 40)
        print("   UNIVERSITY ACADEMIC RECORDS SYSTEM")
        print("#" * 40)
        print("1. Register New Student")
        print("2. Manage/Edit Enrolled Courses")
        print("3. Display All Student Records")
        print("4. Query Student Directory")
        print("5. Reset / Clear Database")
        print("6. Return to Main Launcher")
        
        choice = input("\nSelect operation (1-6): ").strip()
        if choice == "1":
            register_ui()
        elif choice == "2":
            manage_courses_ui()
        elif choice == "3":
            display_ui()
        elif choice == "4":
            search_ui()
        elif choice == "5":
            clear_ui()
        elif choice == "6":
            print("Exiting console interface...")
            break
        else:
            print("[INVALID] Please select a valid option (1-6).")