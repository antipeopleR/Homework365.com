
import random as r
class Human:

    HEALTH_BY_DEFAULT = 100

    def __init__(self, name, age, money, scale):
        self.name = name
        self.age = age
        self.money = money
        self.scale = scale
        self.health = self.HEALTH_BY_DEFAULT

class Work:

    SLESAR = "slesar"
    STROITEL = "stroitel"
    SOBYTILNIK = "sobytilnik"
    BABOCHKA = "babochka"

    def __init__(self, obj):
        if  obj.scale[0] >= 90:
          obj.WORK_AS[0] = self.slesar
        if  obj.scale[0] >= 60:
          obj.WORK_AS[0] = self.stroitel
        if  obj.scale[0] >= 30:
          obj.WORK_AS[0] = self.sobytilnik
        if  obj.scale[0] >= 0:
          obj.WORK_AS[0] = self.babochka

michael = Human("Michael", 23, r.randint(100,10000), r.randint(0,100))