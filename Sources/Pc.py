import pygame
from Character import Character
from pg_functions import correctedBlit


class Pc(Character):

  'Base class for the playable character'

  def __init__(self, screen, characterName, initialPosition=[0,0]):
 
    Character.__init__(self, screen, characterName, "Sprites/Characters/Pc/" + characterName + "/" + characterName + "_idle.png", initialPosition)
    # General character arguments
    self.invulnerabilityFrameDuration = 50
    self.image = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_idle.png").convert_alpha()
    self.deathSprite = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_dead.png").convert_alpha()
    self.inactiveSprite = pygame.image.load("Sprites/Characters/Pc/" + self.name + "/" + self.name + "_inactive.png").convert_alpha()
    self.position = self.image.get_rect()
    self.lookingDirection = 'left'

  def Attack(self, projectileList) :
    return 0

  def Display(self, cameraPosition, active = True):
    if active and not(self.dead): 
      Character.Display(self, cameraPosition)
    elif self.dead :
      if self.direction != self.spriteDirection :
        correctedBlit(self.screen,pygame.transform.flip(self.deathSprite, True, False), self.position, cameraPosition)
      else :
        correctedBlit(self.screen,self.deathSprite, self.position, cameraPosition)
    else:
      if self.direction != self.spriteDirection :
        correctedBlit(self.screen,pygame.transform.flip(self.inactiveSprite, True, False), self.position, cameraPosition)
      else :
        correctedBlit(self.screen,self.inactiveSprite, self.position, cameraPosition)

    self.DisplayHp(cameraPosition)

  def GetSize(self):
    if not self.dead:
      return Character.GetSize(self)
    else :
      return (self.deathSprite.get_width(), self.deathSprite.get_height())
