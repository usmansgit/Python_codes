'''This program is written by Muhammad USman. It goes through the elements of a list'''
def main():
    list=[]
    print("Give 5 numbers:")
    for i in range(5):
        num = int(input("Next number: "))
        list.append(num)
    print("The numbers you entered, in reverse order:")

    for j in reversed(list):
        print(j)

if __name__ == "__main__":
    main()