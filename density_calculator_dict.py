"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for pricelist assignment.
"""


def word_count():
    '''This function calculates the density of words in strings'''
    print("Enter rows of text for word counting. Empty row to quit.")
    counts = dict()
    while True:
        word=input()
        word=word.lower()
        #print(type(word))

        words = str.split(word)
        if word == "":
            break
        else:
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    #print(sorted(counts.items()))
    for keys, values in sorted(counts.items()):
        print(f"{keys} : {values} times")

def main():
    word_count()

if __name__ == "__main__":
    main()
