def is_the_list_in_order(entries):
    '''This function check if the list entries are in order'''
    list=[]
    for a in entries:
        list.append(a)
    list1 = list[:]
    list1.sort()
    print(list1)
    if list1==list:
        return True
    else:
        return False
def main():
    testlist=[]
    print(is_the_list_in_order(testlist))
if __name__ == "__main__":
    main()