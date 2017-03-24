
'''EXAMPLE MAIN'''
from concretegame import ConcreteGame
from astargame import AstarGame 


def main():
    '''main execution func'''
    game = AstarGame()
    # make gameobjects to participate in game
    game.__init__()
    game.run()


if __name__ == "__main__":
    main()
