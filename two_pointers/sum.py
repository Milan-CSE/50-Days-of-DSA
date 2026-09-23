arr = [2,6,8,11]

left = 0
right = len(arr) - 1

while right > left:

    sum = arr[left] + arr[right]

    if sum > 14:
        right -= 1
    elif sum < 14:
        left += 1
    elif sum == 14:
        print(f"{arr[left]} + {arr[right]} = 14")
        break

else:
        print("No combination foud to get 14 as a sum")
