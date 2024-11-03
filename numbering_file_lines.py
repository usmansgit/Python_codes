'''This program is by Muhammad Usman prints text with line numbers'''

def main():
    '''This prints the files with line numbers'''
    filename = input("Enter the name of the file: ")
    line_number=0
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
    for file_line in file:
        line_number = line_number+1
        print(f"{line_number} {file_line}",end='')
    file.close()


if __name__ == "__main__":
    main()