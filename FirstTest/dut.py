class DUT:
    def __init__(self):
        self.values = None

    def __int__(self):
        self.values = {}

    def set(self, key: str, value) -> bool:
        self.values[key] = value
        return True

    def get(self, key: str) -> str:
        return self.values.get(key, None)

    def reset(self):
        self.values = {}
