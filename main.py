from player import Player
from lineup import LineUp
from typing import List

# mPlayerNames = ["Logan", "Atticus", "Will", "Rowan", "Cooper", "Baxter", "Jackson"]
# mPlayerNames = ["Logan", "Atticus", "Will", "tBaxter", "Cooper", "Rowan", "Jackson", "Tommy"]
mPlayerNames = ["Logan", "Atticus", "Cooper", "Tommy", "Will", "Rowan", "Jackson", "Baxter"]
mNumPlayers = len(mPlayerNames)
mLineups = []
mPlayers = []

for i in range(0, mNumPlayers):
    player = Player(mPlayerNames[i])
    mPlayers.append(player)

mNumPeriods = 4
mPeriodLen = 8
mSubPeriod = 4
mNumPlayersToSub = 2
mTotalGameTime = mNumPeriods * mPeriodLen

def createLineup(players:List[Player]):
    nLineup = LineUp()
    for player in players:
        player.incrementPlays(1)
        nLineup.addPlayer(player)

    mLineups.append(nLineup)

def generateLineups():
    mStartPlayers = []
    for i in range(0,4):
        mStartPlayers.append(mPlayers.pop())

    createLineup(mStartPlayers)

    for i in range(0, int(mTotalGameTime / mSubPeriod)-1):
        playersLeaving = []
        playersEntering = []
        for j in range(0, mNumPlayersToSub):
            playersLeaving.append(mStartPlayers.pop(0))
            playersEntering.append(mPlayers.pop(0))

            mStartPlayers.append(playersEntering[j])
            mPlayers.append(playersLeaving[j])

        createLineup(mStartPlayers)

def printLineups():
    print("Number of Players:", mNumPlayers)
    print("Total Game Time is {0} minutes.".format(mNumPeriods * mPeriodLen))
    print("Sub every {0} minutes.".format(mSubPeriod))
    print("{0} players swap at each sub interval".format(mNumPlayersToSub))
    print("")

    for i in range(0, len(mLineups)):
        print("\nLineup {0}".format(i))
        if(i != 0):
            mLineups[i].print(mLineups[i-1])
        else:
            mLineups[i].print(0)

def shiftLineupDown():
    print("Enter the lineup index to shift down:")
    uInput = input()

    lineup = mLineups.pop(int(uInput))
    mLineups.insert(int(uInput)+1, lineup)
    printLineups()
    selectAction()

def movePlayer():
    print("What line up is the player in?")
    mOriginalLineup = int(input())

    print("What player from this lineup?")
    mOriginalPlayer = int(input())

    print("What lineup to move the player into?")
    mOtherLineup = int(input())

    print("What player to swap with in the second lineup?")
    mOtherPlayer = int(input())

    mLineups[mOriginalLineup].swapPlayers(mLineups[mOtherLineup], mLineups[mOriginalLineup].players[mOriginalPlayer], mLineups[mOtherLineup].players[mOtherPlayer])
    printLineups()
    selectAction()

def selectAction():
    print("\nMake a selection:\n 1. Shift Lineup Down\n 2. Move Player\n 3. Exit")

    uInput = input()

    if int(uInput) == 1:
        shiftLineupDown()
    if int(uInput) == 2:
        movePlayer();

generateLineups()
printLineups()
selectAction()

