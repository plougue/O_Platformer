import pygame

class Character:
  'Base class for the playable character'
  def __init__(self, screen, characterName, spritePath, initialPosition=[0,0]):
  
    # General character arguments
    self.screen = screen
    self.name = characterName
    self.image = pygame.image.load(spritePath).convert_alpha()
    self.position = self.image.get_rect()
    self.position[0] = initialPosition[0]
    self.position[1] = initialPosition[1]
    self.lastFramePosition = self.position

    self.spriteDirection = 'left'

    # General combat arguments
    self.dead = 0
    self.maxHp = 6
    self.currentHp = 6
    self.invulnerabilityFrameDuration = 40
    self.invulnerabilityRemainingFrames = 0
    self.projectileImmunityList = []
    self.subjectToProjectileImmunity = True
    
    # X-movement related arguments 
    self.xSpeed = 0
    self.xMaxSpeed = 15
    self.xStartAcceleration = 3   # How much speed the first input gives
    self.xSlowDown = self.xMaxSpeed/25.0    # How quickly the character slows down
    self.xAcceleration = self.xMaxSpeed/20.0    # How quickly he accelerates
    
    # Gravity
    self.gravity = 0.5
    
    # Jump related arguments
    self.numberOfJumps = 3
    self.ySpeed = 0
    self.yMaxSpeed = 10
    self.jumpSpeed = 6    # Initial jump speed
    self.jumpAcceleration = 1/0.7   # How fast the character gains speed until maxJumpSpeed
    self.maxAccelerationFrames = 7
    self.accelerationFramesRemaining = 0
    self.canAccelerateJump = 1   # [BOOL] can the character accelerate his jump ? 
    self.remainingJumps = 0    # [BOOL] can the character jump ?
    self.nextJumpsRatio = 0.8   # How reduced is the speed given by the jumps after the first ?
    self.jumpFreeze = 0   # The jump is frozen until the up command is cancelled
    self.direction = 'right'
    self.lookingDirection = 'right'
    
  #############################################################################
  ##    CHANGES THE STATE ACCORDINGLY IF A COLLISION OCCURS                  ##
  #############################################################################
  def DeclareCollision(self, directions):
    if (directions['down'] and self.ySpeed > 0) or (directions['up'] and self.ySpeed < 0) :
      self.ySpeed = 0
    if (directions['left'] and self.xSpeed < 0)  or (directions['right'] and self.xSpeed > 0) : 
      self.xSpeed = 0
      
    if directions['down']:
      self.remainingJumps = self.numberOfJumps
      self.canAccelerateJump = 0 
      self.accelerationFramesRemaining = self.maxAccelerationFrames

    # Basically, if the character falls down he loses a jump
    if self.remainingJumps == self.numberOfJumps and not(directions['down']): 
      self.remainingJumps = self.remainingJumps - 1

  def blit(self):
    if self.direction != self.spriteDirection :
      self.screen.blit(pygame.transform.flip(self.image, True, False), self.position)
    else :
      self.screen.blit(self.image, self.position)

  def DisplayHp(self):
    totalLineLength = 50
    linePosition = [0,0]
    characterPosition =  self.GetPosition()
    characterSize = self.GetSize()
    linePosition[0] = characterPosition[0] + (characterSize[0] - totalLineLength) / 2 
    linePosition[1] = characterPosition[1] - 30
    greenLineLength = totalLineLength * (float(self.currentHp) / self.maxHp)
    greenLineEndPosition = [0,0]
    lineEndPosition = [0,0]
    greenLineEndPosition[1] = linePosition[1]
    lineEndPosition[1] = linePosition[1]
    greenLineEndPosition[0] = linePosition[0] + greenLineLength
    lineEndPosition[0] = linePosition[0] + totalLineLength
    if self.currentHp > 0 :
      greenLine = pygame.draw.line(self.screen, [0,200,0], linePosition, greenLineEndPosition,10)
    if self.currentHp < self.maxHp :
      redLine = pygame.draw.line(self.screen, [200,0,0], greenLineEndPosition, lineEndPosition,10)
    
  def Act(self, actions, projectileList) :
    if(actions['attack']) :
      self.Attack(projectileList)

  def Move(self,movements) :

    self.lastFramePosition = self.position

    ### Change frame counters
    if self.invulnerabilityRemainingFrames > 0 :
      self.invulnerabilityRemainingFrames = self.invulnerabilityRemainingFrames - 1

    ### X MOVEMENt MANAGEMENT
    if(movements['left']  and (not(movements['right']))):
      if(self.xSpeed >= 0):
        self.xSpeed -= self.xStartAcceleration
      self.xSpeed -= self.xAcceleration
    elif(movements['right'] and (not(movements['left']))):
      if(self.xSpeed <= 0):
        self.xSpeed += self.xStartAcceleration
      self.xSpeed += self.xAcceleration 
    elif(self.xSpeed > 0):
      self.xSpeed -= self.xSlowDown
      if(self.xSpeed < 0): # should never slow down as much as to change direction
        self.xSpeed = 0
    elif(self.xSpeed < 0):
      self.xSpeed += self.xSlowDown
      if(self.xSpeed > 0): # should never slow down as much as to change direction
        self.xSpeed = 0

    if(self.xSpeed > self.xMaxSpeed):
      self.xSpeed = self.xMaxSpeed
    if(self.xSpeed < -self.xMaxSpeed):
      self.xSpeed = -self.xMaxSpeed 
      
    ### JUMPING MANAGEMENT

    # Once you stop accelerating it's too late
    if not(movements['up']):
      self.jumpFreeze = 0
      if self.remainingJumps < self.numberOfJumps :
        self.canAccelerateJump = 0
        self.accelerationFramesRemaining = 0
    if self.accelerationFramesRemaining == 0:
      self.canAccelerateJump = 0
    if(movements['up'] and self.remainingJumps > 0 and not(self.canAccelerateJump) and not(self.jumpFreeze)):
      if (self.remainingJumps < self.numberOfJumps) :
        self.ySpeed = -self.nextJumpsRatio * self.jumpSpeed
      else :
        self.ySpeed = -self.jumpSpeed
      self.remainingJumps = self.remainingJumps - 1
      self.canAccelerateJump = 1 
      self.accelerationFramesRemaining = self.maxAccelerationFrames
      self.jumpFreeze = 1
    elif(movements['up'] and self.ySpeed < 0 and self.canAccelerateJump):
      self.ySpeed -= self.jumpAcceleration
      self.accelerationFramesRemaining = self.accelerationFramesRemaining - 1
    ## GRAVITY
    self.ySpeed += self.gravity
    
    ## MODIFY POSITION
    self.position = self.position.move(self.xSpeed,self.ySpeed) 
    if movements['right'] and self.lookingDirection == 'left':
      self.lookingDirection = 'right'
      self.direction = 'right'
    if movements['left'] and self.lookingDirection == 'right':
      self.lookingDirection = 'left'
      self.direction = 'left'
 
  def Attack(self, projectileList):
    return 0
  
  def TakeDamage(self, damageValue):
    if self.invulnerabilityRemainingFrames == 0 :
      if damageValue >= self.currentHp :
        self.Die()
      else :
        self.currentHp = self.currentHp - damageValue
      self.invulnerabilityRemainingFrames = self.invulnerabilityFrameDuration

  def Die(self):
    self.currentHp = 0
    self.dead = 1

  def GetLastFramePosition(self):
    return self.lastFramePosition

  def GetPosition(self):
    return self.position
  
  def GetSize(self):
    return (self.image.get_width(), self.image.get_height())
  
  def GetName(self):
    return self.name

  def SetPosition(self,newPosition):
    self.position[1] = newPosition[1]
    self.position[0] = newPosition[0]

  def AddProjectileImmunity(self,projectile) :
    if(self.subjectToProjectileImmunity) :
      self.projectileImmunityList.append(projectile)

  def IsImmuneToProjectile(self,projectile) :
    return (projectile in self.projectileImmunityList)

  def GetMaxHp(self) :
    return self.maxHp

  def GetCurrentHp(self) :
    return self.currentHp

  def IsDead(self):
    return self.dead
