class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException('no')
        return self.buffer.pop(0)
        

    def write(self, data):
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("no")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.read()
        self.write(data)

    def clear(self):
        self.buffer = []
