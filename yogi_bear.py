"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""
def repeat_name(name,repetition):
    '''This function do the repetition'''
    x=str(name)
    y=int(repetition)
    print(f"{x}, {x} Bear\n"*y, end="")

def verse(lyrics,name):
    '''This function print the lyrics'''
    words= str(lyrics)
    x=str(name)
    print(F"{words}")
    print(F"{x}, {x}")
    print(F"{words}")
    repeat_name(x, 3)
    print(F"{words}")
    repeat_name(x,1)

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()