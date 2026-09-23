'''
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] 
such that they are at different indices, and their sum equals zero:nums[i] + nums[j] + nums[k] == 0
'''

nums = [-1, 0, 1, 2, -1, -4]

nums.sort() 

result = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
        
    left = i + 1
    right = len(nums) - 1
    
    while left < right:
        total_sum = nums[i] + nums[left] + nums[right]
        if total_sum < 0:
            left += 1
        elif total_sum > 0:
            right -= 1
        elif total_sum == 0:
            result.append([nums[i], nums[left], nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
                
            left += 1
            right -= 1

print(result)
