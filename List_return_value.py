'''This program is written by Muhammad USman. It check if the element exist in a list'''
def input_to_list():
    '''This function reads the input and output the number user wants to check'''
    list=[]
    
    numbers=int(input("How many numbers do you want to process: "))
    print(f"Enter {numbers} numbers:")

    while i<=numbers:
        val = int(input(''))
        list.append(val)
        i+=1
    #print(list)
    look_for=int(input("Enter the number to be searched: "))
    if look_for in list:
        print(f"{look_for} shows up {list.count(look_for)} times among the numbers you have entered.")
    else:
        print(f"{look_for} is not among the numbers you have entered.")

def main():

    input_to_list()
if __name__ == "__main__":
    main()