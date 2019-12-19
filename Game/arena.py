from factory import Factory


class Arena:

    def __init__(self,combatant_1,combatant_2):
        self.combatant_1 = self.player_choose
        self.combatant_2 = self.pc_choose



    def attack_or_escape(self,attack):
        if attack == "o":
            self.attack_or_escape == True
            return self.attack_or_escape
        else :
            self.attack_or_escape == False



    def attack_adverse(self,attack_adverse):
        hero = self.combatant_1
        ennemie = self.combatant_2

        self.attack_level = hero.character.attack


    def combat(self,hero,ennemie):
        combatant = None
        ennemie = None

        if self.attack_or_escape == True:
            combatant = self.combatant_1
            ennemie = self.combatant_2
            return combatant
            return ennemie
            dommage(ennemie,combatant)
            print(ennemie.life,combatant.life)

            combatant = self.combatant_2
            ennemie = self.combatant_1
            return combatant
            return ennemie
            dommage(ennemie,combatant)
            print(ennemie.life,combatant.life)

        else :
            print("vous fuyez !!!!!!!!!!")





    def dommage(self,ennemie,combatant):

        if ennemie.defense <= 0:
            ennemie.life -= commbatant.attack

        elif ennemie.defense >= commbatant.attack:
            ennemie.defense -= commbatant.attack

        else :
            ennemie.life -=(commbatant.ennemie.defense)
            ennemie.defense = 0

    def dead(self,combatant_1,combatant_2)
        if 
