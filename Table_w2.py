"""
       This program is written by muhammad usman and it displayes the table of a chosen number by the user
       """
def main():
    number = int(input("Choose a number: "))
    repetition_counter = 1
    product = 1
    while product <= 100:

        product = repetition_counter * number

        print(repetition_counter, "*", number,"=", product)
        repetition_counter += 1

if __name__ == "__main__":
    main()