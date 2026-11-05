wc = input("(All q's ar y/n) U r in a wizard duel. Is ur wand charged????? ")
if wc == 'y':
    mana = int(input("What is ur mana? "))
    if mana >= 50:
        spell = input("Is spell lightning (ln) or ice(i)? ")
        if spell == 'ln':
            eshield = input("Is the enemy's shield fire? ")
            if eshield == "y":
                print('⚡ Lightning pierces the shield — you win!')
            else:
                print("Enemy absorbs and reflects the spell — you lose HP.")
        else:
            temp = float(input("What is temp?"))
            if temp < 0:
                print("Spell doubles in power — enemy frozen!")
            else:
                print("Spell melts mid-air — wasted mana.")
    else:
        potion = input("Is potion available? ")
        if potion == 'y':
            ptype = input("What is the potion type? ")
            if ptype == 'mana':
                print(" You restore mana and continue the duel.") 
            else:
                print(" Potion backfires — you lose focus.")       
        else:
            print("Enemy takes advantage - critical hit on you! ")
else:
    staffb = input("is ur staff broken? ")
    if staffb == "y":
        bw = input('Do you have a backup wand? ')
        if bw == 'y':
            print("You use ur backup wand, but it has half power.")
        else:
            print("You surrender — no weapon left.")
    else:
        print("You channel energy by hand — risky but powerful.")