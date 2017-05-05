from datetime import date
from .Student import Student
from .Teacher import Teacher
from .Dish import Dish

class Order (object):
    OrderDate = None
    Dish = None
    Person = None
    OrderDelivery = None
    Status = None
    OrderNo = None

    def setOrderDate(self, orderdate):
        self.OrderDate = orderdate

    def setDish(self, dish):
        self.Dish = dish

    def setPerson(self, person):
        self.Person = person

    def setOrderDelivery(self, orderdelivery):
        self.OrderDelivery = orderdelivery

    def setStatus(self, status):
        self.Status = status

    def setOrderNo(self, orderno):
        self.OrderNo = orderno