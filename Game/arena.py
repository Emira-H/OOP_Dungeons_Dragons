from factory import Factory


class Arena:

    def __init__(self,combatant_1,combatant_2):
        self.combatant_1 = factory.player_choose
        self.combatant_2 = factory.pc_choose



    def attack_or_escape(self,attack):
        attack = input("2 choix s'offre a vous attaquer ")
        if attack == "o":
            self.attack_or_escape == True
            return self.attack_or_escape
        else :
            self.attack_or_escape == False
            return self.attack_or_escape



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
            ennemie.life -=(combatant.ennemie.defense)
            ennemie.defense = 0

    def dead(self,vie_hero,vie_monstre):
        vie_hero = self.combatant_1
        vie_monstre = self.combatant_2

        while vie_hero > 0 and vie_monstre > 0:
            Arena.combat()
