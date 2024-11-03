"""
       This program is written by muhammad usman and it gives zip boing and both
        until the number entered by user.
       """
def main():
    number = int(input("How many numbers would you like to have? "))
    repetition_counter = 1

    while repetition_counter <= number:

        if ((repetition_counter % 3) == 0) and ((repetition_counter % 7) == 0):
            print("zip boing")
        elif (repetition_counter%7) == 0:
            print("boing")
        elif (repetition_counter%3) == 0:
            print("zip")
        elif ((repetition_counter%3) != 0) and ((repetition_counter%7)!= 0):
            print(repetition_counter)


        repetition_counter += 1



if __name__ == "__main__":
    main()