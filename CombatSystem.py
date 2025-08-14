import random

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
    parry = {
        "head" : {
            "wins" : ["head"],
            "draw" : ["chest", "flank"],
            "lose" : ["low"]
        },
        "chest" : {
            "wins" : [""],
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
    if ename[0] not in vowels:
        print(f"You've encountered a {ename}!")
    else:
        print(f"You've encountered an {ename}!")
    print(edesc)
    timer = {}
    while not hp <= 0 and not ehp <= 0:
        if turn % 2 == 0:
            move = input("Do you attack, cast a spell, use an item, or say something?")
            if move.lower() == "attack":
                move = input("Do you attack head, chest, flank or low?")
                enemyMove = random.choice(["head", "chest", "flank", "low"])
                dmg = int(max(3, pow * random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) - edf) + random.uniform(-3.9, 4.0))
                print(f"{ename} parries {enemyMove}")
                if move.lower() in parry[enemyMove]["wins"]:
                    print(f"{ename} parries your attack!")
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
                print(turn)
                ehp -= dmg
            elif move.lower() == "spell":
                move = input(f"Which spell? The spells you have are {spells}.")
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
        else:
            if random.randint(0, 10) <= 7:
                #The enemy attacks!
                move = input("The enemy attacks! Pick a direction to parry, head, chest, flank, or low.")
                enemyMove = random.choice(["head", "chest", "flank", "low"])
                print(f"You parry {move}!")
                print(f"The enemy attacks {enemyMove}")
                dmg = int(max(3, pow * random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) - edf) + random.randrange(-3.9, 4.0))
                if move.lower() in parry[move]["wins"]:
                    print(f"You parry successfully!")
                elif move.lower() in parry[enemyMove]["draw"]:
                    if random.randint(0, 1) == 1:
                        print(f"Your blades clash, but {ename}'s attack slips through!")
                        print(f"{ename} deals {dmg} damage!")
                        dmg = dmg/2
                    else:
                        print(f"You deflect the blade to the side and backflip away!")
                else:
                    print(f"You just got hit.")
                hp -= dmg
        turn += 1
        print(turn)
battle("Justin", "Anna", "An angry and annoying sister", 100, 100, 10, 10, 20, 30, 50, 50, 80, 60, ["cinder", "freeze", "heal"], ["buff", "freeze", "heal"], ["flashbang, fairy"], ["bazooka", "boomerang"], ["Anna stands atop a rock and points her sword at you. 'So weak.' "])


