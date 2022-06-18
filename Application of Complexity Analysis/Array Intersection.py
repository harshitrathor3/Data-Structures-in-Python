arr = [1, 2, 3, 4, 5 ,6, 7]
arr1 = [78, 10]

i = j = 0
ans = []
while i<len(arr) and j<len(arr1):
    if arr[i]<arr1[j]:
        i+=1
    elif arr1[j]<arr[i]:
        j+=1
    else:
        ans.append(arr[i])
        i+=1
        j+=1
print(ans)
