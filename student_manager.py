import json
import os
import datetime

class StudentManager:
    def __init__(self, data_file="students_data.json", start_seq=1000):
        self.data_file = data_file
        self.students = {}
        self.current_seq = start_seq
        self.load_from_json()

    def save_to_json(self):
        serialized_data = {
            f"{sid[0]}-{sid[1]}": record for sid, record in self.students.items()
        }
        with open(self.data_file, "w") as f:
            json.dump(serialized_data, f, indent=4)

    def load_from_json(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r") as f:
                raw_data = json.load(f)
            self.students = {}
            max_seq = self.current_seq
            for str_id, record in raw_data.items():
                year_str, seq_str = str_id.split("-")
                sid_tuple = (int(year_str), int(seq_str))
                record["Student ID"] = sid_tuple
                self.students[sid_tuple] = record
                if int(seq_str) > max_seq:
                    max_seq = int(seq_str)
            self.current_seq = max_seq
        except (json.JSONDecodeError, ValueError):
            self.students = {}

    def clear_database(self):
        self.students = {}
        self.current_seq = 1000
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

    def generate_student_id(self):
        current_year = datetime.datetime.now().year
        self.current_seq += 1
        return (current_year, self.current_seq)

    def check_duplicate_name(self, name):
        normalized = name.strip().casefold()
        for record in self.students.values():
            if record["Name"].casefold() == normalized:
                return True
        return False

    def add_student(self, name, program, courses_list):
        clean_name = name.strip().title()
        clean_prog = program.strip().upper()

        if not clean_name or not clean_prog:
            raise ValueError("Student Name and Program cannot be empty.")

        if self.check_duplicate_name(clean_name):
            raise ValueError(f"Student '{clean_name}' is already registered in the system.")

        student_id = self.generate_student_id()
        cleaned_courses = [c.strip().upper() for c in courses_list if c.strip()]

        record = {
            "Name": clean_name,
            "Course": clean_prog,
            "Student ID": student_id,
            "Subjects": cleaned_courses
        }

        self.students[student_id] = record
        self.save_to_json()
        return record

    def find_record(self, identifier):
        query = identifier.strip().casefold()
        for sid, record in self.students.items():
            formatted_id = self.format_id(sid).casefold()
            if query == formatted_id or query == record["Name"].casefold():
                return sid, record
        return None, None

    def update_student_courses(self, identifier, new_courses_list):
        sid, record = self.find_record(identifier)
        if not record:
            raise ValueError(f"No student record found matching identifier: '{identifier}'.")

        cleaned_courses = [c.strip().upper() for c in new_courses_list if c.strip()]
        record["Subjects"] = cleaned_courses
        self.save_to_json()
        return record

    def get_all_students(self):
        return self.students

    def search_student(self, query):
        q = query.strip().casefold()
        results = []
        for sid, record in self.students.items():
            formatted_id = self.format_id(sid).casefold()
            if q == formatted_id or q in record["Name"].casefold():
                results.append(record)
        return results

    @staticmethod
    def format_id(student_id):
        return f"{student_id[0]}-{student_id[1]}"