from .Ex2 import Student

Student1 = Student()

Student1.setName('Pedro')

Student1.setSurname('Smith')

Student1.setBirthDate(1990, 10, 20)

Student1.addGrade(10)
Student1.addGrade(7)
Student1.addGrade(8)

print(Student1.minGrade())

print(Student1.maxGrade())

print(Student1.avgGrade())
