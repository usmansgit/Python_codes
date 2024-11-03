'''This program prints abbs the string'''
def count_abbas(x):
    '''This function is written by usman it prints the number of abbs in string'''
    count=0
    check=0
    while True:
        check=x.find('abba',check)+1
        if check > 0:
            count += 1
        else:
            return count

def main():
    count_abbas("abbabbabba")
if __name__ == "__main__":
    main()