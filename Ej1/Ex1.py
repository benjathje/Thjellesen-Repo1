from datetime import date

class Student:
    Name = ''
    Surname = ''
    BirthDate = None
    Grades = []

    def setName (self, name):
        self.Name = str(name)

    def setSurname (self, surname):
        self.Surname = str(surname)

    def setBirthDate (self, year, month, day):
        self.BirthDate = date(year, month, day)

    def addGrade (self, grade):
        self.Grades.append(grade)

    def minGrade (self):
        return min(self.Grades)

    def maxGrade (self):
        return max(self.Grades)

    def avgGrade (self):
        return (sum(self.Grades) / len(self.Grades))
