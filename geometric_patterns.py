"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""
from math import pi
def CirclePrint(p,q):
    '''This function prints the calculations'''
    print(f"The circumference is {p:.2f}")
    print(f"The surface area is {q:.2f}")
def Printing(x,y):
    '''This function prints the calculations'''
    print(f"The circumference is {x:.2f}")
    print(f"The surface area is {y:.2f}")
def read_input(x):
    '''This function make sure the input is positive '''
    num=float(input(x))
    while num < 1:
        num = float(input(x))
    return num

def square():
    '''This function make calculations for square'''
    sq_side=read_input("Enter the length of the square's side: ")
    circumference=4*sq_side
    area=sq_side*sq_side
    Printing(circumference,area)
    return circumference,area
def rectangle():
    '''This function make calculations for rectangle'''
    rec_side1=read_input("Enter the length of the rectangle's side 1: ")
    rec_side2 = read_input("Enter the length of the rectangle's side 2: ")
    rec_circum= (2*rec_side1)*(2*rec_side2)
    rec_area=rec_side1*rec_side2
    Printing(rec_circum,rec_area)
    return rec_circum,rec_area
def circle():
    '''This function make calculations for ciircle'''
    rad=read_input("Enter the circle's radius: ")
    cir_circum=4*pi*rad**2
    cir_area=pi*rad**2
    CirclePrint(cir_circum,cir_area)
    return cir_circum,cir_area

def menu():

    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()
            pass

        elif answer == "r":
            rectangle()
            pass
        elif answer == "c":
            circle()
            pass
        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
