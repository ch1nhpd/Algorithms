'''

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''


def checkPossibility(nums) -> bool:
    flag = 0
    if len(nums) < 3:
        return True
    if nums[1] < nums[0]:
        nums[0] = nums[1]
        flag = 1
    for i in range(2, len(nums)):
        if nums[i - 1] > nums[i] and flag == 0:
            if nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
                flag = 1
            else:
                nums[i - 1] = nums[i - 2]
                flag = 1
        elif nums[i - 1] > nums[i] and flag == 1:
            return False
    return True
