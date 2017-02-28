
from Pc import *
from Npc import *
from Obstacle import *

class World:
  'Base class for the world of the game'
  def __init__(self, resolution, backgroundImage, characterName, fps):
    self.resolution = resolution
    self.gravity = 1
    self.background = pygame.image.load("Sprites/Backgrounds/"+ backgroundImage+".png")
    self.background = pygame.transform.scale(self.background, resolution)
    print(self.background.get_rect())
    self.screen = 0 # has to be initialized in the mainLoop() method
    self.pc = 0 # has to beinitialized in the mainiLoop() method
    self.npcList = []
    self.obstacleList = []
    self.gravity = 1
    self.characterName = characterName
    self.fps = fps
  def MainLoop(self):
    pygame.init()
    self.screen = pygame.display.set_mode(self.resolution)
#    self.screen.fill(self.background)

    self.InitiateObstacles()
    self.InitiateNpcs()
    self.pc = Pc(self.screen, self.characterName)
    self.pc.blit()
    pygame.display.flip()
    stayInLoop = 1
    pygame.key.set_repeat(400,30)
    clock = pygame.time.Clock()
    while stayInLoop:
      clock.tick(50)
      movementsKeys = {'left' : 0, 'right' : 0, 'up' : 0, 'sdown' : 0}
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          stayInLoop = 0
        else:
          keys = pygame.key.get_pressed()
          # Select the keys that are link to character movement
          movementKeys = {'left' : keys[pygame.K_LEFT],
          'right' : keys[pygame.K_RIGHT],
          'up' : keys[pygame.K_UP],
          'down' : keys[pygame.K_DOWN]}

          ### FOR TESTING : PRESSING A BRINGS YOU BACK TO YOUR SPAWN
          if keys[pygame.K_a]:
            charPosition = self.pc.GetPosition()
            charPosition[0] = 0
            charPosition[1] = 1
            self.pc.SetPosition(charPosition) 
#      self.screen.fill(self.background)
      self.screen.blit(self.background, [0,0])
      for npc in self.npcList:
        npc.Move(self.resolution)
        self.CheckCollisions(npc, 'Npc')
        npc.blit()
      self.pc.Move(movementKeys, self.resolution)
      self.CheckCollisions(self.pc, 'Pc')
      self.pc.blit()
      for obstacle in self.obstacleList:
        obstacle.blit()
      pygame.display.flip()

  # Checks if (position1, size1) is aligned to (position2, size2)
  def AreAligned(self,position1, size1, position2, size2) :
      if (position1 > position2 and position1 < position2 + size2) or (position1 + size1 > position2 and position1 + size1 < position2 + size2):
        return True
      else:
        return False

  def CheckCollisions(self, character, characterType):
    charPosition = character.GetPosition()
    charSize = character.GetSize()
    charLastFramePosition = character.GetLastFramePosition()
    collision = {'up' : False, 'down' : False,'left' : False,'right' : False}
    if (charPosition[0] + charSize[0] > self.resolution[0]) :
      charPosition[0] = self.resolution[0] - charSize[0]
      collision['right'] = True
    if (charPosition[1] + charSize[1] > self.resolution[1]) :
      charPosition[1] = self.resolution[1] - charSize[1]
      collision['down'] = True
    if (charPosition[0] < 0):
      charPosition[0] = 0
      collision['left'] = True
    if (charPosition[1] < 0):
      charPosition[1] = 0
      collision['up'] = True
    for currentObstacle in self.obstacleList :
      obstaclePosition = currentObstacle.GetPosition()
      obstacleSize = currentObstacle.GetSize()
      xAligned = self.AreAligned(charPosition[0], charSize[0], obstaclePosition[0], obstacleSize[0]) 
      yAligned = self.AreAligned(charPosition[1], charSize[1], obstaclePosition[1], obstacleSize[1]) 
      xLastFrameAligned = self.AreAligned(charLastFramePosition[0], charSize[0], obstaclePosition[0], obstacleSize[0]) 
      yLastFrameAligned = self.AreAligned(charLastFramePosition[1], charSize[1], obstaclePosition[1], obstacleSize[1]) 
      # Collision
      if xAligned and yAligned : 
        # X collision
        if yLastFrameAligned :
          if charPosition[0] >= charLastFramePosition[0]:
            charPosition[0] = obstaclePosition[0] - charSize[0]
            collision['right'] = True
          elif charPosition[0] < charLastFramePosition[0]:
            charPosition[0] = obstaclePosition[0] + obstacleSize[0]
            collision['left'] = True
        # Y collision
        if xLastFrameAligned :
          if charPosition[1] >= charLastFramePosition[1]:
            charPosition[1] = obstaclePosition[1] - charSize[1]
            collision['down'] = True
          elif charPosition[1] < charLastFramePosition[1]:
            charPosition[1] = obstaclePosition[1] + obstacleSize[1]
            collision['up'] = True
    character.DeclareCollision(collision) 
    character.SetPosition(charPosition)
 
  def InitiateNpcs(self):
    self.npcList.append(Npc(self.screen, "Appendix1"))
    self.npcList.append(Npc(self.screen, "SploshyMan",[200,400]))
    self.npcList.append(Npc(self.screen, "Appendix1",[500,500]))

  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,460], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[800,300], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[400,300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,100], [10,3]))
