from .Person import Person


class Teacher(Person):
    Discount = ''

    def setDiscount(self, discount):
        self.Discount = int(discount)

