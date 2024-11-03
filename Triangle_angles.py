'''This function is written by Muhammad Usman it calculates the angles of triangle'''
def calculate_angle(x,y=90):
    '''This function calculates the missing angle of the triangle'''
    x=int(x)
    y=int(y)
    z=180-(x+y)
    print(y)
    return z
def main():
    calculate_angle(30,60)


if __name__ == "__main__":
    main()
