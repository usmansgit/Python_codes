'''This program is written by Muhammad Usman returns the acronym of a name'''
def create_an_acronym(name):
    '''This function is written by Muhammad usman returns the acronym of a name'''
    name=name.upper()
    name=name.split()
    ace=[]
    for i in range(len(name)):
        for j in name:
            ace.append(j[0])
        ac="".join(ace)
        return ac
def main():
    print(create_an_acronym("Muhammad Usman"))
if __name__ == "__main__":
    main()