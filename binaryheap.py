class BinaryHeap:
    def __init__(self,heap_name):
        self.heap = []
        self.heap_name = heap_name
    def heap_size(self):
        return len(self.heap)
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    def compare(self,a,b):
        if self.heap_name=='Max':
            if a > b:
                return True
            return False
        if self.heap_name=='Min':
            if a < b:
                return True
            return False
