'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of actual elements in nums1 and 
nums2 respectively.Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

m = 3
n = 3

p1 = m - 1
p2 = n - 1

w = m + n - 1

while p2 >= 0:
    if p1 >= 0 and nums1[p1] > nums2[p2]:
        nums1[w] = nums1[p1]
        p1 -= 1
    else:
        nums1[w] = nums2[p2]
        p2 -= 1

    w -= 1
print(nums1)