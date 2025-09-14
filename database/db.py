from pathlib import Path

class Database:
    def __init__(self):
        self.db_path = Path("data") / "mtforge.db"
