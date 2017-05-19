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

        Input = str(input("INPUT STUDENT SURNAME:\n"))
        Student1.setSurname(Input)

        Input = str(input("INPUT STUDENT DIVISION:\n"))
        Student1.setDivision(Input)

        Input = str(input("INPUT STUDENT DNI: \n")) #Ya se que no es DNI si esta en ingles pero lo hago por que me acabo de dar cuenta y paja cambiar las clases
        Student1.setDNI(Input)

        People.append(Student1)

    elif (Input == '2'):
        Teacher1 = Teacher()
        Input = str(input("INPUT TEACHER NAME:\n"))
        Teacher1.setName(Input)

        Input = str(input("INPUT TEACHER SURNAME:\n"))
        Teacher1.setSurname(Input)

        Input = str(input("INPUT TEACHER DISCOUNT:\n"))
        Teacher1.setDiscount(Input)

        Input = str(input("INPUT TEACHER DNI: \n"))  #Mas de lo mismo
        Teacher1.setDNI(Input)

        People.append(Teacher1)

    elif (Input == '3'):
        Dish1 = Dish()
        Input = str(input("INPUT DISH NAME\n"))
        Dish1.setDishName(Input)

        Input = int(input("INPUT DISH PRICE\n"))
        Dish1.setDishPrice(Input)

        Dishes.append(Dish1)

    elif (Input == '4'):
        Order1 = Order()
        Day = int (input("INPUT ORDER DAY:\n"))
        Month = int(input("INPUT ORDER MONTH:\n"))
        Year = int(input("INPUT ORDER YEAR:\n"))
        Order1.OrderDate(date(Day, Month, Year))

        for item in Dishes:
            print(item.Name + " - ")
        Input = input("INPUT DISH NAME")
        for item in Dishes:
            if (item.Name == Input):
                Order1.setDish(item)

        for item in People:
            print(item.DNI + "|" + item.Name + " " + item.Surname + " - ")
        Input = input("INPUT PERSON DNI: ")
        for item in People:
            if (item.DNI == Input):
                Order1.setPerson(item)

        Input = str(input("INPUT ORDER DELIVERY TIME: "))
        Order1.setOrderDelivery(Input)

        Order1.setStatus(0)
        Order1.setOrderNo(OrderNo)
        OrderNo += 1

        Orders.append(Order1)

    elif (Input == '5'):
        while (True):
            Input = input ("EDIT STUDENT")
