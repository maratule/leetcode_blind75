from typing import  List
array2d = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 27

def bin_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return False

def finder(matrix, target):
    top, bot = 0, len(matrix) - 1
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False
    else:
        while top <= bot:
            midle_row = (top + bot) // 2
            if matrix[midle_row][-1] < target:
                top = midle_row + 1
            elif matrix[midle_row][0] > target:
                bot = midle_row - 1
            else:
               return bin_search(matrix[midle_row], target)
    return False

print(finder(array2d, target))
