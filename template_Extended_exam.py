"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template.
"""

LOAN_TIME = 3
MAX_LOANS = 3

class Librarycard:
    def __init__(self, card_id, card_holder):
        self.__id = card_id
        self.__holder = card_holder

    def holder(self):
        return self.__holder

    def info(self):
        print("Card holder:", self.__holder)


class Library: 
    def __init__(self):
        self.bookings = []
        
    def read_card_data(self, file_name):
        card_data = {}

        try:
            file_object = open(file_name, mode="r")

            for line in file_object:
                line = line.strip()
                strings = line.split(";")

                card_id = int(strings[0])
                card_holder = strings[1]

                new_card = Librarycard(card_id, card_holder)

                card_data[card_id] = new_card

        except OSError:
            print("Error in reading the file")
            return None

        return card_data


    def read_card_id(self, prompt, database):
        while True:
            try:
                id = int(input(prompt))

                while id not in database:
                    print("Erroneous card id, existing id's are:")
                    listing(database)
                    id = int(input(prompt))

                return id

            except ValueError:
                print("Erroneous card id, existing id's are:")
                listing(database)


    def listing(self, cards):
        for card in sorted(cards):
            print(card, ":", cards[card].holder())
            #print("card holder loans")

    def return_fn(self, library, book):
        book = int(input(book))

        existing_booking, idx = self.get_booking(book)

        if (existing_booking == False):
            print(f"This book has not been borrowed by anyone")
            return
        
        del self.bookings[idx]
        print("Book returned")
        
        

    def get_booking(self, book):
        i=0
        for  booking in self.bookings:
            if (booking["book"]==book):
                return booking, i
            i += 1
        return False, -1

    def get_bookings(self, card):
        user_bookings = []
        for booking in self.bookings:
            if (booking["card"]==card):
                user_bookings.append([booking["book"], booking["weeks"]])
        
        return user_bookings

    def barrow(self, library,book,card):
        #adding modification to see if the book is already barrowed

        card = self.read_card_id(card, library)
        book = int(input(book))
        existing_booking, idx = self.get_booking(book)

        if (existing_booking != False):
            existing_card = existing_booking["card"]
            print(f"Customer {existing_card} {library[existing_card].holder()} has already borrowed book with id {book}")
            return

        if len(self.get_bookings(card)) < MAX_LOANS:
            booking = {
                "book": book,
                "card": card,
                "weeks": 3
            }
            self.bookings.append(booking)

            print(f"Loan successful, loan time 3 weeks")
            return 
            
        else:
            print(f"Card {card} has already 3 loans")
            print("Loan not successful")

    def aditional(self, library):

        #printing Additional information to command I
        card = self.read_card_id("Card code: ", library)
        card_bookings = self.get_bookings(card)
        print(f"Card holder: {library[card].holder()}")
        if len(card_bookings) == 0:
            print("- No loans")
        else:
            card_bookings.sort(key = lambda b: b[0])
            for i in card_bookings:
                print(f"- Loan {i[0]}, loan time left {i[1]} weeks")

    def new_week(self, library):
        i = 0
        for booking in self.bookings: 
            booking["weeks"] = 0 if booking["weeks"] == 0 else booking["weeks"] - 1
            bookings[i] = booking
            i+=1
        print("Loan times updated!")

def main():
    lib = Library()

    library = lib.read_card_data("library.txt")
    if library == None:
        return


    print("Welcome to Perähikiä library!")

    while True:
        command = input("Command: ")
        command = command.upper()

        if command == "I":
            lib.aditional(library)

        elif command == "L":
            lib.listing(library)

        elif command == "B":
            lib.barrow(library, "Book code: ", "Card code: ")


        elif command == "R":
            lib.return_fn(library, "Book code: ")
            pass

        elif command == "W":
            lib.new_week(library)
            pass

        elif command == "" or command == "Q":
            print("Thankyou and good bye!")
            return

        else:
            print("Erroneous command!")
            print("The commands are:")
            print("Info")
            print("List librarycards")
            print("Borrow")
            print("Return")
            print("new Week")


if __name__ == "__main__":
    main()
