# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

#1) without using min, max functions-:
# n = int(input("Enter number of elements: "))
# arr = []
# for i in range(n):
#     num = int(input(f"Enter element {i+1}: "))
#     arr.append(num)
# minimum = arr[0]
# maximum = arr[0]
# for i in arr:
#     if i < minimum:
#         minimum = num
#     if i > maximum:
#         maximum = num
# print("Minimum:", minimum)
# print("Maximum:", maximum)

#2) using min, max functions-:
# n = int(input("Enter number of elements: "))
# arr = []
# for i in range(n):
#     num = int(input(f"Enter element {i+1}: "))
#     arr.append(num)
# minimum = arr[0]
# maximum = arr[0]
# minimum = min(arr)
# maximum = max(arr)
# print("Minimum:", minimum)
# print("Maximum:", maximum)


