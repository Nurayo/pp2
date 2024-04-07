import pygame
import player
import coin
import math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
SPEED = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.update()

clock = pygame.time.Clock()
running = True
player = player.Player()
coin = coin.Coin()
coins = 0
scroll = 0
speed = SPEED

font = pygame.font.SysFont("bahnschrift", 40)

# Loading background image and scaling it
background = pygame.image.load("racer/pictures/AnimatedStreet.png")
bg_aspect_ratio = background.get_width() / background.get_height()
background = pygame.transform.scale(background, (SCREEN_WIDTH, math.ceil(SCREEN_WIDTH / bg_aspect_ratio)))


copy = math.ceil(SCREEN_HEIGHT / background.get_height()) + 1

# Main game loop
while running:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Moving player and coin
    player.move()
    coin.move()
            
    # Scrolling background
    scroll = (scroll + speed // 1.5) % background.get_height()
    for x in range(copy):
        screen.blit(background, (0, scroll + (x - 1) * (background.get_height() - 1)))
        
    # Displaying coin count
    coin_cnt = font.render(str(coins), True, BLACK)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 60, 0, 60, 60))
    screen.blit(coin_cnt, (SCREEN_WIDTH - 50, 10))
    
    # Drawing player and coin
    player.draw(screen)
    coin.draw(screen)
    
    # Checking for collision between player and coin
    if player.rect.colliderect(coin.rect):
        coin.__init__()  # Reinitializing coin
        coins += 1  # Incrementing coin count
      
    # Updating display
    pygame.display.flip()
    clock.tick(FPS) 