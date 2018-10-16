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

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        crt_score = 0
        allergies = []

        for allergen, value in self.allergens:
            new_score = crt_score + value

            if new_score == self.score:
                allergies.append(allergen)
                break
            if new_score < self.score:
                crt_score = new_score
                allergies.append(allergen)
        
        return allergies