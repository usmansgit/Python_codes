"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""
def print_box(w,h,i):
    '''This function prints the box according to width,height '''
    width=int(w)
    height=int(h)
    mark=str(i)
    for row_index in range(height):
        for row_index in range(width):
            print(mark, end='')
        print()
def read_input(x):
    '''This function reads all the inputs '''
    invalid_input = True

    # Read the length of the base while it is smaller than or equal to zero
    # or of a wrong type.
    while invalid_input:
        # Read an input.
        line = input(x)

        # Prepare for exceptions.
        try:
            # Convert the input into a floating point number. If the float
            # function raises an exception, it will be caught by the except
            # clause.
            base_length = int(line)

            # Flip the flag value to end the loop.
            if base_length > 0:
                invalid_input = False
                return base_length
            # Print the error message.
            else:
                print('', end='')
        # Print another error message.
        except ValueError:
            print('',end='')
def main():
    '''This function call all the inputs'''
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()