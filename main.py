import pygame

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode([1600, 900])
        self.clock = pygame.time.Clock()
        
    def draw(self):
        self.screen.fill('black')
        pygame.display.flip()
        