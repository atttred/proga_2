class GeneratorId:
    def __init__(self):
        self.limit = 100
        
    def __iter__(self):
        return self
    def __next__(self):
        for i in range(self.limit):
            yield i