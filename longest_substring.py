'''This program prints the longest substring'''
def longest_substring_in_order(x):
    '''This function prints the longest substring in string'''
    s = x
    r = ''
    c = ''
    for char in s:
        if (c == ''):
            c = char
        elif (c[-1] <= char):
            c += char
        elif (c[-1] > char):
            if (len(r) < len(c)):
                r = c
                c = char
            else:
                c = char
    if (len(c) > len(r)):
        r = c
    #print(r)
    return r

def main():
    longest_substring_in_order("")
if __name__ == "__main__":
    main()