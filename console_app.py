from student_manager import StudentManager

def run_console_app(manager: StudentManager):
    def register_ui():
        print("\n" + "=" * 40)
        print("      STUDENT REGISTRATION MODULE")
        print("=" * 40)
        
        name = input("Enter Full Name: ").strip()
        course = input("Enter Degree Program: ").strip()
        raw_subs = input("Enter Subjects (comma-separated): ")
        subjects = [s.strip() for s in raw_subs.split(",") if s.strip()]
        
        try:
            record = manager.add_student(name, course, subjects)
            formatted_id = manager.format_id(record["Student ID"])
            print(f"\n[SUCCESS] Record initialized. Assigned ID: {formatted_id}")
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
            sub_count = len(data["Subjects"])
            sub_str = ", ".join(data["Subjects"]) if sub_count > 0 else "None"
            
            print(f"\nID Code   : {formatted_id}")
            print(f"Name      : {data['Name']}")
            print(f"Program   : {data['Course']}")
            print(f"Enrolled  : {sub_count} Subject(s) -> {sub_str}")
            print("-" * 40)

    def search_ui():
        print("\n" + "=" * 40)
        print("           SEARCH DIRECTORY")
        print("=" * 40)
        
        query = input("Enter Student ID or Full Name: ").strip()
        matches = manager.search_student(query)
        
        if not matches:
            print("\n[NOTICE] No matching student record located.")
            return
            
        for data in matches:
            formatted_id = manager.format_id(data["Student ID"])
            print("\n[MATCH FOUND]")
            print(f"ID Code   : {formatted_id}")
            print(f"Name      : {data['Name']}")
            print(f"Program   : {data['Course']}")
            print(f"Subjects  : {', '.join(data['Subjects']) if data['Subjects'] else 'None'}")

    while True:
        print("\n" + "#" * 40)
        print("   UNIVERSITY ACADEMIC RECORDS SYSTEM")
        print("#" * 40)
        print("1. Register New Student")
        print("2. Display All Student Records")
        print("3. Query Student Directory")
        print("4. Return to Main Launcher")
        
        choice = input("\nSelect operation (1-4): ").strip()
        if choice == "1":
            register_ui()
        elif choice == "2":
            display_ui()
        elif choice == "3":
            search_ui()
        elif choice == "4":
            print("Exiting console interface...")
            break
        else:
            print("[INVALID] Please select a valid option (1-4).")