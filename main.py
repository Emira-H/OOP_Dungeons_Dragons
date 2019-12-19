from character.extends_of_character import *
from Game.extends_of_game import *

adv1=Wizard(250)
adv1.name="emira"
print(adv1)
adv2=Wolf()

print(adv2)
a=Arena(adv1,adv2)
a.part()
