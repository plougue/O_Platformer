
from Pc import *
from Npc import *

class World:
  'Base class for the world of the game'
  def __init__(self, resolution, color, characterName, fps):
    self.resolution = resolution
    self.gravity = 1
    self.background = color
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
    self.screen.fill(self.background)
    self.pc = Pc(self.screen, self.characterName)
    self.pc.blit()
    self.npcList.append(Npc(self.screen, "Appendix1"))
    pygame.display.flip()
    stayInLoop = 1
    pygame.key.set_repeat(400,30)
    clock = pygame.time.Clock()
    while stayInLoop:
      clock.tick(50)
      movementsKeys = {'left' : 0, 'right' : 0, 'up' : 0, 'down' : 0}
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
      
      self.screen.fill(self.background)
      for npc in self.npcList:
        npc.Move(self.resolution)
        self.CheckCollisions(npc, 'Npc')
        npc.blit()
      self.pc.Move(movementKeys, self.resolution)
      self.CheckCollisions(self.pc, 'Pc')
      self.pc.blit()
      pygame.display.flip()
  def CheckCollisions(self, character, characterType):
    charPosition = character.GetPosition()
    charSize = character.GetSize()
    collision = {'up' : False, 'down' : False,'left' : False,'right' : False}
    if(charPosition[0] + charSize[0] > self.resolution[0]):
      charPosition[0] = self.resolution[0] - charSize[0]
      collision['right'] = True
    if(charPosition[1] + charSize[1] > self.resolution[1]):
      charPosition[1] = self.resolution[1] - charSize[1]
      collision['down'] = True
    if(charPosition[0] < 0):
      charPosition[0] = 0
      collision['left'] = True
    if(charPosition[1] < 0):
      charPosition[1] = 0
      collision['up'] = True
    character.DeclareCollision(collision) 
    character.SetPosition(charPosition)
#  def MakeCollision(self, charPosition, charSize) :
#    if charPosition[0] + charSize[0] > self.Resolution : 
#     charPosition[0] = self.Resolution - charSize[0]
#    if charPosition[1] + charSize[1] > self.Resolution : 
#      charPosition[1] = self.Resolution - charSize[1]
