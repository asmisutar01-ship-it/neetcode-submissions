class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        len_of_arr = len(arr)
        for i in range(len_of_arr):
            print(arr[i])
            max_number = 0
            for j in range(i+1,len_of_arr):
                #to find the largest on right 
                max_number = max(arr[j], max_number)
            result.append(max_number)
        
        result[-1] = -1
        return result
            
        