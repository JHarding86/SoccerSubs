class Player:
    def __init__(self, name):
        self.numPlays = 0
        self.name = name

    def __str__(self):
        return "{0:10} plays:{1}".format(self.name, self.numPlays)

    def incrementPlays(self, value):
        self.numPlays += value