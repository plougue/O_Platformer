import pygame
from Character import Character

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

  def blit(self, active = True):
    if active and not(self.dead): 
      Character.blit(self)
    elif self.dead :
      if self.direction != self.spriteDirection :
        self.screen.blit(pygame.transform.flip(self.deathSprite, True, False), self.position)
      else :
        self.screen.blit(self.deathSprite, self.position)
    else:
      if self.direction != self.spriteDirection :
        self.screen.blit(pygame.transform.flip(self.inactiveSprite, True, False), self.position)
      else :
        self.screen.blit(self.inactiveSprite, self.position)

    self.DisplayHp()

  def GetSize(self):
    if not self.dead:
      return Character.GetSize(self)
    else :
      return (self.deathSprite.get_width(), self.deathSprite.get_height())
