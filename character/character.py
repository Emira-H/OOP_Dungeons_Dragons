class Character:

    def __init__(self,life,attack,defense,agility):
        self.__name=None
        self.life=life
        self.__attack=attack
        self.defense=defense
        self.agility=agility

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,name):
        if 2<len(name)<15:
            self.__name=name
            return True
        else:
            return False


    def attack(self,agility_adverse):
        """je verifier en fonction de l'agilité s'il doit attaqé
        ou non"""
        import random
        """dans cette fonction une proba de 90% d'attaqué"""
        up_to_100=random.randint(1,100)
        if up_to_100 in range(0,agility_adverse+1):
            return 0
        else:
            return self.__attack
    def __repr__(self):
        return "name ({}) , life ({}) , defense ({}) ,il a ({}%) de chance d'esquiver les attaques".format(
            self.__name,self.life,self.defense,self.agility)



