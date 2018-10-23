class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    # if self.capacity == :
    #     return Exception("buffer is empty")
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._buffer = []
        
    def read(self):
        try:
            print('read',self._buffer) 
            r = self._buffer.pop(0)            
        except IndexError:
            raise BufferEmptyException('buffer is empty')        

        print('after',self._buffer, '_') 
        return r 

    def write(self, data):
        if len(self._buffer) == self.capacity:
            raise BufferFullException('buffer is full')

        self._buffer.append(data)

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException:
            self.read()
            self.write(data)
        # self._buffer.append(data)

    def clear(self):
        self._buffer = []
