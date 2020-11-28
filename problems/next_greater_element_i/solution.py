class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hm = {}
        res = []
        for i in nums2:
            while stack and i > stack[-1]:
                hm[stack.pop()] = i
            stack.append(i)
        while stack:
            hm[stack.pop()] = -1
        for i in nums1: 
            res.append(hm[i])
            #res[i].append(hm[i])
        return res
    