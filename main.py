import logging
class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger('StudentProcessor')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f"Added student: {student}")
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.logger.info(f"Removed student: {student}")
        else:
            self.logger.warning(f"Student not found: {student}")
    def process_students(self):
        self.logger.info("Processing students:")
        for student in self.students:
            self.logger.info(f"Processing student: {student}")
student_processor = StudentProcessor()
student1 = "John"
student2 = "Jane"
student_processor.add_student(student1)
student_processor.add_student(student2)
student_processor.process_students()
student_processor.remove_student(student1)
student_processor.remove_student("Mary")
