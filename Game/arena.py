


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
            else:
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
