import zombiedice,random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class randomzombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            m=random.randint(0,1)
            if m==0:
                break
            else:
                diceRollResults = zombiedice.roll()

class shotgun2:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
class random14:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        m=4
        shotgun=0
        while m>0:
            shotgun += diceRollResults['shotgun']
            m=m-1
            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class shotgunbrain:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotgun > brains:
                break
            else:
                diceRollResults = zombiedice.roll()
     
zombies = (
    MyZombie(name='My Zombie Bot'),
    randomzombie(name='Random-Bot'),
    shotgun2(name='Shotgun2a'),
    random14(name='BOT-3'),
    shotgunbrain(name='BOT-4'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
