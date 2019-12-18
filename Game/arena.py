from character import Character
from wizzard import Wizzard

class Arena(Character):

    def __init__(self,life,defense,attack,agility,attack_adverse):
        super().__init__(life,defense,attack,agility)


    def dommage(self,life,defense,attack,agility,attack_adverse):

        if defense <= 0:
            life -= attack_adverse

        elif defense >= attack_adverse:
            defense -= attack_adverse

        else :
            life -=(attack_adverse-defense)
            defense = 0
