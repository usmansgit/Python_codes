"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    param:filename
    return dict
    """

    # TODO initialize a new data structure
    dict = {}
    s_name = set()
    s_genre = set()
    try:
        file = open(filename, mode="r")
        filelist = file.readlines()
        print(filelist)

        for row in filelist:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for w in sorted(genres):

                s_genre.add(w)

            s_name.add(name)

            if name not in dict:
                dict[name] = sorted(genres)


            # TODO add the name and genres data to the data structure
        file.close()

        # print(s_name)
        listToStr = ', '.join([str(elem) for elem in sorted(s_genre)])
        print(f'Available genres are: {listToStr}')
        # print(dict)

        return dict
        # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def finding_movie(dictionary, catagory):
    """
    using the genre name , it finds out movies under the given genre

    :param dictionary:
    :param catagory:
    :return: movie
    """
    movie = []
    for key, value in dictionary.items():
        # print('key', key)
        # print('value', value)""
        for v in value:
            if v == catagory:
                movie.append(key)

    return movie



def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    # print(genre_data)

    # TODO print the genres
    while True:
        genre = input("> ")
        # movies = finding movie(dictionary,catagory)
        movies = finding_movie(genre_data, genre)
        for x in sorted(movies):
            print(x)

        if genre == "exit":
            return
        # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()

