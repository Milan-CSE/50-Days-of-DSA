arr = [1,1,2,2,2,3,3,4]

arr_index = 1

for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        arr[arr_index] = arr[i]
        arr_index += 1

del arr[arr_index:]

print(arr)