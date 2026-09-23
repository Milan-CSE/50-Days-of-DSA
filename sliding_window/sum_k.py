arr = [2, 5, 1, 3, 2]
k = 3

current_sum = sum(arr[:k])
max_sum = current_sum


for right in range(3, len(arr)):
    leaving_passenger = arr[right - 3]
    entering_passenger = arr[right]
    current_sum = current_sum - leaving_passenger + entering_passenger
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)