from World import *
  

worldResolution = [1000,600]
worldColor = [255,255,255]
worldCharacterName = "Markus"
worldFps = 60
gameWorld = World(worldResolution, worldColor, worldCharacterName, worldFps)
gameWorld.MainLoop()

'''
import pygame 

pygame.init()
screen = pygame.display.set_mode((1000,600))


# fills the screen with white
screen.fill(background_color)


# loads shroomy with transparency
shroomy = pygame.image.load("Sprites/Characters/Pc/Shroomy/shroomy_idle.png").convert_alpha()
shroomy_position = shroomy.get_rect()
screen.blit(shroomy, shroomy_position)


# sends what's drawn in the buffer in the actual monitor
pygame.display.flip()
stayInLoop = 1

# set the key to repeat themselves when pressed continuously
pygame.key.set_repeat(400, 30)
pixelPerMove = 10
while stayInLoop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:    # If the QUIT events occur we end the loop
      stayInLoop = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        shroomy_position = shroomy_position.move(0,pixelPerMove)
      if event.key == pygame.K_UP:
        shroomy_position = shroomy_position.move(0,-pixelPerMove)
      if event.key == pygame.K_RIGHT:
        shroomy_position = shroomy_position.move(pixelPerMove,0)
      if event.key == pygame.K_LEFT:
        shroomy_position = shroomy_position.move(-pixelPerMove,0)

  # re-drawing the screen
  screen.fill(background_color)
  screen.blit(shroomy, shroomy_position)

  # validating changes in the buffer
  pygame.display.flip()
  '''
