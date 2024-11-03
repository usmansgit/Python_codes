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
    num=int(input(x))
    while num < 1:
        num = int(input(x))
    return num
def main():
    '''This function call all the inputs'''
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
