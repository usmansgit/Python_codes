'''This program is written by Muhammad Usman. It reverse the given names'''
def reverse_name(name):
    '''This function reverse the names given'''
    coma=","
    if coma not in name:
        return name
    f_name=name.split(",")
    if f_name[1].strip()=="" or f_name[0].strip()=="":
        f=(f"{f_name[1].strip()}{f_name[0].strip()}")
        return f
    else:
        n=(f"{f_name[1].strip()} {f_name[0].strip()}")
        return n


def main():
    print(reverse_name("von Grünbaumberger, Herbert"))
if __name__ == "__main__":
    main()