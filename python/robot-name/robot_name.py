import string
import re
import random

class Robot(object):

    def __init__(self):        
        self.seen = set()
        self.reset()

    def choose(self, lst, n):
        return "".join([random.choice(lst) for i in range(n)])

    def mk_name(self):
        l, d = self.choose(string.ascii_uppercase, 2), self.choose(string.digits, 3)
        return f'{l}{d}'

    def reset(self):
        name = self.mk_name()
        if name in self.seen:
            self.reset() 
        else:
            self.seen.add(name)
            self.name = name
