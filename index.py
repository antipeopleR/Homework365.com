import random as r
class Pet:

    HEALTH_BY_DEFAULT = 100
    EMOTIONAL_HELTH_BY_DEFAULT = 100

    def __init__(self, age, food, emotion_health, health):
        self.age = age
        self.food = food
        self.emotion_health = self.EMOTIONAL_HELTH_BY_DEFAULT
        self.health = self.HEALTH_BY_DEFAULT

class Place:
    def __init__(self):
        x = r.randint(0,101)
        if x <= 20:
            self.emotion_health -= 40
            print(f"Вы родились в лесу : {self.EMOTIONAL_HELTH_BY_DEFAULT}")
        if x >= 21 and x <= 40:
            self.emotion_health -= 30
            print(f"Вы родились в селе : {self.EMOTIONAL_HELTH_BY_DEFAULT}")
        if x >= 41 and x <= 60:
            self.emotion_health -= 20
            print(f"Вы родились в деревне : {self.EMOTIONAL_HELTH_BY_DEFAULT}")
        if x >= 61 and x <= 80:
            self.emotion_health -= 10
            print(f"Вы родились в поселке городского типа (Блатного) : {self.EMOTIONAL_HELTH_BY_DEFAULT}")
        if x >= 81:
            print(f"Вы родились в селе : {self.EMOTIONAL_HELTH_BY_DEFAULT}")
            
class live_a_day:
    def __init__(self):
        x = r.randint(0,3)
        if self.food <= 0:
            self.health -= 30
        if self.health <= 0:
            print(f"Ваша жизнь окончена : {self.health}")
        self.food -= 10
        if x == 1:
            self.food -= 0
        if x == 2:
            self.food += 10
        if x == 3:
            self.food += 20


businka = Pet(r.randint(1,13), r.randint(1,100), 100, 100)
print(businka)