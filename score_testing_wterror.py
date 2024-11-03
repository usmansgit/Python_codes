
"""
COMP.CS.100 Programming 1

program by Muhammad Usman, Program prints the calculated scores of the players in alphabaticl order.

"""
def main():
    """
    input file name, open a file
    ordering the players name alphetically
    sum of the scores of players
    :param:
    :return:
    """
    filename = input('Enter the name of the score file: ')
    #print('Contestant score:')
    try:
        player_file = open(filename, 'r')
    except OSError:
        print("There was an error in reading the file.")
        return
    file_lines_list = player_file.readlines()
    #print(file_lines_list)

    dict1 = {}
    for line in sorted(file_lines_list):
        line = line.rstrip()
        if len(line.split()) != 2:
            print(f"There was an erroneous line in the file:\n{line}")
            return
        key,value= line.split(' ')
        try:
            value = int(value)
        except ValueError:
            print(f"There was an erroneous score in the file:\n{value}")
            return
        if key in dict1:
            dict1[key].append(int(value))
        if key not in dict1:
            dict1[key]=[int(value)]
    for player in (dict1):
        print(f'{player} {sum(dict1[player])}')

    player_file.close()
if __name__ == '__main__':
    main()
