import sys
from student_manager import StudentManager
from console_app import run_console_app
from gui_app import run_gui_app

def main():
    manager = StudentManager()

    while True:
        print("\n==========================================")
        print("  CPE106L - APPLICATION ENTRY LAUNCHER   ")
        print("==========================================")
        print("1. Launch Console-Based System")
        print("2. Launch Graphical User Interface (GUI)")
        print("3. Reset All JSON Data")
        print("4. Exit Application")
        
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            run_console_app(manager)
        elif choice == "2":
            run_gui_app(manager)
        elif choice == "3":
            confirm = input("Reset stored data file? (y/n): ").strip().lower()
            if confirm == 'y':
                manager.clear_database()
                print("JSON storage file reset successfully.")
        elif choice == "4":
            print("\nShutting down application. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please input 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()