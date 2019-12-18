from character.character import Character
class Wizard(Character):

    def __init__(self,mana):
        super().__init__(600,20, 50,25)
        self.mana=mana
        self.cheek_heal=True
    
    def heal(self,add_life):
        if self.cheek_heal:
            if self.mana>=add_life:
                self.mana-=add_life
                self.life+=add_life
            elif self.mana<add_life:
                self.life+=self.mana
                self.mana=0
                self.cheek_heal=False
            return self.cheek_heal
    def __repr__(self):
        return super().__repr__()+", mana ({})".format(self.mana)
            



