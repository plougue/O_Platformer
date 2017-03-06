import pygame
def blit_alpha(target, source, location, opacity):
  x = location[0]
  y = location[1]
  temp = pygame.Surface((source.get_width(), source.get_height())).convert()
  temp.blit(target, (-x, -y))
  temp.blit(source, (0, 0))
  temp.set_alpha(opacity)        
  target.blit(temp, location)

def correctedBlit(screen, image, position, cameraPosition) :
  screenSize = screen.get_size()
  imageSize = [image.get_width(), image.get_height()]
  blitPosition = [0,0]
  blitPosition[0] = position[0] - cameraPosition[0]
  blitPosition[1] = position[1] - cameraPosition[1]
  if ( blitPosition[0] >= 0 or blitPosition[0] + imageSize[0] <= screenSize[0] ) \
    and (blitPosition[1] >= 0 or blitPosition[1] + imageSize[1] <= screenSize[1]) :
    screen.blit(image, blitPosition)
