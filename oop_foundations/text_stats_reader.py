"""Read a text file and summarize line, word, and character counts."""

class TextStats:
    def __init__(self, path):
        self.path = path
        self.line = None
        self.word = None
        self.char = None

    def load_file(self):
        with open(self.path, "r", encoding='utf-8') as file:
            lines = file.readlines()

            # Store counts on the object so `summary()` can reuse them later.
            self.line = sum(1 for _ in lines)
            self.word = sum(len(line.split()) for line in lines)
            self.char = sum(len(line) for line in lines)
    
    def summary(self):
        if self.line is None:
            self.load_file()
        return {
            "lines": self.line,
            "word" : self.word,
            "char" : self.char
        }
    
    
# Example run against the sample text file in the repo root.
f = TextStats("example.txt")
print(f.summary())

    
