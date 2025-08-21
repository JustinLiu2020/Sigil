import random
import time

def manageSpells(move, mp):
    move = move.lower()
    dmg = 0
    effect = None
    target = "E"
    cost = 0
    
    if move == "cinder":
        print("Your enemy has been set on fire.")
        dmg = mp
        effect = "burn"
    elif move == "heal":
        print("You feel an ethereal power flying through your arteries, and resting at your heart.")
        print(f"You've healed {round(cost / 2)} hp!")
        dmg = -round(cost / 2)
        target = "U"
    elif move == "buff":
        print("You buff up your attack!")
        dmg = mp
    elif move == "freeze":
        print("A beam of liquid nitrogen shoots from your hand and freezes the air around the enemy!")
        effect = "freeze"
        
    return dmg, effect, target

def ask(allowedInputs):
    question = ""
    for i in range(len(allowedInputs)):
        question += f"({i + 1}) {allowedInputs[i]}\n" #E.G 1. Attack
    while True:
        try:
            answer = int(input(question))
            if answer <= len(allowedInputs) and answer > 0:
                break
            else:
                print("Your value was out of bounds. Please enter a valid value.")
        except ValueError:
            print("Please enter an integer.")
    return allowedInputs[answer - 1]

def battle(name, ename, edesc, maxhp, emaxhp, cdf, ecdf, cpow, ecpow, maxmp, emaxmp, cspeed, ecspeed, spells, espells, items, eitems, etaunts):
    turn = 0
    hp = maxhp
    ehp = emaxhp
    mp = maxmp
    emp = emaxmp
    pow = cpow
    epow = ecpow
    df = cdf
    edf = ecdf
    speed = cspeed
    ecspeed = ecspeed
    vowels = ["a", "e", 'i', 'o', 'u']
    numToMove = ["head", "chest", "flank", "low"]
    parry = {
        "head" : {
            "wins" : ["head"],
            "draw" : ["chest", "flank"],
            "lose" : ["low"]
        },
        "chest" : {
            "wins" : ["chest"],
            "draw" : ["head", "low"],
            "lose" : ["flank"]
        },
        "flank" : {
            "wins" : ["flank"],
            "draw" : ["head", "low"],
            "lose" : ["chest"]
        },
        "low" : {
            "wins" : ["low"],
            "draw" : ["chest", "flank"],
            "lose" : ["head"]
        }
    }
    turn = 0
    runaway = False
    if ename[0] not in vowels:
        print(f"You've encountered a {ename}!")
    else:
        print(f"You've encountered an {ename}!")
    print(edesc)
    timer = {}
    while not hp <= 0 and not ehp <= 0 and not runaway:
        if turn % 2 == 0:
            print(f"HP: {hp}/{maxhp}\nMP: {mp}/{maxmp}")
            print(f"Enemy HP: {ehp}/{emaxhp}\nEnemy MP: {emp}/{emaxmp}")
            #move = input("Do you attack, cast a spell, use an item, or say something?")
            move = ask(["Attack", "Spell", "Item", "Taunt", "Flee"])
            dmg = 0
            if move.lower() == "attack":
                #move = ask([1, 2, 3, 4], "Do you attack head (1), chest (2), flank (3) or low (4)?", "Please enter a number between 1 and 4 inclusively.")
                print("Which line do you attack from?")
                move = ask(["head", "chest", "flank", "low"])
                enemyMove = random.choice(["head", "chest", "flank", "low"])
                dmg = int(max(3, pow * random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) - edf) + random.uniform(-3.9, 4.0))
                print(f"{ename} parries {enemyMove}")
                if move.lower() in parry[enemyMove]["wins"]:
                    print(f"{ename} parries your attack!")
                    dmg = 0
                elif move.lower() in parry[enemyMove]["draw"]:
                    if random.randint(0, 1) == 1:
                        print("Your blades clash, but your attack slips through!")
                        dmg = dmg/2
                        print(f"You dealt {dmg} damage!")
                    else:
                        print(f"{ename} deflects your blade to the side and backs away!")
                else:
                    print(f"{ename} just outright has a skill issue and gets hit.")
                    print(f"You dealt {dmg} damage!")
            elif move.lower() == "spell":
                print("\n Pick a spell:")
                move = ask(spells)
                move = move.lower()
                if move in spells:
                    dmg, effect, target = manageSpells(move, int(input(f"How much mp do you spend? You have {mp} mp left.")))
                    if move == "heal":
                        hp += round(mp/2)
                    if move == "buff":
                        pow += round(mp/2)
                        timer["1buff"] = 3
                else:
                    print(f"You try and utter the spell of {move}, but it doesn't work, as you are too braindead to know it!")
                if effect == "burn":
                    print(f"Flames burst from within {ename}! They have been inflicted with the burn status effect!")
                if effect == "freeze":
                    print(f"{ename} has inflicted with freeze status effect!")
                    turn -= 1
            elif move.lower() == "item":
                pass
            elif move.lower() == "taunt":
                move = input("What do you say?")
                print(move)
            else:
                print("We will roll a die to determine if you successfully flee or not.\nRolling higher than 5 allows you to successfully flee.")
                move = int(random.randint(1, 20) + cspeed/20 - ecspeed/20)
                print(f"You roll a {move} (Adding on your speed and the enemy's speed).")
                if move > 5:
                    print(f"You have successfully fled!")
                    runaway = True
                else:
                    print(f"The enemy stops you and cuts you down!")
                    hp -= int(max(3, epow * random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) - df) + random.uniform(-3.9, 4.0))
                    
            turn += 1
            if mp <= maxmp:        
                mp += min(maxmp - mp, round(maxmp / 10))
            ehp -= dmg
            time.sleep(1)
        else:
            if ((hp > 1.1 * pow - df + 4)) and random.randint(0, 9) > 8:
                #The enemy attacks!
                print("The enemy attacks! Pick a direction to parry:")
                move = ask(["head", "chest", "flank", "low"])
                enemyMove = random.choice(["head", "chest", "flank", "low"])
                print(f"You parry {move}!")
                print(f"The enemy attacks {enemyMove}")
                dmg = int(max(3, epow * random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) - df) + random.uniform(-3.9, 4.0))
                if enemyMove.lower() in parry[move]["wins"]:
                    print(f"You parry successfully!")
                    dmg = 0
                elif enemyMove.lower() in parry[move]["draw"]:
                    if random.randint(0, 1) == 1:
                        print(f"Your blades clash, but {ename}'s attack slips through!")
                        print(f"{ename} deals {dmg} damage!")
                        dmg = dmg/2
                    else:
                        print(f"You deflect the blade to the side and backflip away!")
                        dmg = 0
                else:
                    print(f"You just got hit.")
                hp -= dmg
            else:
                if not ((hp > 1.1 * pow - df + 4)):
                    if mp > 2 * (20 - hp):
                        enemyMove = random.randint(36 - hp, 26 - hp)
                        print(f"Red streams of particles unbind themselves from the ground and fly towards {ename}! They have regained {enemyMove / 2} hp!")
                if ehp > hp + 20:
                    print(etaunts[random.randrange(0, len(etaunts))])
            emp += min(2, emaxmp - emp)
            turn += 1
            time.sleep(1)
    if runaway:
        print("You coward. Are you proud of yourself?")
    elif hp < 1:
        print("You died!")
    else:
        print("You defeated the enemy!")
battle("Justin", "Anna", "An angry and annoying sister", 100, 100, 10, 10, 20, 30, 50, 50, 80, 60, ["cinder", "freeze", "heal"], ["buff", "freeze", "heal"], {"flashbang": {"desc": "Stuns for one frame", "type": "escape", "amount": None}, "fairy": {}}, ["bazooka", "boomerang"], ["Anna stands atop a rock and points her sword at you. 'So weak.' "])


