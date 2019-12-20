from factory import Factory


class Arena:

    def __init__(self,combatant_1,combatant_2):
        self.combatant_1 = combatant_1
        self.combatant_2 = combatant_2



    def attack_or_escape(self):
        attack = input("2 choix s'offre a vous entrez combattre ou fuir ")
        if attack == "o":

            return True
        else :
            return False


    def combat(self):

            if self.attack_or_escape():
                strike=self.combatant_1.attack(self.combatant_2.agility)

                if strike == 0:
                    print("l'attaque a echoué")
                else:
                    if combatant_2.defense >= strike:
                        combatant_2.defense-=strike
                    else:
                        combatant_2.life -= (strike - combatant_2.defense)
                        combatant_2.defense = 0
            else: 
                print("vous fuyez!!!!!!!!!")


    def dommage(self,ennemie,combatant):
        a=enemie.attack(combatant.agility)
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
