def main():
    price = input("Purchase price: ")
    paid = input("Paid amount of money: ")
    price = int(price)
    paid = int(paid)
    change = paid -price
    if change > 0:
       print("Offer change:")
       if change % 10 != 0:
           print(change // 10, "ten-euro faulty notes")
           ((change % 10) % 5)
           if ((change % 10) % 5) != 0:
               print(((change % 10) // 5), "five-euro notes")
               (((change % 10) % 5) % 2)
               if (((change % 10) % 5) % 2) != 0:
                   print((((change % 10) % 5) // 2), "two-euro coins")
                   print((((change % 10) % 5) % 2), "one-euro coins")
               else:
                   print((((change % 10) % 5) // 2), "two-euro coins")
           else:
               print(((change % 10) // 5), "five-euro notes")
       else:

           print(change // 10, "ten-euro notes")
    else:
        print("No change")



if __name__ == "__main__":
    main()