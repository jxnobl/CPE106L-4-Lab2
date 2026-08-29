```markdown
# Student Information Management System (SIMS)
### CPE106L-4: Software Design Laboratory — Laboratory Report 2
**Mapúa University** | School of Artificial Intelligence, Electrical, Electronics, and Computer Engineering

---

## 📌 Project Overview

The **Student Information Management System (SIMS)** is a collaborative, modular Python software application designed to demonstrate the practical application of fundamental Python data structures: **Strings**, **Lists**, **Tuples**, and **Dictionaries**. 

The system features a dual-interface architecture offering both an interactive **Command-Line Interface (CLI)** and a modern **Graphical User Interface (GUI)** built with Tkinter. It implements data persistence via JSON serialization, record conflict handling, dynamic course enrollment, and student lifecycle management.

---

## 💡 Implementation of Core Data Structures

| Data Structure | Role in System | Implementation Detail |
| :--- | :--- | :--- |
| **`String`** | Identity & Categorization | Stores sanitized student names, degree programs, and UI text blocks. |
| **`Tuple`** | Immutable Unique ID | Implements `(Year, Sequence)` identifiers (e.g., `(2026, 1001)`) preventing runtime mutation. |
| **`List`** | Course Management | Houses dynamic, ordered collections of enrolled academic courses (`Subjects`). |
| **`Dictionary`** | Primary Record Container | Maps field attributes (`Name`, `Course`, `Student ID`, `Subjects`, `Status`) into structured records. |

---

## 🎨 Interactive Interface & User Experience (UX)

### 1. Graphical User Interface (`gui_app.py`)
* **Interactive Table View (`ttk.Treeview`):** Real-time tabulated display of all registered students with dedicated column headers and a synchronized vertical scrollbar.
* **Master-Detail Binding:** Selecting a student row automatically loads records into the workspace for instant updating or course management.
* **Modal Operations Dialog:** Dedicated pop-up windows for single-action operations like targeted course dropping.
* **Status Lifecycle Indicators:** Visual differentiation between `Active` and `Dropped` academic states.
* **Destructive Action Safeguards:** Confirmation modal alerts (`askyesno`) before dropping or permanently deleting student records.

### 2. Command-Line Interface (`console_app.py`)
* **Menu-Driven Workflow:** Numbered options facilitating student enrollment, directory inspection, course adjustments, and record searching.
* **Agnostic Lookup:** Record querying via either formatted ID (`YYYY-####`) or partial student name matching.

---

## 🚀 Key Functional Features

* **Modular Separation of Concerns:** Core operations decoupled from presentation layers via `StudentManager`.
* **Duplicate Prevention:** Case-insensitive validation against redundant student registrations.
* **Dynamic Course Add/Drop:** Targeted course adjustments via comma-separated entry without re-entering existing subjects.
* **Dual Deletion Mechanism:** Supports both non-destructive archiving (`Dropped`) and permanent record removal (`Delete`).
* **Persistent Storage Engine:** Automatic syncing to `students_data.json` on all create, update, and delete actions.

---

## 📁 Repository Structure

```text
├── main.py              # Application entry point and launcher
├── student_manager.py   # Core logic, validations, and JSON persistence engine
├── console_app.py       # Terminal/CLI interface
├── gui_app.py           # Tkinter modern GUI application
├── students_data.json   # Auto-generated JSON database
└── README.md            # Project documentation and specifications

```

---

## ⚙️ Setup & Execution

### Prerequisites

* **Python 3.10+**
* Standard Python libraries: `tkinter`, `ttk`, `json`, `os`, `sys`, `datetime` *(No external `pip` dependencies required)*

### Running the Application

Launch the unified entry launcher from your terminal:

```bash
python main.py

```

```text
==========================================
  CPE106L - APPLICATION ENTRY LAUNCHER   
==========================================
1. Launch Console-Based System
2. Launch Graphical User Interface (GUI)
3. Reset All JSON Data
4. Exit Application

Enter choice (1-4):

```

---

## 🌿 Collaborative Git Workflow

* **Branching Strategy:** Feature branches used for isolated module development (e.g., `feature/console-app`, `feature/gui-app`).
* **Integration:** Work merged into the `main` branch via peer-reviewed GitHub Pull Requests.
* **Conflict Resolution:** Git merge conflicts managed and verified through VS Code Source Control.

```

```
