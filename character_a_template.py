"""
Name: Muhammad Usman
Email: muhammad.usman@tuni.fi

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.


"""

class Character:
    """Define various method
       and variable in Class
    """
    def __init__(self,name):
        self.__name= name
        self.__list=[]
        self.__no_of_item=0
        self.__countedItem={}
    def get_name(self):
        return self.__name


    def give_item(self,item):
        self.__list.append(item)

    def remove_item(self,del_item):
        return  self.__list.remove(del_item)
    def how_many(self,count_item):

        self.__no_of_item=self.__list.count(count_item)

        return self.__no_of_item

    def printout(self):
        print(f'Name: {self.__name}')
        if self.__list==[]:
            print('  --nothing--')
        else:


          for item in sorted(self.__list):
              self.__no_of_item = self.__list.count(item)

              self.__countedItem[item] = self.__no_of_item
          for keys in self.__countedItem:
              print(f'  {self.__countedItem[keys]} {keys}')



    def has_item(self,item):

        if item in self.__list:
            return True
        else:
            return False




def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()