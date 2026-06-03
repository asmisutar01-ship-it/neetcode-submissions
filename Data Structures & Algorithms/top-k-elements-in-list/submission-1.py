class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if nums[i] == nums[j] :
                    c+=1
            l.append((nums[i],c))

        l = sorted(l, key=lambda x: x[1], reverse=True)
        
        r = []
        seen = set()

        for n, c in l:
            if n not in seen:
                r.append(n)
                seen.add(n)
            if len(r) == k:
                break


        return r 


        