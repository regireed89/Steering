'''gametemplate.py'''

# from gameobject import GameObject
import agent
import pygame
import constants
if __name__ == '__main__':
    import main as Main
    Main.main()


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        pygame.init()
        self._fps = 30
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill((0, 0, 0))
        

    def startup(self):
        '''do startup routines'''
        return True

    def update(self):
        '''input and time'''
        
        return True

    def draw(self):
        '''base draw'''
        pygame.display.flip()
        self.screen.blit(self.surface, (0, 0))

    def shutdown(self):
        '''shutdown the game properly'''
        pygame.quit()
