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
    def _sift_up(self,i):
        while i>0:
            parent = (i-1)//2
            if self.compare(self.heap[i],self.heap[parent]):
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
                i=parent
            else:
                break
    def pop(self):
        if len(self.heap) == 0:
            return None
        peek = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        del self.heap[-1]
        self._sift_down(0)
        return peek
    def _sift_down(self,i):
        while i<len(self.heap)//2:
            child1=2 * i + 1
            child2=2 * i + 2
            best = child1
            if child2 < len(self.heap) and self.compare(self.heap[child1],self.heap[child2]):
                best =child1
            elif child2 < len(self.heap) and self.compare(self.heap[best],self.heap[child2]):
                best = child2
            if self.compare(self.heap[best],self.heap[i]):
                self.heap[i],self.heap[best]=self.heap[best],self.heap[i]
                i=best
            i = best
    def push(self,value):
        self.heap.append(value)
        self._sift_up(len(self.heap)-1)
    def compare(self,a,b):
        if self.heap_name=='Max':
            if a > b:
                return True
            return False
        if self.heap_name=='Min':
            if a < b:
                return True
            return False
    def __str__(self):
        return str(self.heap)
if __name__ == "__main__":
    heap = BinaryHeap("Max")
    for x in  [10,2,55,3245,5]:
        heap.push(x)
        pass
    print(heap)
    heap.pop()
    print(heap)