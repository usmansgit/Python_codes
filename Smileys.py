
def main():

    number = input("How do you feel? (1-10) ")
    number = int(number)

    if number >= 1 and number <= 10:

        if number == 1:
            print("A suitable smiley would be :'(")
        elif number < 4:

            print("A suitable smiley would be :-(")
        elif number <= 7:

            print("A suitable smiley would be :-|")
        elif number == 10:
            print("A suitable smiley would be :-D")

        else:

            print("A suitable smiley would be :-)")
    else:
        # Print an error message.
        print("Bad input!")

if __name__ == "__main__":
    main()