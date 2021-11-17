'''
Given an integer array nums and two integers k and t,
return true if there are two distinct indices i and j in the array
such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

TEST CASE

nums = [1,2,3,1]
k = 3
k = 0
nums = [1,5,9,1,5,9]
k = 2
t = 3

'''
from bisect import *
from typing import List

from sortedcontainers import SortedList


def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
    tmp = SortedList()
    for i in range(0,len(nums)):
        if i > k:
            tmp.remove(nums[i-k-1])
        pos1 = bisect_left(tmp,nums[i]-t)
        pos2 = bisect_right(tmp,nums[i]+t)

        if pos1!= pos2:
            return True
        tmp.add(nums[i])
    return False
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(containsNearbyAlmostDuplicate(nums,k,t))

# s = SortedList([5,9,8,4,75,6,10])
# print(s)
# print(bisect_left(s,70))
# print(bisect_right(s,70))