#Magic the Gathering Mana Checker

Manapool = "WRRGUU"
Manacost = "2RR"

def KasittelemanaCost(Cost):
    possibleManas = [["W", 0],
                     ["U", 0],
                     ["B", 0],
                     ["R", 0],
                     ["G", 0],
                     ["C", 0],
                     ["ANY COLOR", 0]]
    neutralneededtemp = []
    
    #Check total manacost
    for x in Cost:
        #check if x is number to get how many neutral manas are needed
        if x.isdigit():
            neutralneededtemp.append(int(x))
    #if neutralmanacost in 2 digits combine them
    NumTeksti = ''.join(str(num) for num in neutralneededtemp)
    neutralneeded = int(NumTeksti)
    possibleManas[len(possibleManas)-1][1] = neutralneeded
    #Check how many and what colored manas are needed
    for i in Cost:
        for j in possibleManas:
            if i == j[0]:
                j[1] += 1
    return possibleManas
    
    
    #Check how much of each color is in the pool
def KasitteleManapool(pool):
    Usablemana = [["W", 0],
                  ["U", 0],
                  ["B", 0],
                  ["R", 0],
                  ["G", 0],
                  ["C", 0]]
    for x in pool:
        for y in Usablemana:
            if x == y[0]:
                y[1] += 1
    return Usablemana
def onkoRiittavasti(manaC, manaP):
    manaC = KasittelemanaCost(manaC)
    manaP = KasitteleManapool(manaP)
    usableNeutral = 0
    for x in manaC:
        for y in manaP:
            if x[0] == y[0]:
                if x[1] > y[1]:
                    return False
                if x[1] < y[1]:
                    usableNeutral += y[1] - x[1]
    if usableNeutral >= manaC[len(manaC)-1][1]:
        return True
    else:
        return False

Onnistuuko = onkoRiittavasti(Manacost, Manapool)
print(Onnistuuko)
