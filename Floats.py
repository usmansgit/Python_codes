"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """
def compare_floats(val_1,val_2,EPSILON):
    """
    This function is written by Muhammad Usman
    First value need to compare:param val_1:
    second value need to compare:param val_2:
    absolute error compare to :param EPSILON:
    :return:
    """
    return abs (val_1-val_2)<EPSILON

def main():
    '''This function is written by Muhammad Usman
    First value need to compare:param val_1:
    second value need to compare:param val_2:
    absolute error compare to :param EPSILON:
    :return:'''
    #Val_1=float(input("Entre first value:"))
    #Val_2 = float(input("Entre second value:"))
    #print(20.0 - 0.1 - 19.9)

    compare_floats(0.00000000000000000001, 0.0000000000000000002, 0.000000001)
    

if __name__ == "__main__":
    main()