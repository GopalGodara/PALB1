def trap_water(arr):
    n = len(arr)
    water = 0

    for i in range(1, n-1):
        left_max = arr[i]
        for j in range(i):
            if arr[j] > left_max:
                left_max = arr[j]

        right_max = arr[i]
        for j in range(i+1, n):
            if arr[j] > right_max:
                right_max = arr[j]

        water += min(left_max, right_max) - arr[i]

    return water

arr = [3,0,1,0,4]
print(trap_water(arr))