'''
The Problem Description:You are given an array of integers nums consisting of n elements, 
and an integer k. Find a contiguous subarray whose length is equal to k that has the maximum 
average value, and return this maximum average.
'''

nums = [1, 12, -5, -6, 50, 3]

k = 4

current_sum = sum(nums[:k])

max_sum = current_sum

left = 0

for right in range(k, len(nums)):
    current_sum = current_sum - nums[left] + nums[right]
    left += 1
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum/k)