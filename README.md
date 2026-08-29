# 🎓 University Academic Records System

A simple **Student Information Management System** built in Python, developed for **CPE106L-4 Laboratory Report 2 — Strings, Lists, Tuples, and Dictionaries** at Mapúa University.

The system stores student records, manages enrolled subjects, generates unique student IDs, and offers both a **console interface** and a **Tkinter GUI**, backed by a shared JSON data store.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="Tkinter" src="https://img.shields.io/badge/GUI-Tkinter-blue">
  <img alt="Storage" src="https://img.shields.io/badge/Storage-JSON-lightgrey">
  <img alt="Status" src="https://img.shields.io/badge/Status-Lab%20Activity-success">
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Data Model](#-data-model)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
  - [Console Mode](#console-mode)
  - [GUI Mode](#gui-mode)
- [Sample Data](#-sample-data)
- [Team](#-team)
- [Learning Outcomes](#-learning-outcomes)

---

## 📖 Overview

This project implements a university records system that demonstrates the practical use of Python's core data structures:

| Data Structure | Used For |
|---|---|
| **String** | Student name, program, course codes |
| **List** | Enrolled subjects per student |
| **Tuple** | Immutable Student ID `(year, sequence)` |
| **Dictionary** | The complete student record & the in-memory/JSON database |

Two front-ends share the same backend logic (`StudentManager`), so any change made in one interface is immediately reflected in the other's JSON-backed data.

## ✨ Features

- 📝 **Register students** with auto-generated, year-based unique IDs (e.g. `2026-1001`)
- 📚 **Manage enrolled courses** — add or drop subjects per student
- 🔍 **Search & query** the directory by ID or name
- ✏️ **Edit** existing student records (name, program, courses)
- 🚫 **Drop / Restore** students without losing their historical record
- 🗑️ **Permanently delete** a record when needed
- 💾 **Persistent JSON storage**, auto-loaded and saved on every change
- 🖥️ **Dual interface** — a menu-driven console app and a styled Tkinter GUI
- ♻️ **Reset database** option available from both interfaces

## 🗂 Project Structure

```
.
├── main.py               # Application launcher (choose console or GUI)
├── student_manager.py     # Core backend logic (StudentManager class)
├── console_app.py         # Console/terminal interface
├── gui_app.py              # Tkinter GUI interface
├── students_data.json      # Persistent JSON database (auto-generated)
└── README.md
```

## 🧬 Data Model

Each student is stored as a dictionary:

```python
student = {
    "Name": "Edmarc Justin C. Oabel",
    "Course": "BS COMPUTER ENGINEERING",
    "Student ID": (2026, 1001),          # tuple: (year, sequence)
    "Subjects": ["CPE106L-4", "ECEA101-1", ...],  # list
    "Status": "Active"                    # "Active" | "Dropped"
}
```

Student IDs are generated as `(current_year, incrementing_sequence)` starting from `1000`, and formatted for display as `YEAR-SEQ` (e.g. `2026-1001`).

## 🚀 Getting Started

**Requirements:** Python 3.x (Tkinter ships with the standard library, no extra installs needed)

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Run the application
python main.py
```

## 🕹 Usage

Running `main.py` opens the entry launcher:

```
==========================================
  CPE106L - APPLICATION ENTRY LAUNCHER
==========================================
1. Launch Console-Based System
2. Launch Graphical User Interface (GUI)
3. Reset All JSON Data
4. Exit Application
```

### Console Mode

A menu-driven terminal interface for all operations:

```
1. Register New Student
2. Manage Enrolled Courses (Add/Drop)
3. Display All Student Records
4. Query Student Directory
5. Reset / Clear Database
6. Return to Main Launcher
```

### GUI Mode

A Tkinter desktop window featuring:
- A **registration form** (Name, Program, Courses)
- A live **student directory table** with sortable columns
- Action buttons: `EDIT STUDENT`, `DROP COURSE`, `DROP STUDENT`, `RESTORE STUDENT`, `DELETE RECORD`
- Inline status bar feedback for every action

## 🧪 Sample Data

The repository ships with a sample `students_data.json` containing 3 records (2 active, 1 dropped) so you can explore the system immediately without registering new students first.

## 👥 Team

| Name | Program |
|---|---|
| Molar, Jabez C. | BS Computer Engineering |
| Oabel, Edmarc Justin C. | BS Computer Engineering |

**Course:** CPE106L-4 Software Design Laboratory
**School:** Artificial Intelligence, Electrical, Electronics, and Computer Engineering — Mapúa University

## 🎯 Learning Outcomes

- Differentiate Strings, Lists, Tuples, and Dictionaries
- Apply appropriate Python data structures in software design
- Develop a console-based application using collections
- Demonstrate teamwork through collaborative software development (Git branching, push/pull/merge)
- Analyze the advantages and limitations of different data structures

---

<p align="center"><i>Laboratory Report 2 — CPE106L-4 Software Design Laboratory, Mapúa University</i></p>
