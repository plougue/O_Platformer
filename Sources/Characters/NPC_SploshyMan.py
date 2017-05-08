import pygame
from Sources.Npc import Npc

class NPC_SploshyMan(Npc):

  'Base class for TreeMonster'

  def __init__(self, screen, initialPosition=[0,0]):
    Npc.__init__(self,screen, "SploshyMan", initialPosition)

    # General combat arguments
    self.invulnerabilityFrameDuration = 0
    


    self.currentHp = 5
    self.maxHp = 5

    self.jumpSpeed = 4
    self.maxAccelerationFrames = 4

    # X movement related arguments
    self.spriteDirection = 'right'
    
  def DeclareCollision(self, directions):
    if (directions['right'] and self.direction == 'right') :
      self.direction = 'left'
    if (directions['left'] and self.direction == 'left') :
      self.direction = 'right'
    Npc.DeclareCollision(self, directions)



