"""
COMP.CS.100 Programming 1
Template for task: box printing
"""
def print_box(width,height,mark):
    '''This function draw a box of height and width'''
    w=int(width)
    h=int(height)
    m=str(mark)
    i=1
    while i < h+1:
        print(m*(w))
        i +=1

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width,height,mark)


if __name__ == "__main__":
    main()
