class Question:
    def __init__(self, question_text, answers, correct_answer):
        """correct answer has to be pygame keyboard constant"""
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer
