import pygame
import pg_functions
from Npc import Npc
from Character import Character

class NPC_TreeMonster(Npc):

  'Base class for TreeMonster'

  def __init__(self, screen, initialPosition=[0,0], direction = 'right'):
    Npc.__init__(self,screen, "TreeMonster", initialPosition)

    # General combat arguments
    self.maxHp = 300
    self.currentHp = 300
    self.invulnerabilityFrameDuration = 0

    self.direction = direction
    # X movement related arguments
    self.xMaxSpeed = 5
    self.xSlowDown = self.xMaxSpeed/25.0
    self.xAcceleration = self.xMaxSpeed/20.0

    # Jump related arguments
    self.numberOfJumps = 0

    # Spirit sprite related arguments
    self.spiritImage = pygame.image.load("Sprites/Characters/Npc/TreeMonster/TreeMonster_spirit.png")
    self.spiritImageReverse = pygame.transform.flip(self.spiritImage, True, False) 
    self.displayTamponSize = 3
    self.framesBetweenTampon = 1
    self.lastPositions = []
    self.lastDirections = []

    self.spriteDirection = 'left'
    for i in range(self.displayTamponSize * self.framesBetweenTampon):
      self.lastPositions.append(self.position)
      self.lastDirections.append(self.lastDirections)
    # General character arguments

  def DeclareCollision(self, directions):
    Npc.DeclareCollision(self, directions)


  def blit(self):
    ## Tampon management
    del self.lastPositions[0]
    self.lastPositions.append(self.position)
    del self.lastDirections[0] 
    self.lastDirections.append(self.direction)
    for i in range(self.displayTamponSize*self.framesBetweenTampon):
      if i%self.framesBetweenTampon == 0:
        if self.lastDirections[i] == 'right':
          pg_functions.blit_alpha(self.screen, self.spiritImageReverse, self.lastPositions[i], 150 + (1.0*i)/self.displayTamponSize * 105)
        if self.lastDirections[i]  == 'left':
          pg_functions.blit_alpha(self.screen, self.spiritImage, self.lastPositions[i], 150 + (1.0*i)/self.displayTamponSize * 105)
    Npc.blit(self)

  def Move(self):
    if self.direction == 'right':
      Character.Move(self, {'left':0, 'right':1, 'up':0, 'down':0})
    if self.direction == 'left':
      Character.Move(self, {'left':1, 'right':0, 'up':0, 'down':0})

