from threading import Lock
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.start = 0
        self.end = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == len(self.queue):
            return False
        self.size += 1
        self.queue[self.end] = value
        self.end = (self.end + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.size -= 1
        self.start = (self.start + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.queue[self.end-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()