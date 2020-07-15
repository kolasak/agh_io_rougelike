import pygame
from gameplay.Question import Question
from gameplay.QuestionContainer import QuestionContainer


def keyboard_control(actions):
    """Function to control keyboard input
    actions: dict (keyboard_key -> action (callable))
    example usage:
    keyboard_control({pygame.K_SPACE: lambda: print('foo')})"""
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in actions.keys():
                    actions[event.key]()
                    key_pressed = True


def load_random_question():
    return QuestionContainer.getInstance().pop_random_question()
