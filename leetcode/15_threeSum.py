from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length_nums = len(nums)
        rs = []

        for i in range(0, length_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p, q = i + 1, length_nums - 1

            while p < q:
                three_sum = nums[i] + nums[p] + nums[q]
                if three_sum == 0:
                    rs.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while p < q:
                        if nums[p] == nums[p - 1]:
                            p += 1
                        elif nums[q] == nums[q + 1]:
                            q -= 1
                        else:
                            break
                elif three_sum < 0:
                    p += 1
                else:
                    q -= 1
        return rs