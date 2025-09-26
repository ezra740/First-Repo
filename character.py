class Character ():
    def _init_ (self):
        self.max_health = 100.0
        print("This is the Character Class")
        
    def retreat (self):
        print("Did the Hero just... ran away?")

class Enemy ():

    enem_stats = {"name" : "enemy", "strength": 5, "health": 100.0,}

    def _init_ (self):
        self.max_health = 100
        print("This is the Enemy Class")
        
        print("An Enemy has appeared")

    def attack (self):
        pass

    def take_damage(self,damage):
        self["health"] = self.max_health["health"] - damage
        print (f"The enemy has taken {self.stats['damage']}")
        print (f" The enemy's health is now {self.stats['health']}")

    def attack_hero():
        pass

