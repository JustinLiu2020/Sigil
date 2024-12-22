import random
from math import *
class Mob:
    def __init__(self, name, description, strength, defence, speed, accuracy, hp, maxhp, mp, maxmp, spelllist, boss):
        self.name = name
        self.description = description
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.accuracy = accuracy
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.spelllist = spelllist
        self.state = "neutral"
        self.boss = boss #Boolean: Is this mob a boss?
    def decide(self, targethp, targetmaxhp, targetmp, targetmaxmp, targetstrength, targetdefence, targetspeed, targetaccuracy):
        if self.hp < floor(targetstrength * 1.5) and self.speed < targetaccuracy and not targethp < floor(self.strength * 1.5) and not self.boss:
            return "run"
        elif self.mp > max(list(filter(lambda spell: spell["cost"] == "healing", self.spelllist))) and self.hp < targetstrength * 1.5:
            if self.hp < targetstrength * 0.5:
                return "spell" + max(
                    filter(lambda spell: spell["type"] == "healing", self.spelllist),
                    key=lambda spell: spell["amount"],
                    default=None  # Optional: handle empty lists gracefully
                )
        elif self.hp < targetstrength * 1.5 and targethp > self.strength * 1.5 and random.randint(0, 2) > 0:
            return "counter"
        else:
            if random.randint(0, 1) == 0:
                return "grab"
            else:
                return "attack"
            

        