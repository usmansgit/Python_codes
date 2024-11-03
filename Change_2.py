def main():
    price = input("Purchase price: ")
    paid = input("Paid amount of money: ")
    price = int(price)
    paid = int(paid)
    change = paid -price
    ten = change//10
    five = (change%10)//5
    two = ((change%10)%5)//2
    one = (((change%10)%5)%2)//1

    if change > 0:
       print("Offer change:")
       if ten >= 1:
           print(ten,"ten-euro notes")
       if five >=1:
           print(five,"five-euro notes")
       if two >= 1:
           print(two,"two-euro coins")
       if one >= 1:
           print(one,"one-euro coins")

    else:
        print("No change")



if __name__ == "__main__":
    main()