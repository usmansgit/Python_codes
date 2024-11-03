"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
    def simplify(self):
        grtst_cmn_dvsr=greatest_common_divisor(self.__numerator,self.__denominator)
        self.__numerator=self.__numerator//grtst_cmn_dvsr
        self.__denominator=self.__denominator//grtst_cmn_dvsr
        return self.__str__()
    def  complement(self):
        if self.__numerator * self.__denominator < 0:
            complement_object = Fraction(abs(self.__numerator), abs(self.__denominator))
        else:
            complement_object = Fraction(-1 * self.__numerator, self.__denominator)
        return complement_object
    def reciprocal(self):
        reciprocal_object = Fraction(self.__denominator, self.__numerator)
        return reciprocal_object
    def multiply(self, fraction_object):
        num = self.__numerator * fraction_object.__numerator
        dnum = self.__denominator * fraction_object.__denominator
        product_of_fractions = Fraction(num, dnum)
        return product_of_fractions
    def divide(self, fraction_object):
        num = self.__numerator * fraction_object.__denominator
        dnum = self.__denominator * fraction_object.__numerator
        division_of_fractions = Fraction(num, dnum)
        return division_of_fractions

    def add(self, fraction_object):
        n = (self.__numerator * fraction_object.__denominator) + \
            (self.__denominator * fraction_object.__numerator)
        d = self.__denominator * fraction_object.__denominator
        addition_of_fractions = Fraction(n, d)
        return addition_of_fractions

    def deduct(self, fraction_object):
        n = (self.__numerator * fraction_object.__denominator) - \
            (self.__denominator * fraction_object.__numerator)
        d = self.__denominator * fraction_object.__denominator
        subtraction_of_fractions = Fraction(n, d)
        return subtraction_of_fractions
    def __lt__(self, other):
        return self.__numerator/self.__denominator < other.__numerator/other.__denominator

    def __gt__(self, other):
        return self.__numerator/self.__denominator > other.__numerator/other.__denominator

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"




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
    '''Making list from class objects'''


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


if __name__ == "__main__":
    main()
