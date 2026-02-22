# arr1=[1, 5, 10, 20, 40, 80]
# arr2=[6, 7, 20, 80, 100]
# arr3=[3, 4, 15, 20,30, 70, 80, 120]
# arr4=[]
# for i in arr1:
#     if i in arr2 and i in arr3:
#         arr4.append(i)
# print("Common elements of 3 arrays are:",arr4)

# arr1=[1, 5, 10, 20, 40, 80]
# arr2=[6, 7, 20, 80, 100]
# arr3=[3, 4, 15, 20,30, 70, 80, 120]
# common=set(arr1).intersection(arr2).intersection(arr3)
# print("Common elements of 3 arrays are:",list(common)) #coz of property of set being unordered, 80 came first

# arr1=[1, 5, 10, 20, 40, 80]
# arr2=[6, 7, 20, 80, 100]
# arr3=[3, 4, 15, 20,30, 70, 80, 120]
# common=set(arr1) & set(arr2) & set(arr3)
# print(list(common))