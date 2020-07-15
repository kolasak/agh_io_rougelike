from random import random
from numpy import random as rand

class QuestionContainer:
    __instance = None

    def __init__(self):
        if QuestionContainer.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            QuestionContainer.__instance = self
        self.question_container = []
        self.question_container_backup = []

    @staticmethod
    def getInstance():
        if QuestionContainer.__instance is None:
            QuestionContainer()
        return QuestionContainer.__instance

    @staticmethod
    def pop_random_question():
        if not QuestionContainer.getInstance().question_container:
            QuestionContainer.getInstance().fill_container(QuestionContainer.getInstance())
        while QuestionContainer.getInstance().question_container:
            question = QuestionContainer.getInstance().question_container.pop(rand.randint(0,len(QuestionContainer.getInstance().question_container)-1))
            if not question.is_used:
                return question

    @staticmethod
    def add_question(question):
        QuestionContainer.getInstance().question_container.append(question)

    def fill_container(self):
        self.question_container = [None] * len(self.question_container_backup)
        for i in range(0, len(self.question_container_backup)):
            self.question_container[i] = self.question_container_backup[i]
        self.shuffle_questions(self)

    @staticmethod
    def shuffle_questions(self):
        random.shuffle(self.question_container)
