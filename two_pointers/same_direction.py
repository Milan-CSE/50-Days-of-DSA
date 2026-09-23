arr = [2,2,0,6,6]

j = 0

for i in range(1, len(arr)):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

arr_new = arr[:j+1]

print(arr_new)
