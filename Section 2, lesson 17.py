class Hero():
    """Class to create of hero"""
    def __init__(self, name, level, race):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        description  = (self.name + " Hero level is: " + str(self.level) + "\t Race is: " + self.race + "\tHealth is: " + str(self.health))
        print(description)

    def level_up(self):
        """Hero level up"""
        self.level += 1

    def move(self):
        """Start moving"""
        print("Hero " + self.name + " start moving")

myhero = Hero("Elex", 5, "Vampire")
myhero2 = Hero("Andryu", 1, "Human")
myhero3 = Hero("Oleg", 2, "Orc")

myhero.show_hero()
myhero2.show_hero()
myhero2.move()
myhero.level_up()
myhero3.show_hero()

