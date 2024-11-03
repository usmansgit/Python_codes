'''def probability_cal(T,D):
    T=int(T)
    D=int(D)
    T_fac=1
    D_fac=1
    for i in range(1,T+1):
        T_fac=T_fac*i
        print(T_fac)
    for j in range(1,D+1):
        D_fac=D_fac*j
        print(D_fac)'''

def read_input(x):
    num = int(input(x))
    if num<1:
        print("The number of balls must be a positive number.")
    else:
        return num


def main():
    '''This function call all the inputs'''
    total = read_input("Enter the total number of lottery balls: ")
    drawn = read_input("Enter the number of the drawn balls:")

    #read_input(inballs,drawn_balls)
    probability_cal(total, drawn)


if __name__ == "__main__":
    main()