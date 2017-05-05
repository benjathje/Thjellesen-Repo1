class Dish (object):
    DishName = ''
    DishPrice = ''

    def setDishName(self , dishname):
        self.DishName = str(dishname)

    def setDishPrice(self , dishprice):
        self.DishPrice = int(dishprice)