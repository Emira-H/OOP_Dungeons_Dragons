from time import sleep
from os import system
class Arena:
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
       