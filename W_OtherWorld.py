from Pc import *
from Npc import *
from NPC_TreeMonster import *
from NPC_Gargoyle import *
from NPC_SploshyMan import *
from Obstacle import *
from World import *

class W_OtherWorld(World):
  'Base class for the world of the game'
  def __init__(self, difficulty):
    World.__init__(self, [1366,700], [4000,2000], "DarkGrey", "Markus", 60)
    self.difficulty = difficulty
  def InitiateNpcs(self):
    self.npcList.append(NPC_SploshyMan(self.screen,[500,1300]))
    self.npcList.append(NPC_SploshyMan(self.screen,[600,1300]))
    self.npcList.append(NPC_Gargoyle(self.screen,[700,1300]))
    if self.difficulty == "Hard" :
      self.npcList.append(NPC_TreeMonster(self.screen, [800,1300]))
#    self.npcList.append(NPC_TreeMonster(self.screen, [500,0], 'left'))
      self.npcList.append(NPC_Gargoyle(self.screen,[900,1300]))
    return 1
  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,1300+250], [1,13]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[300,1300+360], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,1300+300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[1000,1300+360], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[1000,1300+150], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,1300+100], [10,3]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[0,1300+650], [200,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[2000,1300+350], [4,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[2400,1300+350], [1,1]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[1500,1300+250], [1,13]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[3000,1300+250], [1,13]))
    return 1
    
