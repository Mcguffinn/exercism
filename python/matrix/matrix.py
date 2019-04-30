class Matrix(object):
    def __init__(self, matrix_string):
        self.store = []

        for row, rowdata in enumerate(matrix_string.split('\n')):
            self.store.append([])
            for  columnn, columndata in enumerate(rowdata.split(' ')):
                self.store[row].append(int(columndata))
            

    def row(self, index):
        return self.store[index]


    def column(self, index):
        ok = []
        for row, data in enumerate(self.store):
            ok.append(data[index])
        print(ok)
        return ok
