def kth_smallest(arr, k):
    n = len(arr)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr[k - 1]

arr = [10,5,4,3,48,6,2,33,53,10]
k = 4
print(kth_smallest(arr, k))