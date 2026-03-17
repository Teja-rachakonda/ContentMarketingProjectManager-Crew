class ChatMemory:
    def __init__(self):
        self.history = []

    def add_user(self, content):
        self.history.append({"role": "user", "content": content})

    def add_assistant(self, content):
        self.history.append({"role": "assistant", "content": content})

    def get_history(self):
        return self.history