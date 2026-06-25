import json


class ResearchEngine:
    def __init__(self):
        with open("database/symbols.json", "r", encoding="utf-8") as f:
            self.symbols = json.load(f)

    def investigate(self, term):
        key = term.lower()

        if key not in self.symbols:
            return {
                "themes": [],
                "traditions": [],
                "related": []
            }

        return self.symbols[key]
