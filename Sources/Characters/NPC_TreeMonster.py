import pygame
import Sources.pg_functions
from Sources.Npc import Npc
from Sources.Character import Character


class NPC_TreeMonster(Npc):

  'Base class for TreeMonster'

  def __init__(self, screen, initialPosition=[0,0], direction = 'right'):
    Npc.__init__(self,screen, "TreeMonster", initialPosition)

    # General combat arguments
    self.maxHp = 300
    self.currentHp = 300
    self.invulnerabilityFrameDuration = 0
    self.subjectToProjectileImmunity = False

    self.direction = direction
    # X movement related arguments
    self.xMaxSpeed = 5
    self.xSlowDown = self.xMaxSpeed/25.0
    self.xAcceleration = self.xMaxSpeed/20.0

    # Jump related arguments
    self.numberOfJumps = 0

    # Spirit sprite related arguments
    self.displayTamponSize = 3
    self.framesBetweenTampon = 1
    self.lastPositions = []
    self.lastDirections = []

    self.framesBetweenHeal = 4 # How much frames between two heals ?
    self.healRemainingFrames = 4 # How much frames untill heal ?
    self.healAmount = 1 # How much heal ?
    
    self.spriteDirection = 'left'
    for i in range(self.displayTamponSize * self.framesBetweenTampon):
      self.lastPositions.append(self.position)
      self.lastDirections.append(self.lastDirections)
    # General character arguments

  def DeclareCollision(self, directions):
    Npc.DeclareCollision(self, directions)


  def Act(self, projectileList):
    Npc.Act(self, projectileList) 
    if(self.healRemainingFrames == 0) :
      self.healRemainingFrames = self.framesBetweenHeal
      maxHealAmount = self.maxHp - self.currentHp
      self.currentHp = self.currentHp + min((maxHealAmount, self.healAmount))
    else :
      self.healRemainingFrames = self.healRemainingFrames - 1

  def Move(self):
    if self.direction == 'right':
      Character.Move(self, {'left':0, 'right':1, 'up':0, 'down':0})
    if self.direction == 'left':
      Character.Move(self, {'left':1, 'right':0, 'up':0, 'down':0})

