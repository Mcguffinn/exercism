class Phone(object):
    def __init__(self, phone_number):
        self.number = self.cleaner(phone_number)
        self.area_code = self.number[0:3]
        self.exchange = self.number[3:6]
        self.rest = self.number[6:]
        
        if self.number[0] in '0' or self.number[3] in '10':
            raise ValueError('Invalid1')
        if self.area_code[0] in '01':
            raise ValueError('wrong')
        if len(self.number) <= 9 or len(self.number) > 11 or len(self.number) == 11 and self.number[0] in '2':
            raise ValueError('nope')
        print(self.number, self.number[0])
        # print(self.area_code)

    def cleaner(self, phone_number):
        clean = ''.join(c for c in phone_number if c.isdigit())
        if clean[0] == '1':
            return clean[1:]
        else:
            return clean

    def pretty(self,):
        outcome = '({}) {}-{}'.format(self.area_code, self.exchange,self.rest)
        return outcome