"""
        This program is written by Muhammad Usman, It fix the spacing between print outs.
        """
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            K=i*j
            print(f"{K:4}",end="")
        print()

if __name__ == "__main__":
    main()
