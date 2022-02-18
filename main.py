import datetime

# Importing now as today as asked in the assignment (2021-06-14)

now = datetime.date(2021, 6, 14)


class Product:
    def __init__(self, name, brand, price):

        self._name = name
        self._brand = brand
        self._price = price

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getBrand(self):
        return self._brand

    def setBrand(self, brand):
        self._brand = brand

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price


# Perishable products below this line:


class PerishableProduct(Product):

    def __init__(self, name, brand, price, expirationDate):
        super().__init__(name, brand, price)
        self._expirationDate = expirationDate

    def getExpirationDate(self):
        return self._expirationDate

    def setExpirationDate(self, expirationDate):
        self._expirationDate = expirationDate

    # Getting discount values based on time of expiration
    def aboutToExpire(self, now):

        difference = datetime.timedelta(days=-5)
        expDateSplit = self.getExpirationDate().split('-')
        expDate = datetime.date(int(expDateSplit[0]), int(expDateSplit[1]), int(expDateSplit[2]))
        discount = 0

        if expDate == now:
            discount = 0.7
        else:
            if expDate <= (now-difference):
                discount = 0.3

        return discount


class Food(PerishableProduct):
    def __init__(self, name, brand, price, expirationDate):

        super().__init__(name, brand, price, expirationDate)


class Beverages(PerishableProduct):
    def __init__(self, name, brand, price, expirationDate):

        super().__init__(name, brand, price, expirationDate)


# Perishable products end with this last class


# Nonperishable products


class Clothes(Product):

    def __init__(self, name, brand, price, size, color):

        super().__init__(name, brand, price)
        self._size = size
        self._color = color

    def getSize(self):
        return self._size

    def setSize(self, size):
        self._size = size
        return self._size

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

class Appliances(Product):

    def __init__(self, name, brand, price, model, productionDate, weight):

        super().__init__(name, brand, price)
        self._model = model
        self._productionDate = productionDate
        self._weight = weight

    def getModel(self):
            return self._model

    def setModel(self, model):
            self._model = model

    def getProductionDate(self):
        return self._productionDate

    def setProductionDate(self, productionDate):
        self._productionDate = productionDate

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    # Getting discount values based on the day of the week
    def discountCheck(self, now):

        listOfWeekdays = [2, 3, 4, 5]
        weekend = [6,7]
        discount = 0

        if now.isoweekday() in listOfWeekdays:

            discount = 0.1

        elif self.getPrice() > 999 and now.isoweekday() in weekend:
                discount = 0.07

        return discount


# Nonperishable products end here


def cashier(cart):

    # Variables for sums and flags
    discountSum = 0
    sum = 0


    # IMPORTING TODAY'S DATE, EVEN THOUGH CALCULATIONS ARE DONE WITH 2021-06-14
    # AS WRITTEN IN ASSIGNMENT, TO CHECK IF IT WORKS, 'now' DATE IS ON TOP OF THE CODE,
    # CAN BE CHANGED TO ANY DATE

    print(datetime.datetime.now())

    print('---Products--- \n')

    # Looping through products in the cart

    for element in cart:

        sum+=(element[0].getPrice() * element[1])

        # element[0] is the object and element[1] is the quantity

        # Checking the type of product and printing what is needed

        if isinstance(element[0], Food) or isinstance(element[0], Beverages) :
            print('\nName: ', element[0].getName(), 'Brand:', element[0].getBrand())
            print(element[1], ' x ', element[0].getPrice(), ' = ', round((element[1] * element[0].getPrice()), 2))
            discount = element[0].aboutToExpire(now)
            if discount != 0:
                print('#discount ', discount * 100, '%  = ', round( (element[0].getPrice() * element[1] * discount) ,2))
                discountSum += element[0].getPrice() * element[1] * discount

        # Checking the type of product and printing what is needed

        if isinstance(element[0], Appliances):
            print('\nName: ', element[0].getName(), 'Brand:', element[0].getBrand())
            print('Model: ', element[0].getModel())
            print(element[1], ' x ', element[0].getPrice(), ' = ', round((element[1] * element[0].getPrice()), 2))
            discount = element[0].discountCheck(now)
            if discount != 0:
                print('#discount ', discount * 100, '%  = ', round( (element[0].price * element[1] * discount) ,2))
                discountSum += element[0].getPrice() * element[1] * discount

        # Checking the type of product and printing what is needed

        if isinstance(element[0], Clothes):
            print('\nName: ', element[0].getName(), 'Brand:', element[0].getBrand())
            print('Size: ', element[0].getSize(), 'Color:', element[0].getColor())
            print(element[1], ' x ', element[0].getPrice(), ' = ', round((element[1] * element[0].getPrice()), 2))


    print('-' * 20)
    print('SUBTOTAL: ', round(sum, 2))
    print('DISCOUNT: ', round(discountSum, 2))
    total = sum - discountSum
    print('\nTOTAL: ', round(total, 2))


if __name__ == '__main__':
    apple = Food('Apple', 'BrandA', 1.5, '2021-06-14')
    milk = Beverages('Milk', 'BrandM', 0.99, '2022-02-02')
    tshirt = Clothes('T-shirt', 'BrandT', 15.99, 'M', 'violet')
    laptop = Appliances('Laptop', 'BrandL', 2345, 'ModelL', '2021-03-03', 1.125)

    cart = [[apple, 2.45], [milk, 3], [tshirt, 2], [laptop, 1]]
    cashier(cart)
