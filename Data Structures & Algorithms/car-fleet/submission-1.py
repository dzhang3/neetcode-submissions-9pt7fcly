class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        stack = []
        for p,s in cars:
            if not (stack):
                stack.append((p,s))
            else:
                tp,ts = stack[-1]
                if (ts >= s and tp > p) or (tp - p) / (s - ts) > (target - tp) / ts: # if car doesn't reach ahead car before finishing
                    stack.append((p,s))
        return len(stack)
        