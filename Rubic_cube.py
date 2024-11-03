'''This program is written by Muhammad Usman. It prints out the average time taken to solve the rubic cube'''
def main():
    list=[]
    total=0
    for i in range(1,6):
        time=float(input(f"Enter the time for performance {i}: "))
        list.append(time)
    list.remove(min(list))
    list.remove(max(list))
    for ele in range(0, len(list)):
        total = total + list[ele]
    print(f"The official competition score is {total/len(list):.2f} seconds.")
    #print(list)
if __name__ == "__main__":
    main()