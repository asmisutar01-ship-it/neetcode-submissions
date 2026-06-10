class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        c = 0 
        while students and sandwiches :
            if students[0]==sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                c = 0
            else :
                students.append(students.popleft())
                c += 1
            if c == len(students):
                break 
        return len(students)



        