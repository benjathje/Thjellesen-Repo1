from .Person import Person

class Student (Person):
    Division = ''

    def setDivision (self, division):
        self.Division = str(division)

