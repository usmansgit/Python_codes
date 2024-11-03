"""
COMP.CS.100 Programming 1
Code template for "replacing grades" progra"""
def convert_grades(list):
    '''This function is written by Muhammad usman it changes the list index to six if its greater than o'''
    index=0
    while index<len(list):
        if list[index]>=1:
            list[index]=6
        index+=1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
