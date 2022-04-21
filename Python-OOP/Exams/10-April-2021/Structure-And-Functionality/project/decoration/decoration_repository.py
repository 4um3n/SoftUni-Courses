class DecorationRepository:
    def __init__(self) -> None:
        self.decorations = []

    def add(self, decoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str) -> str:
        for decoration in self.decorations:
            if type(decoration).__name__ == decoration_type:
                return decoration
        return f"None"
