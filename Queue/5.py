#Leetcode 1700. Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud=deque(students)
        sand=deque(sandwiches)
        c=0
        while stud and c<len(stud):
            if stud[0]==sand[0]:
                stud.popleft()
                sand.popleft()
                c=0
            else:
                stud.append(stud.popleft())
                c+=1
        return len(stud)