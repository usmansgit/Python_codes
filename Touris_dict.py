"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    sorting_value = sorted(english_spanish.items(), key=lambda k: k[0])
    print(", ".join(f"{keys}" for keys, value in sorting_value))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word=input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_add=input("Give the word to be added in English: ")
            sp_add=input("Give the word to be added in Spanish: ")
            english_spanish[eng_add] = sp_add
            print("Dictionary contents:")
            sorting_value = sorted(english_spanish.items(), key=lambda k: k[0])
            print(", ".join(f"{keys}" for keys, value in sorting_value))

        elif command == "R":
            word_to_remove = input("Give the word to be removed: ")
            if word_to_remove in english_spanish:
                del english_spanish[word_to_remove]
            else:
                print("The word", word_to_remove, "could not be found from the dictionary.")


        elif command == "Q":
            print("Adios!")
            return
        elif command == "P":
            print()
            print("English-Spanish")
            for keys, values in sorted(english_spanish.items()):
                print(f"{keys} {values}")

            print()
            print("Spanish-English")
            spanish_english = {v: k for k, v in english_spanish.items()}
            for keys, values in sorted(spanish_english.items()):
                print(f"{keys} {values}")
            # for i in english_spanish.items():
            # print(f"{sorted(english_spanish.values())} {english_spanish.keys()}")
            print()
        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")

            # joining the dict word found with the string
            phrase = " ".join([english_spanish.get(m, m) for m in sentence.split()])
            print(f"The text, translated by the dictionary: \n{phrase}")

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
