class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0 
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                s = numbers[i]+numbers[j]
                if s == target :
                    return [i+1,j+1]
        


        