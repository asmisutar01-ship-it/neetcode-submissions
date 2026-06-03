class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maax = 0
        temp = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i]>heights[j] :
                    temp = heights[j]*(abs(i-j))
                else :
                    temp = heights[i]*(abs(j-i))
                
                if maax<temp :
                    maax = temp 
        return maax 


        