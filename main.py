from player import Player

def printPlayers(players):
    for player in players:
        print(player)

# mPlayerNames = ["Logan", "Atticus", "Will", "Rowan", "Cooper", "Baxter", "Jackson"]
# mPlayerNames = ["Logan", "Atticus", "Will", "Baxter", "Cooper", "Rowan", "Jackson", "Tommy"]
mPlayerNames = ["Logan", "Atticus", "Cooper", "Rowan", "Will", "Tommy", "Jackson", "Baxter"]
mNumPlayers = len(mPlayerNames)

mPlayers = []
for i in range(0, mNumPlayers):
    player = Player(mPlayerNames[i])
    mPlayers.append(player)


mNumPeriods = 4
mPeriodLen = 8
mSubPeriod = 4
mNumPlayersToSub = 2
mTotalGameTime = mNumPeriods * mPeriodLen

print("Number of Players:", mNumPlayers)
print("Total Game Time is {0} minutes.".format(mNumPeriods * mPeriodLen))
print("Sub every {0} minutes.".format(mSubPeriod))
print("{0} players swap at each sub interval".format(mNumPlayersToSub))
print("")

mStartPlayers = []
for i in range(0,4):
    mStartPlayers.append(mPlayers.pop())

print("Starting Line Up")
for k in range(0,4):
    mStartPlayers[k].incrementPlays(1)
printPlayers(mStartPlayers)
print()

for i in range(0, int(mTotalGameTime / mSubPeriod)-1):
    playersLeaving = []
    playersEntering = []
    for j in range(0, mNumPlayersToSub):
        playersLeaving.append(mStartPlayers.pop(0))
        playersEntering.append(mPlayers.pop(0))

        mStartPlayers.append(playersEntering[j])
        mPlayers.append(playersLeaving[j])

    # mPlayers.append(mStartPlayers.pop(0))
    # mPlayers.append(mStartPlayers.pop(0))
    # mStartPlayers.append(mPlayers.pop(0))
    # mStartPlayers.append(mPlayers.pop(0))

    for k in range(0,4):
        mStartPlayers[k].incrementPlays(1)

    p1 = str(mStartPlayers[0])
    p2 = str(mStartPlayers[1])
    p3 = str(mStartPlayers[2])
    p4 = str(mStartPlayers[3])

    l1 = str(playersLeaving[0])
    l2 = str(playersLeaving[1])

    e1 = str(playersEntering[0])
    e2 = str(playersEntering[1])

    row0 = "Substitution {0}".format(i)
    row1 = "Line Up                             Players Leaving                         Players Entering".format(i)
    row2 = "{0:40}{1:40}{2}".format(p1, l1, e1)
    row3 = "{0:40}{1:40}{2}".format(p2, l2, e2)
    row4 = "{0}".format(p3)
    row5 = "{0}".format(p4)
    
    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print()

    # print("Substition: ", i)
    # print("Players Leaving:")
    # printPlayers(playersLeaving)
    # print("")
    # print("Players Entering:")
    # printPlayers(playersEntering)
    # print("")
    # print("Current Line up:")
    # printPlayers(mStartPlayers)
    # print("")




#Add all players to one array
for i in range(0, len(mPlayers)):
    mStartPlayers.append(mPlayers.pop())

#Print all players stats
for i in range(0, mNumPlayers):
    print(mStartPlayers[i])