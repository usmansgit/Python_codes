"""
       This program is written by Muhammad Usman. It asks the user if they
       are board and keep asking until they say yes. when the user say yes
       then the program prints out (let's stop this then
       """
def main():

    word = ""

    # Read words while the word is not "quit".
    while (word != "Y") and (word!= "y") and (word!= "N") and (word!="n"):
        word = input("Answer Y or N: ")
        if (word != "Y") and (word!= "y") and (word!= "N") and (word!="n"):
            print("Incorrect entry.")
        else:
            print("You answered",word)


if __name__ == "__main__":
    main()