import random as r
class Child:

    POWER_AT_DEFAULT = 5
    HEALTH_BY_DEFAULT = 100

    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = self.HEALTH_BY_DEFAULT
        self.power = self.POWER_AT_DEFAULT

    def get_name(self):
        return "Child name is" + str(self.name)

    def Power(self, power):
        x = r.randint(1,5)
        if x == 1:
            self.power += 10
            print(self.power)
        elif x == 2:
            self.power += 30
            print(self.power)
        elif x == 3:
            self.power += 60
            print(self.power)
        elif x == 4:
            self.power += 90
            print(self.power)
        else:
            self.power += 100
            print(self.power)

class Yunling (Child):
    def __init__(self, health, age, power):
        self.health += 50
        self.age += 5

    def Power(self, power):
        x = r.randint(1,5)
        if x == 1:
            self.power += 20
            print(self.power)
        elif x == 2:
            self.power += 50
            print(self.power)
        elif x == 3:
            self.power += 70
            print(self.power)
        elif x == 4:
            self.power += 100
            print(self.power)
        else:
            self.power += 120
            print(self.power)

class Jedi (Yunling):
    def __init__(self, age, skill, way, power, health):
        self.health += 130
        self.age += 13

    def Power(self, power):
        x = r.randint(1,5)
        if x == 1:
            self.power += 30
            print(self.power)
        elif x == 2:
            self.power += 60
            print(self.power)
        elif x == 3:
            self.power += 90
            print(self.power)
        elif x == 4:
            self.power += 120
            print(self.power)
        else:
            self.power += 150
            print(self.power)

    def way(self):
        x = r.randint(1,3)
        if x == 1:
            way = "protector"
            self.power += 200
            self.health += 150
            print(self.way)
            print(self.power)
            print(self.health)
        elif x == 2:
            way == "consular"
            self.power += 180
            self.health += 100
            print(self.way)
            print(self.power)
            print(self.health)
        else:
            way == "guardian"
            self.power += 150
            self.health += 130
            print(self.way)
            print(self.power)
            print(self.health)

child = Child("Robert Magne", 4, 100)
yunling = Yunling()
padawan = Jedi()