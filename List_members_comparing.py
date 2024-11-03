'''This program is written by Muhammad Usman.It compares the elements of the lists'''
def are_all_members_same(entries):
   '''This function prints if the elements of a list are equal or not'''
   list=[]
   if entries==0:
       return entries
   for a in entries:
       list.append(a)
   if len(list)==0:
       return True
   else:
       result=list.count(list[0])==len(list)
   return result

def main():
    testlist=[1, 2, 2, 2, 2, 2, 2]
    print(are_all_members_same(testlist))

if __name__ == "__main__":
    main()