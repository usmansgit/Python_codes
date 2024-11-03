"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""

# TODO: the definition of print_box goes here unless it goes after main.
def print_box(C,R,B_M='#',I_M=' '):
    '''This function prints the box according to width,height '''
    for i in range(1,R+1):
        for j in range(1,C+1):
            if (i==1 or i==R or j==1 or j==C):
                print(B_M,end='')
            else:
                print(I_M,end='')
        print()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(6,4,".", "O")


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
