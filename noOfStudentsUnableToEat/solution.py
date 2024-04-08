from typing import List


class Solution:
    '''
    TC: O(n) [for popping worst position element] * O(n) [while all the stundets popped]
    SC: O(1) [for counter]

    Algo:
    1. Loop will run until stundets has been emptied.
    2. counter variable to check how many students didnt get their fav food ={1, 0} and if the counter reaches the length of the current students it means all the stundets wanted food which is not on the top of the sandwitch stack. Hence everyone left will stay hungry.
    3. If the student at top find its food then counter will reset and both the stundent and sandwitch will be popped for the 0th index element which is the top.
    
    '''
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0

        while len(students) > 0:
            if counter == len(students):
                return len(students) # cannot feed any more student

            if students[0] == sandwiches[0]:
                counter = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                counter += 1
                first_elem = students.pop(0)
                students.append(first_elem)

        return 0