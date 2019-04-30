class School(object):
    def __init__(self):
        self.student = {}

    def add_student(self, name, grade):
        self.student.update({name:grade})

    def roster(self):
        names = []
        # sort = sorted(self.student.items(),key = lambda kv:[1])
        sort = [v[0] for v in sorted(self.student.items(), key = lambda kv: (kv[1], kv[0]))]
        print(sort)
        for name in sort:
            names.append(name)
        print(names)
        return names
        

    def grade(self, grade):
        name = []
        for n,g in self.student.items():
            print(n,g)
            if g == grade:
                name.append(n)
        
        return sorted(name)