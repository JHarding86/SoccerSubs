import tkinter as tk
from tkinter import filedialog
from lineup import LineUp
from typing import List
import pickle

class userInterface(tk.Frame):
    def __init__(self, master, mLineups:List[LineUp]):
        super().__init__(master)
        self.master = master
        self.mLineups = mLineups
        self.lineupSwap = -1
        self.playerSwap = -1
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # self.removeAllWidgets()
        # Create lineup labels and buttons
        for i, lineup in enumerate(self.mLineups):
            row = i // 4
            col = i % 4
            label = tk.Label(self, text=f"Lineup {i+1}")
            label.grid(row=row*6, column=col*3, sticky="w")
            button = tk.Button(self, text="Swap", command=lambda idx=i: self.swap_lineup(idx))
            button.grid(row=row*6, column=col*3+1, sticky="w")

            # Create player list and swap buttons
            for j, player in enumerate(lineup):
                player_label = tk.Label(self, text=f"- {player}")
                player_label.grid(row=row*6+j+1, column=col*3, sticky="w", padx=20, pady=2)
                player_button = tk.Button(self, text="Swap", command=lambda lidx=i, pidx=j: self.swap_player(lidx, pidx))
                player_button.grid(row=row*6+j+1, column=col*3+1, sticky="w", pady=2)

        # Create Save, Load, and Print buttons
        save_button = tk.Button(self, text="Save", command=self.save_file)
        save_button.grid(row=(row+1)*6+1, column=0)

        load_button = tk.Button(self, text="Load", command=self.load_file)
        load_button.grid(row=(row+1)*6+1, column=1)

        print_button = tk.Button(self, text="Print", command=self.print_output)
        print_button.grid(row=(row+1)*6+1, column=2)

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            with open(filename, "wb") as f:
                pickle.dump(self.mLineups, f)

    def load_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt")
        if filename:
            with open(filename, "rb") as f:
                self.mLineups = pickle.load(f)

            # Refresh the display
            self.create_widgets()

    def print_output(self):
        # print("Number of Players:", mNumPlayers)
        # print("Total Game Time is {0} minutes.".format(mNumPeriods * mPeriodLen))
        # print("Sub every {0} minutes.".format(mSubPeriod))
        # print("{0} players swap at each sub interval".format(mNumPlayersToSub))
        # print("")

        for i in range(0, len(self.mLineups)):
            print("\nLineup {0}".format(i))
            if(i != 0):
                self.mLineups[i].print(self.mLineups[i-1])
            else:
                self.mLineups[i].print(0)

    def swap_lineup(self, lineup_idx):
        if self.lineupSwap == -1:
            self.lineupSwap = lineup_idx
            return
        else:
            self.mLineups[self.lineupSwap], self.mLineups[lineup_idx] = self.mLineups[lineup_idx], self.mLineups[self.lineupSwap]
            self.lineupSwap = -1
            self.removeAllWidgets()
            self.create_widgets()

            print(f"Swapping lineup {lineup_idx}")

    def swap_player(self, lineup_idx, player_idx):
        if self.lineupSwap == -1 or self.playerSwap == -1:
            self.lineupSwap = lineup_idx
            self.playerSwap = player_idx
            return
        else:
            thisPlayer = self.mLineups[lineup_idx].players[player_idx]
            
            otherLineup = self.mLineups[self.lineupSwap]
            thatPlayer = otherLineup.players[self.playerSwap]
            
            self.mLineups[lineup_idx].swapPlayers(otherLineup, thisPlayer, thatPlayer)
            self.lineupSwap = -1
            self.playerSwap = -1
            self.create_widgets()

        print(f"Swapping player {player_idx} in lineup {lineup_idx}")
    
    def removeAllWidgets(self):
        lineups = self.mLineups
        _list = self.master.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        for item in _list:
            item.destroy()

        super().__init__(self.master)
        self.grid()
        self.mLineups = lineups
        # _list = self.master.winfo_children()

        # for item in _list :
        #     if item.winfo_children() :
        #         _list.extend(item.winfo_children())

        # for item in _list:
        #     item.pack_forget()
# Example usage
# mLineups = [
#     ["John", "Paul", "George", "Ringo"],
#     ["Mick", "Keith", "Ronnie", "Charlie"],
#     ["Freddie", "Brian", "Roger", "John"],
#     ["Thom", "Jonny", "Colin", "Phil"],
#     ["Kurt", "Dave", "Krist", "Pat"],
#     ["Eddie", "Mike", "Stone", "Jeff"],
#     ["Bono", "The Edge", "Adam", "Larry"],
#     ["Robert", "Jimmy", "John Paul", "Bonham"],
# ]
# root = tk.Tk()
# app = MyApp(root, mLineups)
# app.mainloop()
