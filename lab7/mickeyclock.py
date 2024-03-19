import pygame
from datetime import datetime

pygame.init() 
screen_width = 500
screen_height = 500
center = (screen_width / 2, screen_height / 2)
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()

bg = pygame.image.load('main-clock.jpeg')
bg_width = 500
bg_height = 500
bg_x_pos = (screen_width / 2 - bg_width / 2)
bg_y_pos = (screen_height / 2 - bg_height / 2)

big_arrow = pygame.image.load('seconds.png')
big_arrow_width = 35
big_arrow_aspect_ratio = 0.13
big_arrow_height = big_arrow_width / big_arrow_aspect_ratio
big_arrow = pygame.transform.scale(big_arrow, (big_arrow_width, big_arrow_height))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = center

small_arrow = pygame.image.load('minutes.png')
small_arrow_width = 60
small_arrow_aspect_ratio = 0.35
small_arrow_height = small_arrow_width / small_arrow_aspect_ratio
small_arrow = pygame.transform.scale(small_arrow, (small_arrow_width, small_arrow_height))

small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = center

running = True
while running:  
  for event in pygame.event.get():
    if event.type == pygame.quit:
      running = False

  screen.fill(white)
  screen.blit(bg, (bg_x_pos, bg_y_pos))
  
  angle = datetime.now().second * -6
  rotated_big_arrow = pygame.transform.rotate(big_arrow, angle)
  rotated_big_arrow_rect = rotated_big_arrow.get_rect()
  rotated_big_arrow_rect.center = big_arrow_rect.center
  screen.blit(rotated_big_arrow, rotated_big_arrow_rect)

  _angle = datetime.now().minute * -6
  rotated_small_arrow = pygame.transform.rotate(small_arrow, _angle)
  rotated_small_arrow_rect = rotated_small_arrow.get_rect()
  rotated_small_arrow_rect.center = small_arrow_rect.center
  screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

  pygame.display.flip()
  clock.tick(fps)