from player import Player
from typing import List

class LineUp:
    def __init__(self):
        self.players:List[Player] = []

    def addPlayer(self, player: Player):
        self.players.append(player)

    def print(self, otherLineup):
        if(otherLineup == 0):
            for player in self.players:
                print(player)
        else:
            mPlayersLeaving     = []
            mPlayersEntering    = []

            for player in self.players:
                if self.doesLineUpContainPlayer(otherLineup, player) == False:
                    mPlayersEntering.append(player)
                # print(player)

            for player in otherLineup.players:
                if otherLineup.doesLineUpContainPlayer(self, player) == False:
                    mPlayersLeaving.append(player)

            # print("\nPlayers Leaving:")
            # for player in mPlayersLeaving:
            #     print(player)

            # print("\nPlayers Entering:")
            # for player in mPlayersEntering:
            #     print(player)
            
            print("Line Up                             Players Leaving                         Players Entering")
            for i in range(0, len(self.players)):
                print("{0:40}".format(self.players[i].name), end=" ")
                if i < len(mPlayersLeaving):
                    print("{0:40}".format(mPlayersLeaving[i].name), end=" ")
                else:
                    print("{0:40}".format(""), end=" ")
                if i < len(mPlayersEntering):
                    print("{0:40}".format(mPlayersEntering[i].name))
                else:
                    print("{0:40}".format(""))

            #         row2 = "{0:40}{1:40}{2}".format(self.players[0], mPlayersLeaving[0], mPlayersEntering[0])
            # row3 = "{0:40}{1:40}{2}".format(self.players[1], mPlayersLeaving[1], mPlayersEntering[1])
            # row4 = "{0:40}{1:40}{2}".format(self.players[2], mPlayersLeaving[2], mPlayersEntering[2])
            # row5 = "{0:40}{1:40}{2}".format(self.players[3], mPlayersLeaving[3], mPlayersEntering[3])

    def doesLineUpContainPlayer(self, linueup, player:Player):
        for p in linueup.players:
            if p.name == player.name:
                return True
        
        return False
    
    def swapPlayers(self, otherLineup, thisLineupPlayer:Player, thatLineupPlayer:Player):
        
        if otherLineup.doesLineUpContainPlayer(otherLineup, thisLineupPlayer) :
            print("Cannot swap a player into a line that the player already exists in!")
            print("Press enter to continue")
            input()
            return
        
        if self.doesLineUpContainPlayer(self, thatLineupPlayer) :
            print("Cannot swap a player into a line that the player already exists in!")
            print("Press enter to continue")
            input()
            return

        thisIndex = self.players.index(thisLineupPlayer);
        thatIndex = otherLineup.players.index(thatLineupPlayer);

        self.players[thisIndex] = thatLineupPlayer;
        otherLineup.players[thatIndex] = thisLineupPlayer;

        print("Players swapped successfully!")
        print("Press enter to continue")
        input()