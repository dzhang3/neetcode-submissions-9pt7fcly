class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars = sorted(cars)
        
        stack = []
        for pos,speed in cars:
            # test if current car limits all prev
            while len(stack) > 0 and (target - pos) / speed >= (target - stack[-1][0]) / stack[-1][1]:
                stack.pop()
            stack.append((pos,speed))
        return len(stack)
            
            
        

        
        