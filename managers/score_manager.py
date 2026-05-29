class ScoreManager:
    def __init__(self):
        self.score = 0

    def add_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score
