from character.extends_of_character import *
from Game.arena import Arena

adv1=Warrior()
adv1.name="emira"
print(adv1)
adv2=Wolf()
print(adv2)

combat = Arena(adv1,adv2)
combat.battle()
