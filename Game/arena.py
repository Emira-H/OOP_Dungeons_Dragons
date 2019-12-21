from factory import Factory
from character.extends_of_character import *


class Arena:
<<<<<<< HEAD
    """ une classe qui simule une partie tant que il n'y a pas un perdant"""
    def __init__(self,player,pc):
        self.player=player
        self.pc=pc

 
    def coup_player(self):
       
        """ le player attaque d'abord une defense ensuite si la defense est epuisé attaque le life"""
        respense=""
        while respense not in ["a","e","s"]:
            respense=input("taper 'a' pour attaquer ou 'e' pour esquiver dans le cas de magicien vous pouver vous soinger 's': ").lower()
        if respense=="a":
            attack= self.player.attack(self.pc.agility)
            if attack==0:
                print("{} a esquiver l'attaque de {} garce a son agility de {}".format(self.pc.name,self.player.name,self.pc.agility))
                sleep(5)
            else:
                print("{} attaque avec {} son adversaire {}".format(self.player.name,attack,self.pc.name))
                sleep(5)
            if attack<self.pc.defense:
                self.pc.defense-=attack
            else:
                self.pc.life-=(attack-self.pc.defense)
                self.pc.defense=0
         
        if respense=="e":
            print("{} a esquiver au lieu d'attaquer {}".format(self.player.name,self.pc.name))
            sleep(5)

            """ je verifie si player s'agit bien d'une instance de Wizzar"""
        if respense=="s" and self.player.__dict__.get("mana",-1) !=-1:
            print("vous avez {} point de  vie et {}  de mana".format(self.player.life,self.player.mana))
            if self.player.heal(int(input("combien vous voulez recuperer  de point de vie: "))):
                 print("desormais vous avez {} point de  vie et {} de mana ".format(self.player.life ,self.player.mana))
            else:
                print("vous avez plus de mana")
        elif respense=="s" and self.player.__dict__.get("mana",-1)==-1:
            print("vous n'êtes magicien et vous taper 's', ^_^  vous aller soubir le coup d'attaque de l'avesaire {}".format(self.pc.name))
                


    def coup_pc(self):
       
        """ le pc attaque d'abord une defense ensuite si la defense est epuisé attaque le life """
        attack= self.pc.attack(self.player.agility)
        if attack==0:
            print("{} a esquiver l'attaque de {} garce a son agility de {}".format(self.player.name,self.pc.name,self.player.agility))
            sleep(5)
        else:
            print("{} attaque avec {} son adversaire {}".format(self.pc.name,attack,self.player.name))
            sleep(5)
        if attack<self.player.defense:
            self.player.defense-=attack
        else:
            self.player.life-=(attack-self.player.defense)
            self.player.defense=0


    def part(self):
      
        """ la methode qui fait jouer les adversaire a tour de role """
        while self.player.life>0 and self.pc.life>0:
            system("clear")
            self.coup_player()
            self.coup_pc()
            print(self.player)
            print(self.pc)
            sleep(5)
       
=======

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
>>>>>>> a78223820ba97e4f5f90c81696524d8faefbd9f8
