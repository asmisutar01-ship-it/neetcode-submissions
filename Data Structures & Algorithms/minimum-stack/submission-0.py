class MinStack:

    def __init__(self):
        self.con = deque()
        self.mini = deque()
        

    def push(self, val: int) -> None:
        self.con.append(val)
        if not self.mini or val <= self.mini[-1] :
            self.mini.append(val)
        

    def pop(self) -> None:
        if self.con[-1]==self.mini[-1] :
            self.mini.pop()
        self.con.pop()
        

    def top(self) -> int:
        return self.con[-1]

    def getMin(self) -> int:
        return self.mini[-1]


        
        
