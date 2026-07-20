class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        m_freq = max(c.values())
        c_max = list(c.values()).count(m_freq)
        t = (m_freq-1)*(n+1)+c_max
        return max(len(tasks),t) 
        