class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = sorted(set(nums))
        c = 1
        l = 1
        for i in range(len(nums)-1) :
            if nums[i+1]-nums[i] == 1 :
                c=c+1
                l = max(l,c) 
            else :
                c = 1
        return l 

        