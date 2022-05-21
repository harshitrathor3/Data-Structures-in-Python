def find(i, x):
    if i<0:
        return -1
    if arr[i]==x:
        return i+1
    else:
        return find(i-1, x)

def find1(arr, x):
    if len(arr)<1:
        return -1
    if arr[-1]==x:
        return 1
    else:
        ans = find1(arr[:-1], x)
        if ans==-1:
            return -1
        else:
            return ans+1

def find2(arr, x):
    if len(arr)==0:
        return -1
    ans = find2(arr[1:], x)
    if ans!=-1:
        return ans+1
    else:
        if arr[0]==x:
            return 1
        else:
            return -1
def find3(i, x):
    if i>=len(arr):
        return -1
    ans = find3(i+1, x)
    if ans!=-1:
        return ans
    else:
        if arr[i]==x:
            return i+1
        else:
            return -1

arr = list(map(int, input().split()))
x = int(input())
# print(find(len(arr)-1, x))
# ans = find1(arr, x)
# if ans==-1:
#     print(-1)
# else:
#     print(len(arr)-ans+1)
# print(len(arr)-find(arr, x)+1)

# print(find2(arr, x))
print(find3(0, x))