import random

def manageSpells(move, mp):
    move = move.lower()
    dmg = 0
    effect = None
    target = "E"
    cost = 0
    
    if move == "fireball":
        print("You cast a burning red fireball, and hurl it at your opponent.")
        dmg = mp
        effect = "burn"
    elif move == "heal":
        print("You feel an ethereal power flying through your arteries, and resting at your heart.")
        print(f"You've healed {round(cost / 2)} hp!")
        dmg = -round(cost / 2)
        target = "U"
    elif move == "Buff":
        print("You buff up your attack!")
        dmg = mp
    elif move == "Freeze":
        print()
        
        
    return dmg, effect, target

def battle(name, ename, edesc, hp, ehp, df, edf, pow, epow, mp, emp, speed, espeed, spells, espells, items, eitems, etaunts):
    turn = 0
    vowels = ["a", "e", 'i', 'o', 'u']
    parry = {
        "head" : {
            "wins" : ["head"],
            "draw" : ["chest", "flank"],
            "lose" : ["knee"]
        },
        "chest" : {
            "wins" : [""],
            "draw" : ["head", "knee"],
            "lose" : ["flank"]
        },
        "flank" : {
            "wins" : ["flank"],
            "draw" : ["head", "knee"],
            "lose" : ["chest"]
        },
        "knee" : {
            "wins" : ["knee"],
            "draw" : ["chest", "flank"],
            "lose" : ["head"]
        }
    }
    if ename[0] not in vowels:
        print(f"You've encountered a {ename}!")
    else:
        print(f"You've encountered an {ename}!")
    print(edesc)
    while not hp <= 0 and not ehp <= 0:
        move = input("Do you attack, cast a spell, use an item, or say something?")
        if move.lower() == "attack":
            move = input("Do you attack head, chest, flank or knee?")
            enemyMove = random.choice(["head", "chest", "flank", "knee"])
            print(f"The enemy parries {enemyMove}")
            if move.lower() in parry[enemyMove["wins"]]:
                print("The enemy parries your attack!")
            elif move.lower() in parry[enemyMove["draw"]]:
                if random.randint(0, 1) == 1:
                    print("Your blades clash, but your attack slips through!")
                else:
                    print("The opponent deflects your blade to the side and backs away!")
            else:
                print("The enemy just outright has a skill issue and gets hit.")
            ehp -= max(3, pow * random.choice[1, 1, 1, 1, 1, 1, 1, 1, 1, 2] - edf) + random.randrange(-3.9, 4.0)
        elif move.lower() == "spell":
            move = input(f"Which spell? The spells you have are {spells}.")
            if move in spells:
                dmg, effect, target = manageSpells(move)
            else:
                print(f"You try and utter the spell of {move}, but it doesn't work, as you are too braindead to know it!")
        



