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
        self.position = 0
        
    def read(self):
        try:
            print('wrote',self._buffer) 
            r = self._buffer.pop(self.position)
            
        except IndexError:
            raise BufferEmptyException('buffer is empty')        

        print('after',self._buffer, '_') 
        return r 

    def write(self, data):
        if len(self._buffer) == self.capacity:
            raise BufferFullException('buffer is full')

        self._buffer.append(data)

    def overwrite(self, data):
        self._buffer[1:-1] = data

    def clear(self):
        pass
