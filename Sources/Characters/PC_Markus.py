import pygame
from Sources.Pc import Pc
from Sources.Projectiles.PR_Fireball import PR_Fireball
from Sources.pg_functions import correctedBlit

class PC_Markus(Pc):

  'Base class for markus'

  def __init__(self, screen, initialPosition=[0,0]):
    Pc.__init__(self,screen, "Markus", initialPosition)

    # General combat arguments
    self.maxHp = 2
    self.currentHp = 2 

    # Attack related arguments
    self.framesCharged = 0

    # X movement related arguments
    self.xMaxSpeed = 13
    self.xSlowDown = self.xMaxSpeed/25.0
    self.xAcceleration = self.xMaxSpeed/20.0

    # Jump related arguments
    self.numberOfJumps = 2
    self.gravity = 0.375 
    self.jumpSpeed = 4.5
    self.yMaxSpeed = 7.5
    self.jumpAcceleration = 1.1
    self.maxAccelerationFrames = 10

    # Spirit sprite related arguments
    self.spiritImage = pygame.image.load("Sprites/Characters/Pc/Markus/Markus_spirit.png")
    self.spiritImageReverse = pygame.transform.flip(self.spiritImage, True, False) 
    self.displayTamponSize = 3
    self.lastPositions = []
    self.lastDirections = []
    
    # Fireball sprite
    self.chargingFireballSpriteList = []
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_1.png"))
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_2.png"))
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_3.png"))
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_4.png"))
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_5.png"))
    self.chargingFireballSpriteList.append(pygame.image.load("Sprites/Projectiles/Fireball/Fireball_charge_6.png"))

    self.frameToSpriteList = [5,10,30,60,120,240,400]
    self.spriteNumber = 0

    for i in range(self.displayTamponSize):
      self.lastPositions.append(self.position)
      self.lastDirections.append(self.lastDirections)
    # General character arguments

  def Attack(self, projectileList) :
    self.framesCharged = self.framesCharged + 1

  def Act(self, actions, projectileList) :
    if not actions['attack'] and self.framesCharged > 0 :

      characterPosition = self.GetPosition()
      characterSize = self.GetSize()
      
      fireballPosition = [0,0]
      
      if self.direction == 'right':
        fireballPosition[0] = characterPosition[0] + characterSize[0]
      if self.direction == 'left':
        fireballPosition[0] = characterPosition[0] - self.chargingFireballSpriteList[self.spriteNumber].get_width() + 15

      fireballPosition[1] = characterPosition[1] - 15


      projectileList.append(PR_Fireball(self.screen, "Markus", self,  self.direction, self.spriteNumber, self.framesCharged))
      self.framesCharged = 0 
      self.spriteNumber = 0 
    Pc.Act(self, actions, projectileList)

  def Move(self, movements):
    lastFrameDirection = self.direction
    Pc.Move(self, movements)

  def Display(self, cameraPosition, active = True):
    if not self.dead and active :
      del self.lastPositions[0]
      self.lastPositions.append(self.position)
      del self.lastDirections[0]
      self.lastDirections.append(self.direction)
      for i in range(self.displayTamponSize):
        if self.lastDirections[i] == 'right':
          correctedBlit(self.screen, self.spiritImageReverse,self.lastPositions[i], cameraPosition)
        if self.lastDirections[i]  == 'left':
          correctedBlit(self.screen, self.spiritImage,self.lastPositions[i], cameraPosition)
    if not active :
      for i in range(self.displayTamponSize):
        self.lastPositions[i] =  self.position
        self.lastDirections[i] = self.lastDirections
    
    characterPosition = self.GetPosition()
    characterSize = self.GetSize()
    fireballPosition = [0,0]
    for i, chargingFireballSprite in enumerate(self.chargingFireballSpriteList) :
      if self.framesCharged >= self.frameToSpriteList[i] and ( (i == len(self.chargingFireballSpriteList) - 1) or  (self.framesCharged <= self.frameToSpriteList[i+1]) ) :
        spriteSize = [chargingFireballSprite.get_width(), chargingFireballSprite.get_height()]
        fireballPosition[1] = characterPosition[1] + (characterSize[0] - spriteSize[0]) / 2
        if self.direction == 'right' :
          fireballPosition[0] = characterPosition[0] + characterSize[0]
        if self.direction == 'left' :
          fireballPosition[0] = characterPosition[0] - spriteSize[0]
        correctedBlit(self.screen, chargingFireballSprite, fireballPosition, cameraPosition)
        self.spriteNumber = i 
    Pc.Display(self, cameraPosition, active)
