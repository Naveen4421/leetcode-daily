import heapq
def __init__(self):
        self.minHeap = []
        self.present = set()
        self.nextVal = 1
        

def popSmallest(self):
       """
       :rtype: int
       """
       if self.minHeap:
           smallest = heapq.heappop(self.minHeap)
           self.present.remove(smallest)
           return smallest

       # Otherwise return nextVal
       smallest = self.nextVal
       self.nextVal += 1
       return smallest
        

def addBack(self, num):
      """
      :type num: int
      :rtype: None
      """
      if num < self.nextVal and num not in self.present:
          heapq.heappush(self.minHeap, num)
          self.present.add(num)
