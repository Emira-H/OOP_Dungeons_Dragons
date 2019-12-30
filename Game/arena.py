from factory import Factory
from character.extends_of_character import *


class Arena:

    def __init__(self,combatant_1,combatant_2):
        self.combatant_1 = combatant_1
        self.combatant_2 = combatant_2



    def attack_or_escape(self):
        attack = input("2 choix s'offrent a vous: entrez pour combattre ou une autre touche pour fuir ")

        if attack == "":
            return True
        else :
            return False


    def dammage_combatant1(self):
                strike=self.combatant_1.attack(self.combatant_2.agility)

                if strike == 0:
                    print("l'attaque a echoué")
                else:
                    if self.combatant_2.defense >= strike:
                        self.combatant_2.defense-=strike
                    else:
                        self.combatant_2.life -= (strike - self.combatant_2.defense)
                        self.combatant_2.defense = 0
                        if self.combatant_2.life<= 0:
                           self.combatant_2.life = 0
                print(self.combatant_1)
                print(self.combatant_2)



    def dammage_combatant2(self):
            strike=self.combatant_2.attack(self.combatant_1.agility)
            if strike == 0:
                print("l'attaque a echoué")
                mage = Factory()
                if self.attack_or_escape()==True and mage.player_choose == Wizard(250) and self.wizzard.heal() == True:
                    print("vous pouvez vous soignez ou attaqué, votre mana !".format(Wizard.mana))
                    if input("") == "h" :
                        add_life = input("combien de vie ?--->" )
                        wizzard.heal(add_life)

                if self.combatant_1.defense >= strike:
                   self.combatant_1.defense-=strike
                else:
                    self.combatant_1.life -= (strike - self.combatant_1.defense)
                    self.combatant_1.defense = 0
                    if self.combatant_1.life <=0:
                        self.combatant_1.life=0
            print(self.combatant_1)
            print(self.combatant_2)


    def battle(self):
        while self.combatant_1.life > 0 and self.combatant_2.life > 0 and self.attack_or_escape():
            self.dammage_combatant1()
            self.dammage_combatant2()
        if self.combatant_2.life == 0:
            print("Vous avez gagné!")
        elif self.combatant_1.life == 0:
            print("Vous avez perdu!")
        else:
            print("Vous fuyez l'ennemi!","FIN DE PARTIE")

