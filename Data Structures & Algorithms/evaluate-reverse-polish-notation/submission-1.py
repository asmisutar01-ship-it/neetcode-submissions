class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "+-*/" :
                s.append(int(i))
            else :
                b = s.pop()
                a = s.pop()
                s.append(
                    a+b if i=="+" else
                    a-b if i=="-" else
                    a*b if i=="*" else
                    int(a/b)
                )
        return s[0] 
        