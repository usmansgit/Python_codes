'''This program saves the list of fractions from class fraction'''
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


def main():
    '''Saving the list of fractions '''
    print("Enter fractions in the format integer/integer. \nOne fraction per line. Stop by entering an empty line.")

    fraction_list = []

    while True:
        fraction = input()

        if fraction == "":
            break

        fraction = fraction.strip()

        fields = fraction.split("/")

        numerator = fields[0]
        denominator = fields[1]

        fraction_list.append(Fraction(int(numerator), int(denominator)))

    print("The given fractions in their simplified form:")

    for fractions in fraction_list:
        print(f"{fractions} = {fractions.simplify()}")


if __name__ == '__main__':
    main()
