def read_friendship_network(filename):
    dicts = {}
    network=[]
    try:
        file = open(filename, mode="r")
        file = file.readlines()
        #print(file)
        for line in file:
            line = line.rstrip()
            if len(line) > 0 and line[0] == "#":
                continue
            fields = line.split(";")
            print(fields)
            #print(type(fields))
            if len(fields) < 2:
                print(f"Fatal Error: line '{line}' has too few fields.")
                return None

            for name in fields:
                if not name.isalpha():
                    print(f"Fatal Error: '{name}' is not a valid name.")
                    return None
            who = fields[0]

            friend=fields[1:]
            #print(friend)
            dicts[who] = friend
            #print(dicts)
            network.append(dicts)


            #for friend in fields[1:]:
             #   print()

        print(network)
        return network

    except OSError:
        print(f"Fatal Error: opening '{filename}' failed.")
        return None
def add_friendship(network, name1, name2):
    print(network)

    for name in [ name1, name2 ]:
        if not name.isalpha():
            print("Error: '{name}' is not a valid name: friendship not added.")
            return
        if name1 == name2:
            continue

    # TODO: Add information about <name1> being <name2>'s friend and
    #       <name2> being <name1>'s friend into the parameter data
    #       structure <network>.  Note: if <name1> and <name2> are
    #       already known to be friends, nothing needs to be done.

def main():
    filename=("ftest.txt")
    read_friendship_network(filename)
if __name__ == "__main__":
    main()




