#!/usr/bin/python
import curses
import logging

import Game
import Level
import Menu
import Snake


def init():
    global game
    # on initialise la fenetre curses
    curses.initscr()
    win = curses.newwin(30, 80, 0, 0)
    curses.noecho()
    curses.curs_set(0)
    win.nodelay(0)

    logging.basicConfig(filename='snake.log', level=logging.INFO)
    # creation du niveau
    level = Level.create(0, 'levels.txt')
    # creation du snake
    snake = Snake.create(35, 15, 0, 2)

    # creation du food
    food = [10, 10]

    # creation du menu
    menu = Menu.create(
        'Change name',
        'Change Difficulty',
        'Select level',
        'play',
        'quit Game'
    )

    # definition de l'etat du programme
    state = 'menu'

    # definition du nom du joueur
    name = 'player1'

    # definition de la difficulte
    difficulty = 2

    # creation de la variable de type game
    game = Game.create(menu, level, snake, food, win, state, name, difficulty)


def run(game):
    while Game.getState(game) != 'quitProgram':
        logging.info('%s', Game.getState(game))
        show(game)
        interact(game)
    quitProgram()
    return


def show(game):
    if Game.getState(game) == 'menu':
        Menu.show(game)
    elif Game.getState(game) == 'game':
        Game.show(game)
    return


def interact(game):
    if Game.getState(game) == 'menu':
        Menu.interact(game)
    elif Game.getState(game) == 'game':
        Game.interact(game)
    elif Game.getState(game) == 'quitGame':
        Game.quitGame(game)
    return


def quitProgram():
    curses.echo()
    curses.endwin()
    return

#
init()
run(game)
