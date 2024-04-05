TestCases = [[1, 2, 3]]

Expected = [[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]]


def checkSol(arr1, arr2):
    if len(arr1) != len(arr2):

        return False
    for ar in arr1:
        if ar not in arr2:
            return False
    return True
