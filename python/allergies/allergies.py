class Allergies(object):

    def __init__(self, score):

        self.allergens = [
            ('cats', 128),
            ('pollen', 64),
            ('chocolate', 32),
            ('tomatoes', 16),
            ('strawberries', 8),
            ('shellfish', 4),
            ('peanuts', 2),
            ('eggs', 1),
        ]

        self.score = score if score <= 255 else score - 256
        self.lst = self.make_allergy_list()      

    def is_allergic_to(self, item):
        return item in self.lst
    
    def make_allergy_list(self):
        computed_score = 0
        allergies = []

        for allergen, value in self.allergens:
            tv = computed_score + value

            if tv == self.score:
                allergies.append(allergen)
                break

            if tv < self.score:
                computed_score = tv
                allergies.append(allergen)    

        return allergies    


 