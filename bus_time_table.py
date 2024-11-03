"""
COMP.CS.100 Programming 1
Code template for "replacing grades" progra"""
def main():

    bus_time=[630,1015,1415,1620,1720,2000]
    #bus_time1=bus_time
    sum_time=bus_time+bus_time
    #del sum_time[-1]
    current_time=int(input("Enter the time (as an integer): "))
    index=0
    while index<len(bus_time):
        if current_time<= bus_time[index] or current_time >=2000:
            remaining_time=sum_time[index:index+3]
            print("The next buses leave:")
            print(*remaining_time,sep="\n")
            break
        index+=1

if __name__ == "__main__":
    main()