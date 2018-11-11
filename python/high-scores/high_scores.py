class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def top(self):
        rank = sorted(self.scores, reverse = True)
        return rank[0:3]

    def large(self):
        rank = self.scores.sort()
        return rank
    
    def report(self):
        short = (" {} short of".format(self.highest() - self.latest()),"")[self.latest() == self.highest()]
        return "Your latest score was {}. That's{} your personal best!".format(self.latest(), short)
    
    def highest(self,):
        high = self.top()[0]
        return high
    
    def latest(self,):
        new = self.scores[-1]
        return new
