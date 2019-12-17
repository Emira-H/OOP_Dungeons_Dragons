class Character:
    
    def __init__(self,name,life,attack,agility,defense):
        self.name=name
        self._attack=attack
        self.agility=agility
        self.defense=defense
    
    @property
    def attack(self):
        return self._attack
    

        