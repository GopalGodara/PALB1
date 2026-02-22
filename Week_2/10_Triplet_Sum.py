def triplet_sum(arr, target):
    n = len(arr)

    # manual sort
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for i in range(n-2):
        l = i + 1
        r = n - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == target:
                return True
            elif s < target:
                l += 1
            else:
                r -= 1
    return False

arr = [1,4,45,6,10,8]
target = 13
print(triplet_sum(arr, target))