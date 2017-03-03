import pygame
from Pc import Pc

class PC_Markus(Pc):

  'Base class for markus'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Markus", initialPosition)
    self.numberOfJumps = 2
    self.maxHp = 2
    self.currentHp = 2 

    self.spiritImage = pygame.image.load("Sprites/Characters/Pc/Markus/Markus_spirit.png")
    self.spiritImageReverse = pygame.transform.flip(self.spiritImage, True, False) 
    self.displayTamponSize = 3
    self.lastPositions = []
    self.lastDirections = []
    for i in range(self.displayTamponSize):
      self.lastPositions.append(self.position)
      self.lastDirections.append(self.lastDirections)
    # General character arguments
  def Move(self, movements, resolution):
    lastFrameDirection = self.direction
    Pc.Move(self, movements, resolution)
  def blit(self):
    del self.lastPositions[0]
    self.lastPositions.append(self.position)
    del self.lastDirections[0]
    self.lastDirections.append(self.direction)
    for i in range(self.displayTamponSize):
      if self.lastDirections[i] == 'right':
        self.screen.blit(self.spiritImageReverse,self.lastPositions[i])
      if self.lastDirections[i]  == 'left':
        self.screen.blit(self.spiritImage,self.lastPositions[i])
    Pc.blit(self)
