class LLNode:
    def __init__(self, key, val, nex, pre):
        self.nex = nex
        self.pre = pre
        self.val = val
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LLNode(-1, -1,None,None)
        self.tail = LLNode(-1, -1,None,self.head)
        self.mapping = {}
        self.head.nex = self.tail

    def remove(self, node):
        prev, nxt = node.pre, node.nex
        prev.nex, nxt.pre = nxt, prev
    
    def insert(self, node):
        prev, nex = self.head, self.head.nex
        prev.nex = nex.pre = node
        node.pre, node.nex = prev, nex


    def get(self, key: int) -> int:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            return self.mapping[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            self.mapping[key].val = value
        else:
            cur = LLNode(key,value,self.head,self.head.nex)
            self.insert(cur)
            self.mapping[key] = cur

            if len(self.mapping) > self.capacity:
                self.mapping.pop(self.tail.pre.key)
                self.remove(self.tail.pre)
                

        
        
