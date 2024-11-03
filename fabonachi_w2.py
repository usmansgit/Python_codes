"""
        This program is written by Muhammad Usman, prints out fabonachi numbers.
        """
def main():
    numbers = int(input("How many Fibonacci numbers do you want? "))
    count = 1
    pre_feb = 0
    present_feb = 1
    if numbers <= 0:
        print("0.",pre_feb)
    elif numbers <= 1:
        print("1.",present_feb)
    else:
        while count < numbers+1:
            print(count,".",sep="",end="")
            print("",present_feb)
            next_feb = pre_feb +present_feb
            pre_feb = present_feb
            present_feb = next_feb
            count += 1
if __name__ == "__main__":
    main()