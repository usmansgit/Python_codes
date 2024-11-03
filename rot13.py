"""
COMP.CS.100 Programming 1
ROT13 program code template
Muhammad Umar Usman, muhammadumar.usman@tuni.fi
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13

    """
    regular_chars= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.isupper():
        text = text.casefold()
        text in regular_chars
        F = regular_chars.index(text)
        M = encrypted_chars[F]
        #print(M.upper())
        return M.upper()

    elif text.islower():

        text in regular_chars

        F=regular_chars.index(text)
        M=encrypted_chars[F]
        #print(M)
        return M

    else:
        #print(text)
        return text



    # TODO: implement encryption here

def row_encryption(sentence):
    """Encrypts its complete parameter using ROT13 encryption technology."""
    List=[]
    new_sen=list(sentence)

    for i in range(len(new_sen)):
        M=encrypt(new_sen[i])
        List.append(M)
    K="".join(List)
    return K
    #print(K)

def main():
    #encrypt("R")
    #encrypt("%")
    row_encryption("The quick brown fox jumps over the lazy dog.")
    row_encryption("e")


if __name__ == "__main__":

    main()