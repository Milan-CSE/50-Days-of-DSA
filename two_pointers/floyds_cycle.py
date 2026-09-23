arr = [1,3,2,3,4]

slow = 0
fast = 0

while True:
    slow = arr[slow]
    fast = arr[arr[fast]]

    if slow == fast:
        print("..")
        break