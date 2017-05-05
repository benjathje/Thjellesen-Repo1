from datetime import date

class Student:
    Name = ''
    Surname = ''
    BirthDate = None
    Grades = []
    AllSubjects = []

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

    def __init__(self):
        self.AllSubjects = []

class Subject:
    SubjectName = ''
    Grades = []

    def __init__(self):
        self.Grades = []

    def setSubjectName (self, subjectname):
        self.SubjectName = str(subjectname)

    def addSubject (self, subjectname):
        newSubject = Subject()
        newSubject.setSubjectName(subjectname)
        self.AllSubjects.append(newSubject)

    def searchSubject (self, subjectname):
        for item in self.AllSubjects:
            if item.SubjectName == subjectname:
                return item

    def setSubjectGrade(self, subjectname, grade):
        self.searchSubject(subjectname).Grades.append(grade)

    def avgSubjectGrade (self, subjectname):
        return float(sum(self.searchSubject(subjectname).Grades) / len(self.searchSubject(subjectname).Grades))

    