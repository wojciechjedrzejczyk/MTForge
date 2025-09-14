class User:
    def __init__(self, name, password, score):
        self.name = name
        self.password = password
        self.score = score

    def add_score(self, score):
        self.score += score

