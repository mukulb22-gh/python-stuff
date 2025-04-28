#structural flyweight pattern example on school teachers and students

#Teacher concrete class
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self, student):
        print(f"{self.name} is teaching {self.subject} to {student.name}")

#Student concrete class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

#TeacherFactory class
class TeacherFactory:
    _teachers = {}

    @classmethod
    def get_teacher(cls, name, subject):
        if (name, subject) not in cls._teachers:
            cls._teachers[(name, subject)] = Teacher(name, subject)
        return cls._teachers[(name, subject)]


if __name__ == "__main__":
    teacher1 = TeacherFactory.get_teacher("Mr. Kapil", "Math")
    teacher2 = TeacherFactory.get_teacher("Ms. Puja", "Science")
    teacher3 = TeacherFactory.get_teacher("Mr. Sahil", "Math")

    student1 = Student("Gagan", 10)
    student2 = Student("Baban", 11)
    student3 = Student("kangana", 10)

    teacher1.teach(student1)
    teacher2.teach(student2)
    teacher3.teach(student3)

    print(f"teacher1 is teacher3: {teacher1 is teacher3}")
    print(f"teacher1 == teacher3: {teacher1 == teacher3}")
    print(f"teacher1.name == teacher3.name: {teacher1.name == teacher3.name}")
    print(f"teacher1.subject == teacher3.subject: {teacher1.subject == teacher3.subject}")