'''Claculates the players points'''

class Player:
    """
    This class create a variable of Player class
    """

    def __init__(self, player_name, points=0):
        self.player = player_name
        self.points = points
        self.points_log = []
        self.points_for_percentage = []

    def get_name(self):
        return self.player

    def get_points(self):
        return self.points

    def has_won(self):
        if self.points == 50:
            return True
        else:
            return False

    def add_points(self, points):
        self.points += points

        if 40 <= self.points <= 49:
            print(f"{self.player} needs only {50-self.points} points. "
                  f"It's better to avoid knocking down the pins with higher points.")

        if self.points > 50:
            print(f"{self.player} gets penalty points!")
            self.points = 25

    def calculate_average(self, points):
        if points > 0:
            self.points_for_percentage.append(points)

        self.points_log.append(points)
        return sum(self.points_log)/len(self.points_log)

    def calculate_percentage(self):
        if len(self.points_for_percentage) > 0:
            return (len(self.points_for_percentage)/len(self.points_log))*100
        else:
            return 0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if pts > in_turn.calculate_average(pts):
            print("Cheers " + in_turn.get_name() + "!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.calculate_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.calculate_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
