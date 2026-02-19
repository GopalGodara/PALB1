#You are given an array of integers arr[]. You have to reverse the given array.
#Note: Modify the array in place.

#There are few ways to reverse an array-:
#str = input()
#str1= str[-6].upper() + str[-5:-1].lower() + str[-1].upper()
#print(str1)

#str = input()
#str1= str[0].upper() + str[1:len(str)-1].lower()+ str[len(str)-1].upper()
#print(str1)

# str = "election"
# str1 = str[1:-1]
# print(str1)


# str = "python"
# print(str[::-1])
# print(str[-1:-7:-1])
# print(str[len(str):-7:-1]) #python interally changes it to len(str)-1
# print(str[len(str)-1:-7:-1])

# for x in range(len(str)-1, -1, -1):
#     print (str[x])

# str =input()
# rev = " "
# for i in str:
#     # rev = i + rev  ##reverses the string
#     rev = rev  + i    ## forward string
# print(rev)
# print(str[len(str):-1:-1])

# for x in range(len(str)-1,-1,-1):
#     print (str[x])

# .reverse isnt a function in python, coz doing so will mean that we are changing the actual string which is not possible as string is immutable
# reversed only stores the individual characters in reverse, doesnt print it which is why we use ".join" with reversed always to combine the individual chars
# str =input()
# b = reversed(str)
# c = " ".join(b)
# print(c)
