"""
       This program is written by Muhammad Usman. It allows someone to follow the amount
       they jog in a certain time period.
       """



def main():
    days = int(input("Enter the number of days: "))
    jogging = []
    total = 0

    for i in range(1,days+1):
        x = float(input(f"Enter day {i} running length: "))
        jogging.append(x)

        for p in range(len(jogging) - 2):
            if jogging[p] == jogging[p+1 ] and jogging[p+1 ] == jogging[p + 2] and jogging[p + 2] == 0:
                print("\nYou had too many consecutive lazy days!")
                return

    for j in range(0, len(jogging)):
     total = total + jogging[j]
    average = total/len(jogging)

    if average < 3 and average > 0:
        print(f"\nYour running mean of {average:.2f} km was too low!")
    elif average >= 3:
        print(f"\nYou were persistent runner! With a mean of {average:.2f} km.")

if __name__ == "__main__":
    main()
