'''This program is written by muhammad usman. I calculates the probability of jackpot'''
def fact(num):
    '''This function calculates the factorial'''
    factorial_1=int(1)
    for balls in range(1,num+1):
        factorial_1=factorial_1*balls
        #print(factorial_1)
    return factorial_1
def foo():
    '''This function calculates the probability'''
    total_b=int(input("Enter the total number of lottery balls: "))
    drawn_b=int(input("Enter the number of the drawn balls: "))
    den=total_b-drawn_b
    if total_b<0 and drawn_b>0:
        print("The number of balls must be a positive number.")
    elif total_b<drawn_b and not total_b < 0:
        print("At most the total number of balls can be drawn.")
    elif total_b>1 and total_b>drawn_b:

        prob = fact(total_b)/(fact(den)*fact(drawn_b))
        print(f"The probability of guessing all {drawn_b} balls correctly is 1/{int(prob)}")



def main():
   '''This function prints the probability'''
   foo()
if __name__ == "__main__":
    main()