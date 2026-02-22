def is_subset(a, b):
    for i in range(len(b)):
        found = False
        for j in range(len(a)):
            if b[i] == a[j]:
                found = True
                break
        if not found:
            return False
    return True

a = [11,7,1,13,21,3,7,3]
b = [11,3,7,1,7]
print(is_subset(a,b))