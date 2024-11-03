'''This program is written by Muhammad Usman returns the acronym of a name'''
def capitalize_initial_letters(name):
    '''This function is written by Muhammad usman returns the acronym of a name'''
    name=name.lower()
    name=name.title()
    return name
def main():
    print(capitalize_initial_letters("drIVING cAR"))
if __name__ == "__main__":
    main()