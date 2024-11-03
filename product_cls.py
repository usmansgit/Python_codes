"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    def __init__(self, product, price,):
        self.__product = product
        self.__price = price
    def printout(self):
        print("—" * 25)
        print("product:   ", self.__product)
        print("price: ", self.__price)


    def set_sale_percentage(self,percentage):
        self.__sale=percentage
        return  percentage

    def get_price(self, percentage):
        self.__newprice= (self.__price/100)*percentage
        return self.__newprice



def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
