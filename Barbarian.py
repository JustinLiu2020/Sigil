#!/usr/bin/bash python3

import random 
import sys 
#from IPython import embed


class Barbarian:
    def __init__(self, name, p):
        self.name = name
        self.p = p
        self.alive = True

    def attack(self, obj):
        r = random.random()
        if r < self.p:
            dprint("{} is dead!\n".format(obj.name))
            obj.alive = False
        else:
            dprint("{} is still alive!\n".format(obj.name))
            None



class Sim():
    def __init__(self, pa, pb, pc, priority="B"):
        self.A = Barbarian("Alex", pa)
        self.B = Barbarian("Bob", pb)
        self.C = Barbarian("Chris", pc)
        self.priority = priority
        self.winner = None


    def simA_B_First(self):
        if self.A.alive == False:
            dprint("{} Dead!\n".format(self.A.name))
        elif self.B.alive:
            dprint("{} attacks {}!\n".format(self.A.name, self.B.name))
            self.A.attack(self.B)
            if self.B.alive:
                self.simB()
            elif self.C.alive:
                self.simC()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.A.name))
                self.winner = self.A
        elif self.C.alive:
            dprint("{} attacks {}!\n".format(self.A.name, self.C.name))
            self.A.attack(self.C)
            if self.C.alive:
                self.simC()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.A.name))
                self.winner = self.A
        else:
            dprint("All enimies are dead! A win!\n")
            self.winner = self.A


    def simA_C_First(self):
        if self.A.alive == False:
            dprint("{} Dead!\n".format(self.A.name))
        elif self.C.alive:
            dprint("{} attacks {}!\n".format(self.A.name, self.C.name))
            self.A.attack(self.C)
            if self.B.alive:
                self.simB()
            elif self.C.alive:
                self.simC()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.A.name))
                self.winner = self.A
        elif self.B.alive:
            dprint("{} attacks {}!\n".format(self.A.name, self.B.name))
            self.A.attack(self.B)
            if self.B.alive:
                self.simB()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.A.name))
                self.winner = self.A
        else:
            dprint("All enimies are dead! {} win!\n".format(self.A.name))
            self.winner = self.A

    def simA(self):
        if self.priority == "A->B":
            self.simA_B_First()
        elif self.priority == "A->C":
            self.simA_C_First()
        elif self.priority == "Shoot the air":
            if self.B.alive and self.C.alive:
                dprint("{} shoots the air as both {} and {} are alive!\n".format(self.A.name, self.B.name, self.C.name))
                self.simB()
            elif self.priority == "Shoot the air" and self.B.alive :
                self.simA_B_First()
            elif self.priority == "Shoot the air" and self.C.alive :
                self.simA_C_First()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.A.name))
                self.winner = self.A
        else:
            dprint("Unknown priority {}\n".format( self.priority))
    
    def simB(self):
        if self.B.alive == False:
            dprint("{} Dead!\n".format(self.B.name))
        elif self.C.alive:
            dprint("{} attacks {}!\n".format(self.B.name, self.C.name))
            self.B.attack(self.C)
            if self.C.alive:
                self.simC()
            elif self.A.alive:
                self.simA()
        elif self.A.alive:
            dprint("{} attacks {}!\n".format(self.B.name, self.A.name))
            self.B.attack(self.A)
            if self.A.alive:
                self.simA()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.B.name))
                self.winner = self.B
        else:
            dprint("All enimies are dead! {} win!\n".format(self.B.name))
            self.winner = self.B
    
    def simC(self):
        if self.C.alive == False:
            dprint("{} Dead!\n".format(self.C.name))
        elif self.B.alive and self.A.alive:
            dprint("{} attack {}!\n".format(self.C.name, self.B.name))
            self.C.attack(self.B)
            self.simA()
        elif self.A.alive:
            dprint("{} attack {}!\n".format(self.C.name, self.A.name))
            self.C.attack(self.A)
            if self.A.alive:
                self.simA()
            else:
                dprint("All enimies are dead! {} win!\n".format(self.C.name))
                self.winner = self.C
        else:
            dprint("All enimies are dead! {} win!\n".format(self.C.name))
            self.winner = self.C
    
    
def cal(mode, total):
    A_LIVE_COUNT = 0
    B_LIVE_COUNT = 0
    C_LIVE_COUNT = 0
    UNKNOWN_LIVE_COUNT = 0
    for i in range(0, total):
        dprint("============================\n")
        if mode == "A->B":
            s = Sim(0.2, 0.5, 0.8, "A->B")
            s.simA_B_First()
        elif mode == "A->C":
            s = Sim(0.2, 0.5, 0.8, "A->C")
            s.simA_C_First()
        elif mode == "Shoot the air":
            s = Sim(0.2, 0.5, 0.8, "Shoot the air")
            dprint("{} shoots the air as both {} and {} are alive!\n".format(s.A.name, s.B.name, s.C.name))
            s.simB()
        else:
            dprint("Unknown mode\n")
            None
        if s.winner == s.A:
            A_LIVE_COUNT += 1
        elif s.winner == s.B:
            B_LIVE_COUNT += 1
        elif s.winner == s.C:
            C_LIVE_COUNT += 1
        else:
            UNKNOWN_LIVE_COUNT += 1
    return {"A prob":"{}%".format(A_LIVE_COUNT*100/total),
            "B prob":"{}%".format(B_LIVE_COUNT*100/total),
            "C prob":"{}%".format(C_LIVE_COUNT*100/total),
            "UNKNOWN prob":"{}%".format(UNKNOWN_LIVE_COUNT*100/total)}


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def dprint(*args):
    if DEBUG == True:
        print(*args)
    else:
        None

if __name__ == "__main__":
    DEBUG = False
    #DEBUG = False
    totalNum = int(sys.argv[1])
    PROB = {"A->B":None, "A->C":None, "Shoot the air":None,}
    for m in PROB.keys():
        PROB[m] = cal(m, totalNum)
    pretty(PROB, 1)
