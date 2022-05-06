import random as r
class Chelovek:
    
    HEALTH_BY_DEFAULT = 100

    def __init__(self, age, name, money):
        self.money = money ,
        self.age = age ,
        self.name = name ,
        self.health = self.HEALTH_BY_DEFAULT  ,

    def vivod(self):
        print(f"[ЖИЗНЬ ПРОЖИТА] : {self.age}")
        print(f"[УКРАДЕННЫЕ ДЕНЬГИ] : {self.money}")

    def day(self):
        self.money -= 10
        self.health -= 10,
    
    def logistic(self):
        if self.health < 0 or self.money < 0:
            print("Ты или сдох или стал бомжом. ПОЗДРАВЛЯЮ!!!")

michael = Chelovek("Michael", 45, r.randint(100,10000))

michael.vivod()