class Person:
    def __init__(self, name="Jane Doe", age=30, gender="female"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm "+self.name+", a "+str(self.age)+" year old "+self.gender)

    def get_goal(self):
        print("My goal is: Live for the moment")
"""
person1 = Person("Laci",28,"male")
person1.introduce()
person1.get_goal()
"""


class Student(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", previous_organization="School of Life", skipped_days=0):
        super().__init__(name ,age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("My goal is: Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender+" from "+self.previous_organization+" who skipped "+str(self.skipped_days)+" days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

"""
student1 = Student()
student1.get_goal()
student1.introduce()
student1.skip_days(10)
student1.introduce()
"""


class Mentor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", level="intermediate"):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print("My goal is: Educate brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm "+self.name+", a "+str(self.age)+" year old "+self.gender+" "+self.level+" mentor.")


"""
mentor1 = Mentor()
mentor1.introduce()
"""


class Sponsor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", company="Google", hired_students=0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print("Hi, I'm "+self.name+", a "+str(self.age)+" year old "+self.gender+" who represents "+self.company+" and hired "+str(self.hired_students)+" students so far.")

    def get_goal(self):
        print("My goal is: Hire brilliant junior software developers.")

    def hire(self):
        self.hired_students += 1


"""
sponsor1 = Sponsor()
sponsor1.hire()
sponsor1.hire()
sponsor1.get_goal()
sponsor1.introduce()
"""


class PallidaClass():
    def __init__(self, class_name, students=[], mentors=[]):
        self.class_name = class_name
        self.students = students
        self.mentors = mentors

    def add_student(self,student):
        self.students.append(student)

    def add_mentor(self,mentor):
        self.mentors.append(mentor)

    def info(self):
        print("Pallida " + self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")


people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()
    sponsor.hire()


for member in people:
    member.introduce()
    member.get_goal()

badass = PallidaClass('BADCAT')
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)
badass.info()