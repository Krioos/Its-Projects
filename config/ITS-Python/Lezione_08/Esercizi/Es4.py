from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def get_role(self)-> None:
        pass

    @abstractmethod
    def __str__(self)-> str:
        return f"{self.name}, age {self.age}"
    
class Student(Person):
    def __init__(self, name, age, student_id)-> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = set()
    
    def enroll(self, course)-> None:
        self.courses.add(course)
    
    def get_role(self)-> str:
        return "Student"
    
    def __str__(self)-> str:
        courses_str = ', '.join(course.course_name for course in self.courses) if self.courses else "None"
        return (f"Student: {self.name}, ID: {self.student_id}, Age: {self.age}, "
            f"Enrolled in courses: {courses_str}")

class Professor(Person):
    def __init__(self, name, age, professor_id, department = None)-> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = set()

    def assign_to_course(self, course)-> None:
        self.courses.add(course)
    
    def get_role(self)-> str:
        return "Professor"
      
    def __str__(self)-> str:
        courses_str = ', '.join(course.course_name for course in self.courses) if self.courses else "None"
        return (f"Professor: {self.name}, ID: {self.professor_id}, Age: {self.age}, "
            f"Department: {self.department.department_name if self.department else 'None'}, "
            f"Courses: {courses_str}")

class Course():
    def __init__(self, course_name, course_code, professor: Professor = None)-> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students = set()
        self.professor = professor

    def add_student(self, student)-> None:
        self.students.add(student)
        student.enroll(self)

    def set_professor(self, professor: Professor)-> None:
        self.professor = professor
        professor.assign_to_course(self)

    def __str__(self)-> str:
        prof_name = self.professor.name if self.professor else "None"
        students_names = ', '.join(student.name for student in self.students) if self.students else "None"
        return (f"Course name: {self.course_name}, Code: {self.course_code}, "
            f"Professor: {prof_name}, Students: {students_names}")
    
class Department():
    def __init__(self, department_name)-> None:
        self.department_name = department_name
        self.courses = set()
        self.professors = set()
    
    def add_course(self, course: Course)-> None:
        self.courses.add(course)
    
    def add_professor(self, professor: Professor)-> None:
        self.professors.add(professor)
        professor.department = self

    def __str__(self)-> str:
        courses_str = ', '.join(course.course_name for course in self.courses) if self.courses else "None"
        professors_str = ', '.join(professor.name for professor in self.professors) if self.professors else "None"
        return (f"Department: {self.department_name}, Courses: {courses_str}, "
            f"Professors: {professors_str}")
    
class University():
    def __init__(self, name)-> None:
        self.name = name
        self.departments = set()
        self.students = set()
    
    def add_department(self, department: Department)-> None:
        self.departments.add(department)

    def add_student(self, student: Student)-> None:
        self.students.add(student)

    
    def __str__(self)-> str:
        departments_str = ', '.join(department.department_name for department in self.departments) if self.departments else "None"
        students_str = ', '.join(student.name for student in self.students) if self.students else "None"
        return (f"University: {self.name}, Departments: {departments_str}, "
            f"Students: {students_str}")
    
#driver program

def main():
    # Create the university
    uni = University("Arcadia University")
    print(uni)

    # Create departments
    cs_dept = Department("Computer Science")
    lit_dept = Department("Literature")

    # Add departments to the university
    uni.add_department(cs_dept)
    uni.add_department(lit_dept)
    print("\nAfter adding departments:")
    print(uni)

    # Create professors
    prof_smith = Professor("Dr. Smith", 45, "P001")
    prof_jones = Professor("Dr. Jones", 50, "P002")

    # Assign professors to departments
    cs_dept.add_professor(prof_smith)
    lit_dept.add_professor(prof_jones)
    print("\nAfter adding professors to departments:")
    print(cs_dept)
    print(lit_dept)

    # Create courses
    ds_course = Course("Data Structures", "CS101")
    ml_course = Course("Medieval Literature", "LIT201")

    # Add courses to departments
    cs_dept.add_course(ds_course)
    lit_dept.add_course(ml_course)
    print("\nAfter adding courses to departments:")
    print(cs_dept)
    print(lit_dept)

    # Assign professors to courses
    ds_course.set_professor(prof_smith)
    ml_course.set_professor(prof_jones)
    print("\nAfter assigning professors to courses:")
    print(ds_course)
    print(ml_course)

    # Create students
    student_anna = Student("Anna", 20, "S1001")
    student_bob = Student("Bob", 21, "S1002")

    # Add students to university
    uni.add_student(student_anna)
    uni.add_student(student_bob)
    print("\nAfter adding students to university:")
    print(uni)

    # Enroll students in courses
    ds_course.add_student(student_anna)
    ds_course.add_student(student_bob)
    ml_course.add_student(student_bob)
    print("\nAfter enrolling students in courses:")
    print(ds_course)
    print(ml_course)

    # Final state of university
    print("\n--- Final University State ---")
    print(uni)
    print(cs_dept)
    print(lit_dept)
    print(ds_course)
    print(ml_course)

if __name__ == "__main__":
    main()
