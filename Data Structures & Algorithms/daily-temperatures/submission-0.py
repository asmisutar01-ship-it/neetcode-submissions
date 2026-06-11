class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        for i in range(len(temperatures)):
            f = False
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j] :
                    s.append(j-i)
                    f = True
                    break
            if not f:
                s.append(0)
        return s 

        