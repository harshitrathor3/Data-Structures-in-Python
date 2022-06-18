
def maximumProfit(arr):
    m = 0
    arr.sort()
    for i in range(len(arr)):
        t = arr[i]*(len(arr)-i)
        # print(arr[i], len(arr)-i)
        if t>m:
            m = t
    return m    
        

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)