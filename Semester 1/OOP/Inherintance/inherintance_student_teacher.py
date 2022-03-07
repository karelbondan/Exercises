class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def to_string(self):
        return f'Name is {self.name}\nAddress is {self.address}'


class Student(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.course_grade = {}
        self.total = 0
        self.num_courses = 0

    def to_string(self):
        return f'{Person.to_string(self)}'

    def add_course_grade(self, course: str, grade: int):
        self.course = course
        self.grade = grade
        self.course_grade.update({course: grade})
        self.num_courses = len(self.course_grade)

    def print_grades(self):
        for i in self.course_grade:
            print(f'{i}: {self.course_grade[i]}')

    def get_avg_grade(self):
        for i in self.course_grade.values():
            self.total += i
        self.avggrade = self.total / len(self.course_grade)
        return self.avggrade

    def get_num_courses(self): #defined it myself to check the num_courses
        return self.num_courses

class Teacher(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.courses = []
        self.num_courses = 0

    def to_string(self):
        return f'{Person.to_string(self)}'

    def add_course(self, course):
        if course in self.courses:
            return False
        else:
            self.courses.append(course)
            self.num_courses = len(self.courses)
            return True

    def remove_course(self, course):
        if course not in self.courses:
            return False
        else:
            self.courses.remove(course)
            self.num_courses = len(self.courses)
            return True

    def get_num_courses(self): #defined it myself to check the num_courses
        return self.num_courses


def main():
    a = Student('Moo', 'Semarang')
    print(a.to_string())
    a.add_course_grade('Biology', 94)
    a.add_course_grade('Indonesian', 89)
    a.add_course_grade('History', 77)
    a.add_course_grade('Design Graphics', 98)
    a.add_course_grade('Civics', 67)
    print(a.get_avg_grade())
    print(a.print_grades())
    print(a.get_num_courses())
    b = Teacher("Rawr", "Kudus")
    print(b.to_string())
    b.add_course('Indonesian')
    b.add_course('Indonesian')
    b.add_course('History')
    b.add_course('Civics')
    print(b.get_num_courses())
    b.remove_course('Biology')
    b.remove_course('History')
    print(b.get_num_courses())

main()