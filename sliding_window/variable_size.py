arr = [2, 15, 5, 6, 8]

left = 0

running_sum = 0
min_length = 100

for right in range(len(arr)):
    running_sum += arr[right]

    while running_sum >= 14:
        currnt_window = right - left + 1
        min_length = min(min_length,currnt_window)
        running_sum -= arr[left]
        left += 1
        
print(min_length)