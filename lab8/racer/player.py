# Importing necessary library
import pygame

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Speed constant
SPEED = 5

# Player class definition
class Player:
    def __init__(self):
        # Player dimensions
        self.WIDTH = 60
        self.ASPECT_RATIO = 0.5
        self.height = self.WIDTH / self.ASPECT_RATIO
        
        # Loading player image and scaling it
        self.image = pygame.image.load("racer/pictures/Player.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.height))
        
        # Getting rectangle coordinates
        self.rect = self.image.get_rect()
        
        # Setting initial position
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        
        # Setting movement speed
        self.MOVE_SPEED = SPEED * 3
        
    # Method to move the player
    def move(self):
        # Getting pressed keys
        keys = pygame.key.get_pressed()
        # Moving left
        if keys[pygame.K_LEFT]:
            if(self.rect.left > 0):
               self.rect.move_ip(-self.MOVE_SPEED, 0)
        # Moving right
        if keys[pygame.K_RIGHT]:
            if(self.rect.right < SCREEN_WIDTH):
               self.rect.move_ip(self.MOVE_SPEED, 0)
    
    # Method to draw the player on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
