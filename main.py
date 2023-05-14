from player import Player
from lineup import LineUp
from typing import List
import pickle

mPlayerNames = ["Logan", "Atticus", "Will", "Rowan", "Cooper", "Baxter", "Jackson"]
# mPlayerNames = ["Logan", "Atticus", "Will", "tBaxter", "Cooper", "Rowan", "Jackson", "Tommy"]
#mPlayerNames = ["Logan", "Atticus", "Cooper", "Tommy", "Will", "Rowan", "Jackson", "Baxter"]
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

def printLineups(lineup):
    print("Number of Players:", mNumPlayers)
    print("Total Game Time is {0} minutes.".format(mNumPeriods * mPeriodLen))
    print("Sub every {0} minutes.".format(mSubPeriod))
    print("{0} players swap at each sub interval".format(mNumPlayersToSub))
    print("")

    for i in range(0, len(lineup)):
        print("\nLineup {0}".format(i))
        if(i != 0):
            lineup[i].print(lineup[i-1])
        else:
            lineup[i].print(0)

def shiftLineupDown():
    print("Enter the lineup index to shift down:")
    uInput = input()

    lineup = mLineups.pop(int(uInput))
    mLineups.insert(int(uInput)+1, lineup)
    printLineups(mLineups)
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
    printLineups(mLineups)
    selectAction()

def saveLineup():
    print("Enter the filename to save the lineup to:")
    filename = input()

    with open(filename, 'wb') as f:
        # serialize the object and write it to the file
        pickle.dump(mLineups, f)

    print("File Saved, press enter to continue!")
    
    input()
    selectAction()

def loadLineup():
    print("Enter the filename you would like to load:")
    filename = input()

    global mLineups
    with open(filename, 'rb') as f:
        # deserialize the object from the file
        mLineups = pickle.load(f)
    
    print("Lineup loaded, press enter to continue!")
    input()

    printLineups(mLineups)
    selectAction()

def selectAction():
    print("\nMake a selection:\n 1. Shift Lineup Down\n 2. Move Player\n 3. Save Lineup to file\n 4. Load Lineup from file\n 5. Print Lineup\n 6. Exit")

    uInput = int(input())

    if uInput == 1:
        shiftLineupDown()
    elif uInput == 2:
        movePlayer()
    elif uInput == 3:
        saveLineup()
    elif uInput == 4:
        loadLineup()
    elif uInput == 5:
        printLineups(mLineups)
        selectAction()

generateLineups()
printLineups(mLineups)
selectAction()