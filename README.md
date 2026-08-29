# 🎓 Student Information Management System (SIMS)

> **A modular Python-based Student Information Management System featuring both a Command-Line Interface and a Tkinter GUI, with persistent JSON storage and structured student record management.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Storage-JSON-green?style=for-the-badge" alt="JSON">
  <img src="https://img.shields.io/badge/Course-CPE106L--4-purple?style=for-the-badge" alt="CPE106L-4">
</p>

<p align="center">
  <strong>Mapúa University</strong><br>
  School of Artificial Intelligence, Electrical, Electronics, and Computer Engineering
</p>

---

## 📖 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Data Structures](#-data-structures)
* [System Architecture](#-system-architecture)
* [Interfaces](#-interfaces)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Usage](#-usage)
* [Data Management](#-data-management)
* [Git Workflow](#-collaborative-git-workflow)
* [Authors](#-authors)

---

## 📌 Overview

The **Student Information Management System (SIMS)** is a modular Python application developed for **CPE106L-4 Software Design Laboratory**.

The project demonstrates the practical application of fundamental Python data structures—**Strings, Lists, Tuples, and Dictionaries**—within a functional student management system.

SIMS provides **two ways to interact with the system**:

* 🖥️ **Command-Line Interface (CLI)** — A menu-driven terminal application
* 🪟 **Graphical User Interface (GUI)** — A responsive Tkinter-based desktop application

The system also includes **persistent JSON storage**, input validation, duplicate prevention, student status management, and course add/drop functionality.

### 🔄 How SIMS Works

```text
                    ┌──────────────────┐
                    │     main.py      │
                    │ Application      │
                    │    Launcher      │
                    └────────┬─────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │   Console CLI   │     │   Tkinter GUI   │
        │ console_app.py  │     │    gui_app.py   │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 └───────────┬───────────┘
                             ▼
                 ┌─────────────────────────┐
                 │    StudentManager       │
                 │ student_manager.py      │
                 │                         │
                 │ • Validation            │
                 │ • Student Records       │
                 │ • Course Management     │
                 │ • Status Management     │
                 └────────────┬────────────┘
                              ▼
                 ┌─────────────────────────┐
                 │   students_data.json    │
                 │   Persistent Storage     │
                 └─────────────────────────┘
```

---

## ✨ Features

### 👨‍🎓 Student Management

* Register new students
* Store student names and degree programs
* Generate structured Student IDs
* Search students by name or Student ID
* Display complete student directories
* Edit existing student information

### 📚 Course Management

* Add multiple courses/subjects
* Drop individual enrolled courses
* Preserve existing courses when adding new ones
* Display current course enrollment

### 🔄 Student Status Management

Students can move through different states without immediately deleting their records:

```text
ACTIVE
  │
  │ Drop
  ▼
DROPPED
  │
  │ Restore
  ▼
ACTIVE
```

The system also supports permanent record deletion when required.

### 💾 Persistent Storage

All student records are automatically synchronized with:

```text
students_data.json
```

Changes are saved when records are:

* Created
* Updated
* Dropped
* Restored
* Deleted
* Modified through course add/drop operations

### 🛡️ Validation & Safety

* Case-insensitive duplicate-name prevention
* Student ID validation
* Input validation
* Confirmation dialogs for destructive actions
* Controlled course modification
* Consistent record structure

---

## 🧠 Data Structures

The system was designed around four fundamental Python data structures.

| Data Structure | Purpose                                      | Example                               |
| -------------- | -------------------------------------------- | ------------------------------------- |
| **String**     | Stores text-based information                | `"Edmarc Justin C. Oabel"`            |
| **Tuple**      | Represents an immutable Student ID component | `(2026, 1001)`                        |
| **List**       | Stores enrolled courses                      | `["CPE106L", "CPE107"]`               |
| **Dictionary** | Stores complete student records              | `{"Name": "...", "Status": "ACTIVE"}` |

### 🔹 String

Strings are used for:

* Student names
* Degree programs
* Status labels
* Course names
* Formatted output

### 🔹 Tuple

Tuples are used to represent immutable Student ID components.

```python
(2026, 1001)
```

This provides a structured identifier while preserving the immutability of the tuple.

### 🔹 List

Lists manage the student's enrolled subjects.

```python
[
    "CPE106L",
    "CPE107L",
    "MATH"
]
```

Because lists are mutable, courses can be added or removed as needed.

### 🔹 Dictionary

Dictionaries serve as the primary structure for individual student records.

```python
{
    "Name": "Student Name",
    "Course": "Computer Engineering",
    "Student ID": "2026-1001",
    "Subjects": ["CPE106L", "CPE107L"],
    "Status": "ACTIVE"
}
```

---

## 🖥️ Interfaces

### 🪟 Graphical User Interface

The Tkinter GUI provides a more user-friendly way to manage student records.

#### Dashboard

The main dashboard displays registered students in an interactive table.

**Key interface features:**

* 📋 Student directory
* 🔎 Student search
* ✏️ Record editing
* ➕ Course enrollment
* ➖ Course dropping
* 🔄 Status restoration
* 🗑️ Record deletion
* ⚠️ Confirmation dialogs

### 🖥️ Command-Line Interface

The CLI provides a lightweight terminal-based alternative.

Example launcher:

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

The CLI supports:

* Student registration
* Student searching
* Directory viewing
* Course modification
* Student status management
* Record deletion

---

## 🏗️ System Architecture

SIMS follows a **separation-of-concerns approach**.

```text
┌──────────────────────────────────────────┐
│              User Interface              │
│                                          │
│       CLI                 GUI            │
│  console_app.py       gui_app.py         │
└──────────────┬───────────────┬───────────┘
               │               │
               └───────┬───────┘
                       ▼
             ┌───────────────────┐
             │   StudentManager  │
             │                   │
             │ Business Logic    │
             │ Validation        │
             │ Record Management │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │   JSON Storage    │
             │                   │
             │ students_data.json│
             └───────────────────┘
```

### Why this structure?

The business logic is centralized inside `StudentManager`.

This allows both interfaces to use the **same underlying student-management logic**, reducing duplicated code and making the application easier to maintain.

---

## 📁 Project Structure

```text
Student-Information-Management-System/
│
├── 📄 main.py
│   └── Application entry point and interface launcher
│
├── 📄 student_manager.py
│   └── Core business logic, validation, and JSON storage
│
├── 📄 console_app.py
│   └── Command-Line Interface
│
├── 📄 gui_app.py
│   └── Tkinter Graphical User Interface
│
├── 📄 students_data.json
│   └── Persistent student data
│
└── 📄 README.md
    └── Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

### 2. Navigate to the Project

```bash
cd Student-Information-Management-System
```

### 3. Verify Python Installation

SIMS requires:

```text
Python 3.10+
```

Check your installed version:

```bash
python --version
```

### 4. Run the Application

```bash
python main.py
```

> **No third-party Python packages are required.**

SIMS uses standard Python libraries including:

* `tkinter`
* `json`
* `datetime`
* `os`
* `sys`

---

## 🚀 Usage

After launching `main.py`, select an interface:

```text
1. Launch Console-Based System
2. Launch Graphical User Interface (GUI)
3. Reset All JSON Data
4. Exit Application
```

### Recommended

For a visual demonstration:

```text
2 → Launch Graphical User Interface
```

For a lightweight terminal experience:

```text
1 → Launch Console-Based System
```

---

## 🗃️ Data Storage

SIMS uses a local JSON file for persistent storage:

```text
students_data.json
```

This allows student information to remain available even after the application is closed.

Example record structure:

```json
{
    "Student ID": "2026-1001",
    "Name": "Student Name",
    "Course": "BS Computer Engineering",
    "Subjects": [
        "CPE106L",
        "CPE107L"
    ],
    "Status": "ACTIVE"
}
```

> ⚠️ **Note:** `students_data.json` may be automatically generated or modified while using the application.

---

## 🔀 Collaborative Git Workflow

The project was developed collaboratively using Git and GitHub.

### 🌿 Branching

Feature-specific branches were used to separate development tasks:

```text
main
│
├── feature/console-app
├── feature/gui-app
└── feature/student-manager
```

### 🔄 Development Flow

```text
Create Feature
      │
      ▼
Create Branch
      │
      ▼
Develop & Test
      │
      ▼
Commit Changes
      │
      ▼
Push to GitHub
      │
      ▼
Create Pull Request
      │
      ▼
Review & Resolve Conflicts
      │
      ▼
Merge into main
```

GitHub Pull Requests were used to integrate completed features into the main branch. Merge conflicts were reviewed and resolved before final integration.

---

## 🎯 Learning Objectives

This project demonstrates the practical use of:

* 🐍 Python programming
* 🧩 Fundamental data structures
* 🏗️ Modular software design
* 🖥️ CLI application development
* 🪟 GUI development using Tkinter
* 💾 JSON-based persistence
* ✅ Input validation
* 🔀 Git branching and collaboration
* 🔄 CRUD-style record management

---

## 👥 Authors

### **Jabez C. Molar**

### **Edmarc Justin C. Oabel**

**CPE106L-4 — Software Design Laboratory**
**Mapúa University**

---

## ⭐ Project Highlights

| Category              | Implementation                  |
| --------------------- | ------------------------------- |
| Language              | Python                          |
| GUI                   | Tkinter                         |
| Storage               | JSON                            |
| Architecture          | Modular                         |
| Interfaces            | CLI + GUI                       |
| Data Structures       | String, List, Tuple, Dictionary |
| Validation            | Built-in                        |
| External Dependencies | None                            |
| Version Control       | Git + GitHub                    |

---

<p align="center">
  <strong>🎓 Student Information Management System</strong><br>
  Built with Python • Designed for CPE106L-4 • Mapúa University
</p>

<p align="center">
  ⭐ If you found this project useful, consider giving the repository a star!
</p>
