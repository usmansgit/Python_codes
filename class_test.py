"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.
    def __init__(self, name, price):

        self.__name = name
        self.__price = price
        self.__sale = 0.0

    def printout(self):
        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")
    def set_sale_percentage(self,x):
        self.__sale=x
        return self.__sale
    def get_price(self):
        self.__price = self.__price - ((self.__price / 100)*self.__sale)
        return self.__price


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    Product("pizza", 4.95)


    Product.printout()
    print(f"Normal price: {Product.get_price():.2f}")


if __name__ == "__main__":
    main()