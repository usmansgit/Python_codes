
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
    print('Contestant score:')
    player_file = open(filename, 'r')
    file_lines_list = player_file.readlines()
    #print(file_lines_list)

    dict1 = {}
    for line in sorted(file_lines_list):
        line = line.rstrip()
        #print(line)
        key,value= line.split(' ')
        value = int(value)
        if key in dict1:
            dict1[key].append(int(value))
        if key not in dict1:
            dict1[key]=[int(value)]
    for player in (dict1):
        print(f'{player} {sum(dict1[player])}')

    player_file.close()
if __name__ == '__main__':
    main()
