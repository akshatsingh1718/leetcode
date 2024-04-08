from typing import List


class Solution:
    '''
    TC: O(n) [for sum] + O(n)[for sandwitches iteration]
    SC: O(1) [for no_of_zeros] + O(1) [for no_of_ones]

    Algo:
    1. Count the no of zeros and ones in student stack.
    2. Iterate over students and check for the top sandwitch type availability in studnets data which is no_of_ones and no_of_zeros. If the no of students wants to eat certain type of sandwitch eg.- {1, 0} comes out to be zero then it means the rest of the sandwitches will remain un-eaten hence the same of students will also remain hungry as well.    
    '''
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # Count no of ones and zeros in student stack
        no_of_ones = sum(students)
        no_of_zeros = len(students) - no_of_ones

        for i, ele in enumerate(sandwiches):
            if ele == 0 and no_of_zeros > 0:
                no_of_zeros -=1
            elif ele == 0 and no_of_zeros == 0:
                return len(sandwiches) - i
            elif ele == 1 and no_of_ones > 0:
                no_of_ones -= 1
            elif ele == 1 and no_of_ones == 0:
                return len(sandwiches) - i

        return 0
    

students =[1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0]
sandwiches = [0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,0]
expected = 2
print(Solution().countStudents(students, sandwiches))

