class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []

        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i != j:
                    p *= nums[j]
            l.append(p)       
        return l 
            

        