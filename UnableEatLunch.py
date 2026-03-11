class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = len(students)
        while counter > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = len(students)
            else:
                students.append(students.pop(0))
                counter -= 1
        return len(students)
