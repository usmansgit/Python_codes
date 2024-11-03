"""
       This program is written by Muhammad Usman.It print's the dates in a leap year
       """
def main():
    counter=0
    for i in range (1, 13):
        if (i== 12) or(i==1) or (i==3) or (i==5) or (i==7) or (i==8) or (i==10):
            days=32
        elif (i==4) or (i==6) or (i==9) or (i==11) or (i==9):
            days=31
        elif i==2:
            days=29
        for j in range (1, days):
            counter +=1
            if counter in range (3,365,7):
                #print("counter",counter)
                print(j,".",i,".",sep="")
if __name__ == "__main__":
    main()