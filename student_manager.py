import datetime

class StudentManager:
    def __init__(self, start_seq=1000):
        self.students = {}
        self.current_seq = start_seq

    def generate_student_id(self):
        current_year = datetime.datetime.now().year
        self.current_seq += 1
        return (current_year, self.current_seq)

    def add_student(self, name, course, subjects_list):
        if not name or not course:
            raise ValueError("Student Name and Course/Program cannot be empty.")
            
        student_id = self.generate_student_id()
        cleaned_subjects = [s.strip().upper() for s in subjects_list if s.strip()]
        
        record = {
            "Name": name.strip().title(),
            "Course": course.strip().upper(),
            "Student ID": student_id,
            "Subjects": cleaned_subjects
        }
        
        self.students[student_id] = record
        return record

    def get_all_students(self):
        return self.students

    def search_student(self, query):
        query = query.strip().lower()
        results = []
        for student_id, record in self.students.items():
            formatted_id = f"{student_id[0]}-{student_id[1]}"
            if query == formatted_id.lower() or query in record["Name"].lower():
                results.append(record)
        return results

    @staticmethod
    def format_id(student_id):
        return f"{student_id[0]}-{student_id[1]}"