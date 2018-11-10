class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def top(self):
        pass
        rank = self.scores.sort(reverse = True)
        return self.scores[0:3]
    
    def report(self,):
        a = self.highest(self.scores)
        b = self.latest(self.scores)
        w = [a - b for (a, b) in zip(a, b)]
        print(a,b)
        # if new > item1:
        #     rep = "Your latest score was {}. That's your personal best!".format(self.highest())
        #     print(rep)
        # else:
        #     rep = "Your latest score was {}. \
        #     That's {} short of your personal best!".format(self.latest(),self.highest())
        # return rep
    
    def highest(self,scores):
        high = self.top()[0]
        return high
    
    def latest(self,scores):
        new = self.scores[-1]
        return new