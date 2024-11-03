def main():
    input_1 = input("Player 1, enter your choice (R/P/S): ")
    input_2 = input("Player 2, enter your choice (R/P/S): ")
    if input_1 == input_2:
        print("It's a tie!")
    elif input_1 == "P" and input_2 == "R":
        print("Player 1 won!")
    elif input_1 == "R" and input_2 == "S":
        print("Player 1 won!")
    elif input_1 == "S" and input_2 == "P":
        print("Player 1 won!")
    else:
        print("Player 2 won!")
if __name__ == "__main__":
        main()