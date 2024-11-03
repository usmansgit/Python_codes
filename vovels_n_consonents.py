'''This program is written by Muhammad Usman. It check the number of vovals in a word'''
def main():
    word= input("Enter a word: ")
    vovl=0
    consonent=0
    for i in range(len(word)):
        if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u' or word[i]=='y':
            vovl=vovl+1
        else:
            consonent=consonent+1
    print(f"The word \"{word}\" contains {vovl} vowels and {consonent} consonants.")
if __name__ == "__main__":
    main()