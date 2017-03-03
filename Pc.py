import pygame
from Character import Character

class Pc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName, initialPosition=[0,0]):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Pc/" + characterName + "/" + characterName + "_idle.png", initialPosition)
    # General character arguments
    self.image = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_idle.png").convert_alpha()
    self.deathSprite = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_dead.png").convert_alpha()
    self.position = self.image.get_rect()
    self.lookingDirection = 'left'
  def Attack(self, projectileList) :
    return 0
