import pygame

class Cardioid:
    def __init__(self, app):
        pass
    
    def draw(self):
        pass

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode([1600, 900])
        self.clock = pygame.time.Clock()
        self.cardioid = Cardioid(self)
        
    def draw(self):
        self.screen.fill('black')
        self.cardioid.draw()
        pygame.display.flip()
        
    def run(self):
        run = True
        while run:
            self.draw()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    run = False
            self.clock.tick(60)
            