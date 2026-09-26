class Student:
    def __init__(self, name, student_id, email, age, department, *marks):
        self.name = name
        self.student_id = student_id
        self.__email = email       
        self.age = age
        self.department = department
        self.__marks = list(marks) 

    def display_info(self, show_result=False):
        print("\n Student Information")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Email      : {self.__email}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")

        if show_result:
            print(f"Result     : {self.calculate_result()}")

    def calculate_result(self):
        if not self.__marks:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"

    def get_email(self):
        return self.__email


class UndergraduateStudent(Student):

    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        semester,
        *marks
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            *marks
        )

        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self, show_result=False):
        super().display_info(show_result)

        print(f"Semester   : {self.semester}")
        print(f"Type       : {self.get_student_type()}")


class GraduateStudent(Student):

    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic,
        *marks
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            *marks
        )

        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self, show_result=False):
        super().display_info(show_result)

        print(f"Research   : {self.research_topic}")
        print(f"Type       : {self.get_student_type()}")


student1 = UndergraduateStudent(
    "Tahsin Ahmad",
    "CSE101",
    "tahsin@example.com",
    22,
    "CSE",
    3,
    85, 78, 90, 88
)

student2 = GraduateStudent(
    "Rahim Ahmed",
    "CSE201",
    "rahim@example.com",
    25,
    "CSE",
    "Artificial Intelligence",
    92, 88, 95, 90
)

student1.display_info(show_result=True)
student2.display_info(show_result=True)


students = [student1, student2]

for student in students:
    print(f"{student.name} -> {student.get_student_type()}")

print("Student Email:", student1.get_email())

student3 = UndergraduateStudent(
    "Karim Hasan",
    "CSE102",
    "karim@example.com",
    21,
    "CSE",
    2,
    75, 82
)

student3.display_info(show_result=True)