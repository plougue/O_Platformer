import pygame
from Npc import Npc
from Character import Character

class NPC_Gargoyle(Npc):

  'Base class for Gargoyle'

  def __init__(self, screen, initialPosition=[0,0]):
    Npc.__init__(self,screen, "Gargoyle", initialPosition)

    # General combat arguments
    self.invulnerabilityFrameDuration = 200

    self.currentHp = 6
    self.maxHp = 6
    self.xMaxSpeed = 8
    self.gravity = 0.2

    # X movement related arguments
    self.spriteDirection = 'left'
    
  def DeclareCollision(self, directions):
    if (directions['right'] and self.direction == 'right') :
      self.direction = 'left'
    if (directions['left'] and self.direction == 'left') :
      self.direction = 'right'
    Npc.DeclareCollision(self, directions)



