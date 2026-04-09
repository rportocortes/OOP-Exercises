class StopWatch:
    def __init__(self, seconds = 0):
        self.seconds = seconds

    def advance(self, s):
        self.seconds += s
        return self.seconds
    
    def in_minutes(self):
        division = self.seconds // 60
        modulo = self.seconds % 60
        return f"{division} minutes and {modulo} seconds"
    
sw = StopWatch(90)
sw.advance(65)
print(sw.in_minutes())