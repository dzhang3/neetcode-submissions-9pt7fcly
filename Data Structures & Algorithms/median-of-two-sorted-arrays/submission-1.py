import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        n,m = len(nums1), len(nums2)

        l, r = 0, n # binary search on num1
        half = math.ceil((n + m) / 2)
        while l < r:
            m1 = (l + r) // 2  # index of first element of upper of nums1 aka how many elements we choose
            m2 = half - m1 # index of first element of upper of nums2

            l1 = nums1[m1 - 1] if m1 > 0 else None
            u1 = nums1[m1] if m1 < n else None

            l2 = nums2[m2 - 1] if m2 > 0 else None
            u2 = nums2[m2] if m2 < m else None

            if (l1 is not None and  l2 is not None) and l1 > u2:
                r = m1 - 1
            elif (l2 is not None and u1 is not None) and l2 > u1:
                l = m1 + 1
            else:
                l = m1 
                break
        
        nl1 = nums1[l - 1] if l > 0 else float('-inf')
        nl2 = nums2[half - l - 1] if half - l > 0 else float('-inf')

        nu1 = nums1[l] if l < n else float('inf')
        nu2 = nums2[half - l] if half - l < m else float('inf')

        if (n + m) % 2 == 1:
            return max(nl1,nl2)
        else: 
            x = max(nl1,nl2)
            y = min(nu1,nu2)
            return (x + y) / 2


            
            

        
