def minimize_height(arr, k):
    n = len(arr)

    # selection sort
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    ans = arr[n-1] - arr[0]

    for i in range(1, n):
        if arr[i] - k < 0:
            continue

        min_val = arr[0] + k
        max_val = arr[n-1] - k

        if arr[i] - k < min_val:
            min_val = arr[i] - k
        if arr[i-1] + k > max_val:
            max_val = arr[i-1] + k

        if max_val - min_val < ans:
            ans = max_val - min_val

    return ans

arr = [1,5,8,10]
k = 2
print(minimize_height(arr, k))