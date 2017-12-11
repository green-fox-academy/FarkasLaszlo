#Teacher Student

#Create Student and Teacher classes
#Student
#learn()
#question(teacher) -> calls the teachers answer method
#Teacher
#teach(student) -> calls the students learn method
#answer()

class Teacher():
    def teach(self, student):
        student.learn()

    def answer(self):
        pass



class Student():
    def learn(self):
        pass

    def question(self, teacher):
        teacher.answer()


