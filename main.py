import pygame
import math

class Cardioid:
    def __init__(self, app):
        self.app = app
        self.radius = 400
        self.num_lines = 200
        self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height // 2
    
    def draw(self):
        x = [0,0]
        y = [0,0]
        
        for i in range(self.num_lines):
            theta = (2 * math.pi / self.num_lines) * i
            x[0] = int(self.radius * math.cos(theta)) + self.translate[0]
            y[0] = int(self.radius * math.sin(theta)) + self.translate[1]
            
            x[1] = int(self.radius * math.cos(2 * theta)) + self.translate[0]
            y[1] = int(self.radius * math.sin(2 * theta)) + self.translate[1]
            
            pygame.draw.aaline(self.app.screen, 'green', (x[0], y[0]), (x[1], y[1]))

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
App().run()            