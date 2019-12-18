from character.wizard import *
from character.wolf import *

adv1=Wizard(250)
adv1.name="emira"
adv2=Wolf()
adv2.name="farid"
print(adv2.agility)
print(adv1.name,"attaque avec ",adv1.attack(adv2.agility))
print("le deuxieme object",adv2.name)