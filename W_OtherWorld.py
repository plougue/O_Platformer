from Pc import *
from Npc import *
from NPC_TreeMonster import *
from NPC_Gargoyle import *
from NPC_SploshyMan import *
from Obstacle import *
from World import *

class W_OtherWorld(World):
  'Base class for the world of the game'
  def __init__(self):
    World.__init__(self, [1366,700], "DarkGrey", "Markus", 60)
 
  def InitiateNpcs(self):
    self.npcList.append(NPC_SploshyMan(self.screen,[500,0]))
    self.npcList.append(NPC_SploshyMan(self.screen,[600,0]))
    self.npcList.append(NPC_Gargoyle(self.screen,[700,0]))
    self.npcList.append(NPC_TreeMonster(self.screen, [800,0]))
#    self.npcList.append(NPC_TreeMonster(self.screen, [500,0], 'left'))
    self.npcList.append(NPC_Gargoyle(self.screen,[900,0]))
    return 1
  def InitiateObstacles(self):
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,460], [4,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[300,360], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[600,300], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[1000,360], [2,2]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[1000,150], [6,2]))
    self.obstacleList.append(Obstacle(self.screen,"BricWall",[0,100], [10,3]))
    self.obstacleList.append(Obstacle(self.screen,"DarkBricWall",[0,650], [50,2]))
    return 1
    
