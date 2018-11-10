class Phone(object):
    def __init__(self, phone_number):
        # invalid = set()
        self.holder = phone_number
        raw = self.cleaner(self.holder)
        if raw[0] == '1':
            self.number = raw[1:]
        else:
            self.number = raw
        
        self.area_code = self.number[0:3]
        self.exchange = self.number[3:6]
        self.rest = self.number[6:]

        if len(self.number) <= 9 or len(self.number) > 11:
            raise ValueError('Invalid num')
        if self.number[0] != '1' and len(self.number) >= 11:
            raise ValueError('Invalid num')
        if self.exchange[0] in ('1','0'):
            raise ValueError('invalid num')
        if self.area_code[0] in ('1','0'):
            raise ValueError('Invalid num') 

        print(raw[1:])
        print(self.area_code)
    
    def cleaner(self, anything):
        clean = ''.join(c for c in self.holder if c.isdigit())
        return clean

    def pretty(self,):
        outcome = '({}) {}-{}'.format(self.area_code, self.exchange,self.rest)
        return outcome