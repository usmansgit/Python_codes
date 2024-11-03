class Fraction:
    """
    This class represents a list of fractions that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd
        return self.__str__()

    def multiply(self, fraction_object):
        n = self.__numerator * fraction_object.__numerator
        d = self.__denominator * fraction_object.__denominator
        product_of_fractions = Fraction(n, d)
        return product_of_fractions

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b
    return a

"""def read_choice(command):
    while True:
        if command == "add":
            add_command()

        elif command == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")
            return

def add_command():
    fraction = input("Enter a fraction in the form integer/integer: ")
    name = input("Enter a name: ")

    fraction_dictionary = {}

    fraction = fraction.strip()

    fields = fraction.split("/")

    numerator = fields[0]
    denominator = fields[1]

    fraction_dictionary[name] = Fraction(int(numerator), int(denominator))

def print_command():
    name = input("Enter a name: ")"""


def main():
    fraction_dictionary = {}

    while True:
        command = input("> ")

        if command == "add":
            fraction = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")

            fraction = fraction.strip()

            fields = fraction.split("/")

            numerator = fields[0]
            denominator = fields[1]

            fraction_dictionary[name] = Fraction(int(numerator), int(denominator))

        elif command == "print":
            fraction_name = input("Enter a name: ")

            if fraction_name in fraction_dictionary:
                print(f"{fraction_name} = {fraction_dictionary[fraction_name].__str__()}")
            else:
                print(f"Name x was not found")

        elif command == "list":
            for fractions in sorted(fraction_dictionary):
                print(f"{fractions} = {fraction_dictionary[fractions].__str__()}")

        elif command == "*":
            first_operand = input("1st operand: ")
            if first_operand not in fraction_dictionary:
                print(f"Name {first_operand} was not found")
            else:
                second_operand = input("2nd operand: ")
                if second_operand not in fraction_dictionary:
                    print(f"Name {second_operand} was not found")
                else:
                    print(f"{fraction_dictionary[first_operand]} * {fraction_dictionary[second_operand]} = "
                          f"{fraction_dictionary[first_operand].multiply(fraction_dictionary[second_operand])}")

                    print(f"simplified {(fraction_dictionary[first_operand].multiply(fraction_dictionary[second_operand])).simplify()}")

        elif command == "file":
            file_name = input("Enter the name of the file: ")

            try:
                file = open(file_name, mode="r")
            except IndexError:
                print("Error: the file cannot be read.")
                return

            for file_line in file:
                file_line = file_line.rstrip()
                fields = file_line.split("=")

                fraction_name = fields[0]
                nd = fields[1].split("/")
                numerator = nd[0]
                denominator = nd[1]

                fraction_dictionary[fraction_name] = Fraction(int(numerator), int(denominator))

            file.close()

        elif command == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")


if __name__ == '__main__':
    main()
