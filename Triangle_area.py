"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt
def area(line1,line2,line3):
    '''This function calculates the area of a triangle'''
    a=float(line1)
    b=float(line2)
    c=float(line3)
    if a >=1 and b >=1 and c >=1:
        s=(a+b+c)/2
        A=sqrt(s*(s-a)*(s-b)*(s-c))
        return A


def main():
    line1 = input("Enter the length of the first side: ")
    line2 = input("Enter the length of the second side: ")
    line3 = input("Enter the length of the third side: ")

    print(f"The triangle's area is {area(line1,line2,line3):.1f}")


if __name__ == "__main__":
    main()
