from player import Player
from lineup import LineUp
from typing import List
import pickle
import tkinter as tk
from userInterface import userInterface

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

generateLineups()
printLineups(mLineups)

root = tk.Tk()
ui = userInterface(root, mLineups)
ui.mainloop()