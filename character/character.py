class Character:

    def __init__(self,name,life,attack,agility,defense):
        self.name=name
        self._attack=attack
        self.agility=agility
        self.defense=defense


    def skip(self):
        """je passe au tour suivant et renvoi zero"""
        return 0

    def cheek_attack(self):
        """je verifier en fonction de l'agilité s'il doit attaqé
        ou non"""
        import random
        up_to_100=random.randint(1,100)
        if(up_to_100 in range(1,101-self.agility)):
            return self._attack
        else:
            return 0




