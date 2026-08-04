class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        stack = []
        for p,s in cars:
            while stack:
                pv,sv = stack[-1]
                if sv <= s:
                    break
                t = (p - pv) / (sv - s)
                # print(t)
                if t * s + p > target:
                    break
                stack.pop()
            stack.append((p,s))
        return len(stack)
                
                    
            