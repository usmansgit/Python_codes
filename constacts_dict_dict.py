'''This program prints the dictionary of contacts
'''
def read_file(filename,name,detail):
    """
    Reads and saves the series and their genres from the file.

    param:filename
    return dict
    """
    reviews = dict()
    try:
        fhandle = open(filename, mode="r")
        for line in fhandle:
            words = line.split(';')
            reviews.update({words[0]: dict()})
            n = len(words)
            for i in range(1, n - 1, 2):
                if words[0] in reviews.keys():
                    reviews[words[0]].update({words[i]: words[i + 1]})
        #print(reviews)
        return reviews
        # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename=input("enter name: ")
    name=input("enter name: ")
    detail=input("Enter detail: ")
    dict1=read_file(filename, name, detail)
    print(dict1.values())

if __name__ == "__main__":
        main()
