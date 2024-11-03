"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""
def print_verse(animal,vocal):
    ''' This function print the repetative verse witth the animal'''
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {vocal} {vocal} here")
    print(f"And a {vocal} {vocal} there")
    print(f"Here a {vocal}, there a {vocal}")
    print(f"Everywhere a {vocal} {vocal}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")



if __name__ == "__main__":
    main()
