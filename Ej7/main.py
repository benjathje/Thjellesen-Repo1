from datetime import date
from .Student import Student
from .Teacher import Teacher
from .Dish import Dish
from .Order import Order

Orders = []
People = []
Dishes = []

Input = None
Day = None
Month = None
Year = None

OrderNo = 0

while (true)
    Input = input ("1- ADD STUDENT\n"
                   "2- ADD TEACHER\n"
                   "3- ADD DISH\n"
                   "4- ADD ORDER\n"
                   "5- EDIT PERSON/DISH/ORDER\n"
                   "6- DELETE PERSON/DISH/ORDER\n"
                   "7- SHOW ORDERS\n")

    if (Input == '1'):
        Student1 = Student ()
        Input = str (input("INPUT STUDENT NAME:\n"))
        Student1.setName(Input)