class DLLNode:
    def __init__(self,key = 0, val = 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

    def addNode(self,node): #add node after self
        successor = self.next
        self.next = successor.prev = node
        node.next = successor
        node.prev = self
    
    def removeNode(self): #remove current node from list
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {} # from key to Node
        self.head = DLLNode() # LRU Cache
        self.tail = DLLNode()
        self.head.next ,self.tail.prev = self.tail,self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        #find the node in mapping
        node = self.mapping[key]
        #move the node to beginning
        node.removeNode()
        self.head.addNode(node)
        #return value
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # if node doesn't exist then create it, else retrieve the node
        node = None
        if key not in self.mapping:
            node = DLLNode(key,value)
            self.size += 1

            if self.size > self.capacity: # remove last node and mapping entry if over capacity
                keyToRemove = self.tail.prev.key
                self.tail.prev.removeNode()
                self.size -= 1
                self.mapping.pop(keyToRemove)

        else:
            node = self.mapping[key]
            node.val = value
            node.removeNode()
        
        self.head.addNode(node)
        self.mapping[key] = node
        








