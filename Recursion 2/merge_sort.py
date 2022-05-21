def merge1(ar1, ar2):
    i=0
    j=0
    ans=[]
    while i<len(ar1) and j<len(ar2):
        if ar1[i]<ar2[j]:
            ans.append(ar1[i])
            i+=1
        else:
            ans.append(ar2[j])
            j+=1
    ans+=ar1[i:]
    ans+=ar2[j:]
    return ans

def merge(ar1, ar2, ans):
    i=0
    j=0
    k=0
    while i<len(ar1) and j<len(ar2):
        if ar1[i]<ar2[j]:
            ans[k]=ar1[i]
            k+=1
            i+=1
        else:
            ans[k]=ar2[j]
            k+=1
            j+=1
    while i<len(ar1):
        ans[k]=ar1[i]
        i+=1
        k+=1
    while j<len(ar2):
        ans[k]=ar2[j]
        j+=1
        k+=1
    # ans+=ar1[i:]
    # ans+=ar2[j:]

def sort(arr):
    if len(arr)<2:
        return
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    sort(a1)
    sort(a2)
    merge(a1, a2, arr)
    # return arr

def sort1(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    # a1 = arr[:mid]
    # a2 = arr[mid:]
    a1 = sort1(arr[:mid])
    a2 = sort1(arr[mid:])
    return merge1(a1, a2)

arr = list(map(int, input().split()))
print(sort1(arr))
# print(arr)
# print(arr)
# ans=[]
# merge([1, 4, 6, 90, 99], [-1, 2, 21,  45 , 62, 89], ans)
# print(ans)
# a=[0, 0, 0]
# merge([1, 3], [2], a)
# print(a)
# print(merge1([1, 3, 4], [5, 7, 9]))