class Character:

    def __init__(self,name,life,attack,agility,defense):
        self.__name=name
        self.__attack=attack
        self.agility=agility
        self.defense=defense
    @property
    def name(self):
        return __name
    @name.setter
    def name(self,name):
        if 2<len(name)<15:
            self__name=name
            return True
        else:
            return False
        
    def skip(self):
        """je passe au tour suivant et renvoi zero"""
        return 0

    def cheek_attack(self):
        """je verifier en fonction de l'agilité s'il doit attaqé
        ou non"""
        import random
        up_to_100=random.randint(1,100)
        if(up_to_100 in range(1,101-self.agility)):
            return self.__attack
        else:
            return 0




