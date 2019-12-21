from character.extends_of_character import *
from Game.arena import Arena
from factory import Factory


factory=Factory()
var1 = factory.enter_player()
var2 = factory.pc_random()
instance_de_areana=factory.war_zone(var1,var2)
instance_de_areana.battle()
