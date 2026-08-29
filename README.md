# Student Information Management System (SIMS)

A modular, Python-based academic record management system featuring both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) built with Tkinter. The system handles student registration, duplicate detection, flexible course management (add/drop), academic status tracking, and JSON data persistence.

---

## Key Features

* **Modular Architecture:** Business logic is decoupled into a dedicated manager class, with distinct presentation layers for CLI and GUI modes.
* **Tuple-Based Unique IDs:** Student numbers are structured as `(Year, Sequence)` pairs (e.g., `2026-1001`) with automatic sequence generation.
* **Duplicate Prevention:** Case-insensitive validation prevents duplicate student name registrations.
* **Dynamic Course Management:** Real-time course addition and dropping from comma-separated lists without requiring re-entry of existing courses.
* **Status Lifecycle Tracking:** Soft deletion (`Dropped`) to archive inactive students without breaking database consistency, alongside permanent record removal.
* **JSON Data Persistence:** Auto-saving and retrieval using structured JSON files (`students_data.json`) for straightforward reset and inspection.

---

## File Structure

```text
├── main.py              # Application entry point and launcher
├── student_manager.py   # Core business logic and data persistence engine
├── console_app.py       # Terminal/CLI interface
├── gui_app.py           # Tkinter graphical interface
├── students_data.json   # Persistent JSON data storage (auto-generated)
└── README.md            # Project documentation

```

---

## Installation & Requirements

* Python 3.10+
* Standard libraries only (`tkinter`, `json`, `datetime`, `os`, `sys`) — no external package installations required.

---

## Usage

Run the main launcher from your terminal:

```bash
python main.py

```

From the launcher menu, select:

1. **Option 1:** Launch the interactive Console application.
2. **Option 2:** Launch the Tkinter Graphical User Interface.
3. **Option 3:** Reset and clear all stored JSON records.
4. **Option 4:** Exit the program.

---

## Git Workflow & Collaboration

* Development follows a feature-branching model (`feature/console-app`, `feature/gui-app`, etc.).
* All new features are pushed to remote feature branches and merged into `main` via Pull Requests.
