class Question:
    def __init__(self, question_text, answers=None, correct_answer="", is_used=False):
        """correct answer has to be pygame keyboard constant"""
        if answers is None:
            answers = []
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer
        self.is_used = is_used

    @staticmethod
    def add_answer(question, answer):
        question.answers.append(answer)

    @staticmethod
    def add_correct(question, answer):
        question.correct_answer = answer
