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


class SuperHero(Hero):
    """"Super hero class"""
    def __init__(self, name, level, race, magic):
        """"iniciate a superhero"""
        super().__init__(name, level, race)
        self.magic = magic
        self.magicLevel = 100

    def makeMagic(self):
        """"decrease magic level"""
        self.magicLevel -= 10

    def show_super_hero(self):
        description = (self.name + " Hero level is: " + str(self.level) + "\t Race is: " + self.race + "\tHealth is: " + str(self.health) + "\tThis hero make magic: " + self.magic + "\tLevel magic energy: " + str(self.magicLevel))
        print(description)

myhero = Hero("Elex", 5, "Vampire")
myhero2 = Hero("Andryu", 1, "Human")
myhero3 = SuperHero("Oleg", 2, "Orc", "fly")

myhero.show_hero()
myhero2.show_hero()
myhero2.move()
myhero.level_up()
myhero3.show_super_hero()
myhero3.makeMagic()
myhero3.show_super_hero()

