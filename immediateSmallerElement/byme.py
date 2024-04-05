from typing import List


def immediateSmaller(a: List[int]) -> None:
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            # replace with -1
            a[i] = -1

        else:
            a[i] = a[i + 1]
    
    a[-1] = -1



def main():
    input = [4, 7, 8, 2, 3, 1]
    target = [-1, -1, 2, -1, 1, -1]

    immediateSmaller(input)

    if target == input:
        print("Test case passed")
    else:
        print("Test case failed")



main()
