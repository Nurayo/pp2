import pygame
import sys

pygame.init()

songs = ['song1.mp3', 'song2.mp3', 'song3.mp3']
current_song = 0

WIDTH, HEIGHT = 400, 300

pygame.mixer.init()
pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pygame.mixer.music.unpause()
    if keys[pygame.K_DOWN]:
        pygame.mixer.music.pause()
    if keys[pygame.K_LEFT]:
        current_song = (current_song - 1) % len(songs)
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()
    if keys[pygame.K_RIGHT]:
        current_song = (current_song + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()