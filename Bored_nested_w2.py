"""
       This program is written by Muhammad Usman. It asks the user if they
       are board and keep asking until they say yes. when the user say yes
       then the program prints out (let's stop this then
       """
def main():

    word = ""

    # Read words while the word is not "quit".
    while (word != "Y") and (word != "y"):
        word = input("Bored? (y/n) ")
        if (word != "N") and (word != "n") and (word != "Y") and (word != "y"):
            print("Incorrect entry.")
        elif (word == "N") and (word == "n"):
            print()
    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()