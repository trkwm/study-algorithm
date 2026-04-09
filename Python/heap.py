
class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_queue = [None]*(capacity+1)
        self.queue_size = 0
    
    def HeapifyUp(self, child_index):
        if child_index>1:
            parent_index = child_index//2
            if self.heap_queue[child_index]<self.heap_queue[parent_index]:
                self.heap_queue[child_index],self.heap_queue[parent_index] = self.heap_queue[parent_index], self.heap_queue[child_index]
                self.HeapifyUp(parent_index)
    
    def HeapifyDown(self, parent_index):
        if 2*parent_index > self.queue_size:
            return
        elif 2*parent_index < self.queue_size:
            left = 2*parent_index
            right = 2*parent_index+1
            if self.heap_queue[left] < self.heap_queue[right]:
                child_index = left
            else:
                child_index = right
        else:
            child_index = 2*parent_index
        
        if self.heap_queue[child_index] < self.heap_queue[parent_index]:
            self.heap_queue[parent_index],self.heap_queue[child_index] = self.heap_queue[child_index],self.heap_queue[parent_index]
            self.HeapifyDown(child_index)

    def Insert(self, pushed_value):
        if self.queue_size == self.capacity:
            raise OverflowError("heap is full")
        
        self.queue_size += 1
        self.heap_queue[self.queue_size] = pushed_value
        self.HeapifyUp(self.queue_size)

    def FindMin(self):
        if self.queue_size==0:
            raise IndexError("heap is empty")
        return self.heap_queue[1]
    
    def Delete(self, del_index):
        if not (0<del_index<=self.queue_size):
            raise IndexError("invalid index")
        
        removed_value = self.heap_queue[del_index]

        if del_index==self.queue_size:
            self.heap_queue[self.queue_size] = None
            self.queue_size -= 1
            return removed_value
        
        self.heap_queue[del_index] = self.heap_queue[self.queue_size]
        self.heap_queue[self.queue_size] = None
        self.queue_size -= 1

        if del_index>1 and self.heap_queue[del_index] < self.heap_queue[del_index//2]:
            self.HeapifyUp(del_index)
        else:
            self.HeapifyDown(del_index)
        
        return removed_value
    
    def ExtractMin(self):
        if self.queue_size == 0:
            raise IndexError("heap is empty")
        return self.Delete(1)
    
    def Make_Heap(self, L):
        if len(L) > self.capacity:
            raise OverflowError("too many elements")
        self.heap_queue = [None]*(self.capacity+1)
        self.queue_size = len(L)
        for i in range(1, self.queue_size+1):
            self.heap_queue[i] = L[i-1]
        
        for i in range(self.queue_size//2, 0, -1):
            self.HeapifyDown(i)

    def __repr__(self):
        return str(self.heap_queue[1:self.queue_size + 1])
    