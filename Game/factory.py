from character.extends_of_character import *
class Factory():

    def __init__(self):
        self.player_choose =None
        self.pc_choose = None

    def enter_player(self):
        enter_player = input("choississez votre avatar entre warrior,wizard et archer","--->")

        if enter_player == "warrior":
            self.player_choose = Warrior()

        if enter_player == "wizard":
            self.player_choose = Wizard()

        if enter_player == "archer":
            self.player_choose = Archer()

        return self.player_choose

    def pc_random(self,pc_random):
        self.pc_random = [Orc(),Wolf(),Zombie()]
        self.pc_choose = random.choice(self.pc_random)

        return self.pc_choose
