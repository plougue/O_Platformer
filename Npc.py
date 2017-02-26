import pygame
from Character import Character

class Npc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Npc/" + characterName + "/" + characterName + "_idle.png")
    # General character arguments

    self.direction = 'left'
  def Move(self, resolution):
    if self.direction == 'right':
      Character.Move(self, {'left':0, 'right':1, 'up':1, 'down':0}, resolution)
      if self.position[0] + self.image.get_width() >= resolution[0]:
        self.direction = 'left'
    if self.direction == 'left':
      Character.Move(self, {'left':1, 'right':0, 'up':0, 'down':0}, resolution)
      if self.position[0] <= 0:
        self.direction = 'right'
  
