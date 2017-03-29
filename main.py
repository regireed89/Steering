
'''EXAMPLE MAIN'''
from concretegame import ConcreteGame
import agent
import pygame


def main():
    '''main execution func'''
    game = ConcreteGame("the game")
    # make gameobjects to participate in game
    tom = agent.Agent()
    game.addtobatch(tom)
    game.run()

if __name__ == "__main__":
    main()
