import re 
class Phone(object):
    def __init__(self, phone_number):        
        self.number = self.clean(phone_number)        
        self.area_code = self.clean(phone_number)[0:3]
        
        if len(self.number) <= 9 or len(self.number) > 11 :
            raise ValueError('Wrong')
        if self.number[3] in "01":
            raise ValueError('Wrong')
        if self.area_code[0] in '01':
            raise ValueError('Wrong')
        
    def pretty(self):
        cleaned = "({}) {}-{}".format(self.number[0:3],self.number[3:6],self.number[6:])
        return cleaned

    def clean(self, phone_number):
        sort = ''.join([d for d in phone_number if d.isdigit()])
        if len(sort) == 11 and sort[0] == '1':
            sort = sort[1:]
        elif len(sort) == 10:
            pass
        else:
            raise ValueError('Wrong')
        
        return sort