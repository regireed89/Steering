
'''EXAMPLE MAIN'''
from concretegame import ConcreteGame
from astargame import AstarGame 
import agent
import pygame

pygame.init()

def main():
    '''main execution func'''
    game = ConcreteGame("bob")
    # make gameobjects to participate in game
    game.__init__("bob")
    target = game.target
    game.addtobatch(target)
    game.draw()
    game.run()


if __name__ == "__main__":
    main()
