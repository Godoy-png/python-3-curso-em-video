import pygame
pygame.init()
musica = ''

pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.event.wait()
