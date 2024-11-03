
class MovingBox:
    """
    A class for keeping track of the contents of
    a moving box. Items can be added to, removed from,
    itemized (i.e. listed), and searched from a moving box.
    The number of items in a box can also be queried
    and items can be transferred between two boxes.
    """

    def __init__(self, *args):
        self = dict()

    def add_item(self, key, value=[]):
        setattr(self, key, value)
        self.add_item = value

    ##################################################################
    #                                                                #
    #             YOUR CODE GOES HERE.                               #
    #                                                                #
    ##################################################################


##### DON'T CHANGE ANYTHING AFTER THIS LINE ##########################


def convert_str_to_int(word):
    """
    Converts the parameter string *word* in to an integer value.
    If conversion is successful returns the resulting integer.
    In the case of an error, returns None.

    :param (str) word: a word supposedly representing an integer value.
    :return: int | NoneType
    """
    try:
        result = int(word)
    except ValueError:
        return None

    return result


# NOTE!
# The following functions have a second parameter whose type is always
# a list containing strings, even in those cases when the list is empty.
# The reason for this is that the command interface
# in the main function was kept very simple: different commands
# require a different number of words of user input. The main function
# just stores all the extra words given after the actual command word in
# the user input line in single list without worrying
# if they are correct or not. This list is then passed as
# a parameter to the actual command functions below. It is their
# job to check that the words in the list makes sense in the context
# of the command in question.


def newbox(all_boxes, list_of_additional_info):
    """
    Creates a new moving box named after the first element in
    the parameter *list_of_additional_info*. The new box is stored
    in the dictionary *all_boxes* using the box's name as the key.
    If *all_boxes* already contains a box with the same name,
    it will be removed and replaced with the new box.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing a single element:
           the name of the moving box (str) to be created.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of initial data: can't create a new box.")
        return

    box_name = list_of_additional_info[0]
    all_boxes[box_name] = MovingBox(box_name)


def add_to_box(all_boxes, list_of_additional_info):
    """
    Adds a new item into a box stored in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is shown.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be added (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't add into a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't add to a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't add to a box.")
        return

    all_boxes[box_name].add_item(item_name, item_count)


def main():
    """
    In this project *main* function contains the top level
    part of the program's user interface.

    **Do not modify the main function in any way: the automated
    tests rely it to behave in a pre-defined way.**
    """
    boxes = {}

    while True:
        command_line = input("next command> ").strip()
        if command_line == "":
            break

        command_words = command_line.split()
        first_word = command_words[0]
        list_of_other_words = command_words[1:]

        if first_word == "quit":
            break

        elif first_word == "newbox":
            newbox(boxes, list_of_other_words)

        elif first_word == "add":
            add_to_box(boxes, list_of_other_words)

        else:
            print(f"Error: \"{first_word}\" is not a recognized command!")

if __name__ == "__main__":
    main()
