class User:
    def __init__(self, username, score = 0):
        self.username = username
        self.score = score

    def __str__(self):
        return f"{self.username} masz {self.score} pkt"

    def add_score(self, score):
        self.score += score

    def remove_score(self, score):
        self.score -= score
