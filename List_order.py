'''This program is written by muhammad usman it check if the entries in the list are in order'''
def is_the_list_in_order(entries):
    '''This function check if the list entries are in order'''
    list=[]
    for a in entries:
        list.append(a)
    list1=0
    list1=list[:]
    list1.sort()
    if list1==list:
        return True
    else:
        return False
def main():
    testlist=[1,2,3,4,5]
    print(is_the_list_in_order(testlist))
if __name__ == "__main__":
    main()