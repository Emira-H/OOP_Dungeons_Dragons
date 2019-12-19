
class Factory():

    def __init__(self,player_choose,pc_choose):
        self.player_choose =["warrior","wizard","archer"]
        self.pc_choose = None

    def enter_player(self,enter_player):
        enter_player = input("choississez votre avatar entre warrior,wizard et archer","--->")

        if enter_player == "warrior":
            self.player_choose = warrior()

        if enter_player == "wizard":
            self.player_choose = wizard()

        if enter_player == "archer":
            self.player_choose = archer()

        return self.player_choose

    def pc_random(self,pc_random):
        self.pc_random = [orc(),wolf(),zombie()]
        self.pc_choose = random.choice(self.pc_random)

        return self.pc_choose
