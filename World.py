
from PC_Markus import *
from PC_Yvan import *
from PC_Luc import *
from PR_Shuriken import *
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
    self.projectileList = []
    self.characterPool = {}
    self.gravity = 1
    self.characterName = characterName
    self.fps = fps
    self.actualFps = fps # will be calculated every frame

    # HUD IMAGES
    self.fullHeartImage = pygame.image.load("Sprites/Hud/Health/FullHeart.png")
    self.emptyHeartImage = pygame.image.load("Sprites/Hud/Health/EmptyHeart.png")

  def MainLoop(self):
    pygame.init()
    self.screen = pygame.display.set_mode(self.resolution)

    self.InitiateObstacles()
    self.InitiateNpcs()


    self.characterPool = {"Markus" : PC_Markus(self.screen), "Yvan" : PC_Yvan(self.screen), "Luc" : PC_Luc(self.screen)}
    self.pc = self.characterPool[self.characterName]
  
    self.pc.blit()
    pygame.display.flip()
    stayInLoop = 1
    pygame.key.set_repeat(400,30)
    clock = pygame.time.Clock()
    while stayInLoop:
      frameDuration = clock.tick(self.fps)
      self.actualFps = 1000.0/frameDuration
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
          actionKeys = {'attack' : keys[pygame.K_LSHIFT]}

          ### FOR TESTING : PRESSING A BRINGS YOU BACK TO YOUR SPAWN
          if keys[pygame.K_a]:
            charPosition = self.pc.GetPosition()
            charPosition[0] = 0
            charPosition[1] = 1
            self.pc.SetPosition(charPosition) 
          if keys[pygame.K_z]:
            lastWasCharacter = 0
            firstKey = 0
            print(self.characterName)
            print("-------------")
            for key,value in self.characterPool.items() :
              print(key)
              print(lastWasCharacter)
              if not(firstKey):
                firstKey = key
              if key == self.characterName :
                lastWasCharacter = 1
              elif lastWasCharacter:
                self.pc = self.characterPool[key]
                self.characterName = key
                lastWasCharacter = 0
            if lastWasCharacter:
              print(firstKey)
              self.pc = self.characterPool[firstKey] 
              self.characterName = firstKey
      self.screen.blit(self.background, [0,0])

      ## DEALING WITH NPCS
      deadNpcList = []
      for npc in self.npcList:
        npc.Move(self.resolution)
        self.CheckCollisions(npc, 'Npc')
        npc.blit()
        if npc.IsDead():
          deadNpcList.append(npc)
      for npcToRemove in deadNpcList :
        self.npcList.remove(npcToRemove)
      
      ## DEALING WITH PCS
      if not(self.pc.IsDead()) :
        self.pc.Move(movementKeys, self.resolution)
        self.pc.Act(actionKeys, self.resolution, self.projectileList)
        self.CheckCollisions(self.pc, 'Pc')
        self.pc.blit()
      
      ## DEALING WITH PROJECTILES
      toRemoveProjectileList = []
      for projectile in self.projectileList:
        projectile.Move(self.resolution)
        self.CheckCollisions(projectile, 'Projectile')
        projectile.blit()
        if projectile.IsToBeDeleted():
          toRemoveProjectileList.append(projectile)
      for projectileToRemove in toRemoveProjectileList :
        self.projectileList.remove(projectileToRemove)
      
      ## DEALING WITH OBSTACLES
      for obstacle in self.obstacleList:
        obstacle.blit()
      self.DisplayHud()
      pygame.display.flip()

  # Checks if (position1, size1) is aligned to (position2, size2)
  def AreAligned(self,position1, size1, position2, size2) :
      if (position1 > position2 and position1 < position2 + size2) or (position1 + size1 > position2 and position1 + size1 < position2 + size2) \
        or (position1 <= position2 and position1 + size1 >= position2 + size2):
        return True
      else:
        return False

  def CollidesWith(self, subjectItem, objectItem, changePosition = 0) :
      collisions = {'right' : False, 'left' : False, 'up' : False, 'down' : False}
      itemPosition = subjectItem.GetPosition()
      itemSize = subjectItem.GetSize()
      itemLastFramePosition = subjectItem.GetLastFramePosition()
      obstaclePosition = objectItem.GetPosition()
      obstacleSize = objectItem.GetSize()
      xAligned = self.AreAligned(itemPosition[0], itemSize[0], obstaclePosition[0], obstacleSize[0]) 
      yAligned = self.AreAligned(itemPosition[1], itemSize[1], obstaclePosition[1], obstacleSize[1]) 
      xLastFrameAligned = self.AreAligned(itemLastFramePosition[0], itemSize[0], obstaclePosition[0], obstacleSize[0]) 
      yLastFrameAligned = self.AreAligned(itemLastFramePosition[1], itemSize[1], obstaclePosition[1], obstacleSize[1]) 

      # Hard collision (object are imbricated)
      if xAligned and yAligned : 
        # X collision 
        if yLastFrameAligned :
          if itemPosition[0] >= itemLastFramePosition[0]:
            if changePosition :
              itemPosition[0] = obstaclePosition[0] - itemSize[0]
            collisions['right'] = True
          elif itemPosition[0] <= itemLastFramePosition[0]:
            if changePosition :
              itemPosition[0] = obstaclePosition[0] + obstacleSize[0]
            collisions['left'] = True
        # Y collision
        if xLastFrameAligned :
          if itemPosition[1] >= itemLastFramePosition[1]:
            if changePosition :
              itemPosition[1] = obstaclePosition[1] - itemSize[1]
            collisions['down'] = True
          elif itemPosition[1] <= itemLastFramePosition[1]:
            if changePosition :
              itemPosition[1] = obstaclePosition[1] + obstacleSize[1]
            collisions['up'] = True

      # Soft Collisions (objects are on top of each other)
      if yAligned and itemPosition[0] == obstaclePosition[0] - itemSize[0]:
        collisions['right'] = True
      if yAligned and itemPosition[0] == obstaclePosition[0] + obstacleSize[0]:
        collisions['left'] = True
      if xAligned and itemPosition[1] == obstaclePosition[1] - itemSize[1]:
        collisions['down'] = True
      if xAligned and itemPosition[1] == obstaclePosition[1] + obstacleSize[1]:
        collisions['up'] = True
      return collisions

  def CheckCollisions(self, item, itemType):
    if itemType == 'Projectile' and not(item.CanCollide()) :
      return 0
    itemPosition = item.GetPosition()
    itemSize = item.GetSize()
    itemLastFramePosition = item.GetLastFramePosition()
    collision = {'up' : False, 'down' : False,'left' : False,'right' : False}
    if (itemPosition[0] + itemSize[0] >= self.resolution[0]) :
      itemPosition[0] = self.resolution[0] - itemSize[0]
      collision['right'] = True
     # Has to be not strict because we want the player to stick to the ground for jumping purpose
    if (itemPosition[1] + itemSize[1] >= self.resolution[1]) : 
      itemPosition[1] = self.resolution[1] - itemSize[1]
      collision['down'] = True
    if (itemPosition[0] <= 0):
      itemPosition[0] = 0
      collision['left'] = True
    if (itemPosition[1] <= 0):               
      itemPosition[1] = 0
      collision['up'] = True

    for currentObstacle in self.obstacleList :
      currentCollision = self.CollidesWith(item, currentObstacle, True)
      collision['right'] = collision['right'] or currentCollision['right']
      collision['left'] = collision['left'] or currentCollision['left']
      collision['up'] = collision['up'] or currentCollision['up']
      collision['down'] = collision['down'] or currentCollision['down']
  
    if(itemType == 'Pc') :
      for currentNpc in self.npcList :
        npcCollision = self.CollidesWith(item, currentNpc, False)
        if (npcCollision['left'] or npcCollision['right'] or npcCollision['up'] or npcCollision['down']) :
          item.TakeDamage(1)
          print("taking damage")
          print(item.GetPosition())
          print(currentNpc.GetPosition())


    if(itemType == 'Pc' or itemType == 'Npc') :
      for currentProjectile in self.projectileList :
        projectileCollision = self.CollidesWith(item, currentProjectile, False)
        if(projectileCollision['left'] or projectileCollision['right'] or projectileCollision['up'] or projectileCollision['down']) :
          if(currentProjectile.GetOwnerName() != item.GetName()) :
            item.TakeDamage(currentProjectile.GetDamageDealt())

    item.DeclareCollision(collision) 
    item.SetPosition(itemPosition)
    
  def DisplayHud(self):
    heartHeight = self.fullHeartImage.get_height()
    heartWidth = self.fullHeartImage.get_width()
    for i in range(self.pc.GetMaxHp()) : 
      heartPosition = [0,0]
      heartPosition[0] = self.resolution[0] - 1.2 * heartWidth * (i + 1)
      if i >= self.pc.GetCurrentHp() :
        self.screen.blit(self.emptyHeartImage, heartPosition)
      else:
        self.screen.blit(self.fullHeartImage, heartPosition)
    if self.pc.IsDead() :
      self.screen.blit(self.pc.deathSprite, [self.resolution[0] - 50 -  self.pc.deathSprite.get_width(), 1.2 * heartHeight])
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myfont.render("fps: " + str(int(self.actualFps)), 1, [200,0,200])
    self.screen.blit(label, (0,0))


  def InitiateNpcs(self):
    self.npcList.append(Npc(self.screen, "Appendix1"))
    self.npcList.append(Npc(self.screen, "SploshyMan",[200,400]))
    self.npcList.append(Npc(self.screen, "Appendix1",[500,500]))
    return 0

  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,460], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[800,300], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[400,300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,100], [10,3]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,650], [40,2]))

    
