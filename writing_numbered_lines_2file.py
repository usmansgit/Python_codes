"""
This program write input lines from the user and
writes then into a file with line numbers.
"""
def read_message():
    '''This function writes the user input with line numbers into a file'''
    filename = input(f"Enter the name of the file: ")
    line_number = 0

    try:
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    while True:
        line_number = line_number + 1
        text_line = input()

        if text_line == "":
            break

        print(line_number, text_line, file=save_file)

    save_file.close()

    print(f"File {filename} has been written.")


def main():
    read_message()


if __name__ == "__main__":
    main()