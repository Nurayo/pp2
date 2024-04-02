# Importing necessary libraries
import pygame
import random

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Speed constant
SPEED = 5

# Coin class definition
class Coin:
    def __init__(self):
        # Coin dimensions
        self.WIDTH = 20
        self.ASPECT_RATIO = 1
        self.height = self.WIDTH / self.ASPECT_RATIO
        
        # Loading coin image and scaling it
        self.image = pygame.image.load("racer/pictures/coin.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.height))
        
        # Getting rectangle coordinates
        self.rect = self.image.get_rect()
        
        # Setting initial position
        self.rect.center = self.random_position()
        
        # Setting movement speed
        self.MOVE_SPEED = SPEED
        
    # Method to get random position for the coin
    def random_position(self):
        y = int(-self.height)
        x = random.randint(10, SCREEN_WIDTH - 10 - self.rect.width)
        return x, y
    
    # Method to move the coin
    def move(self):
        self.rect.move_ip(0, self.MOVE_SPEED)
        # If the coin is off the screen, reinitialize it
        if(self.rect.top > SCREEN_HEIGHT):
            self.__init__()
            
    # Method to draw the coin on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
