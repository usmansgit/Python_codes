'''This program is written by Muhammad USman. It goes through the elements of a list'''
def main():
    list=[]
    print("Give 5 numbers:")
    for i in range(5):
        num = int(input("Next number: "))
        list.append(num)
    print("The numbers you entered that were greater than zero were:")
    #print(list)
    for j in list:
        if j>0:
            print(j)

if __name__ == "__main__":
    main()