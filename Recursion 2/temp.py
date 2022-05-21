from itertools import combinations

def findsum(a):
    s = 0
    for i in a:
        s+=sum(i)
    return s

arr = [int(ele) for ele in input().split()]
ar3 = []
ar5 = []
ar=[]
for i in arr:
    if i%5==0 and i%3!=0:
        ar3.append(i)
    elif i%3==0 and i%5!=0:
        ar5.append(i)
    else:
        ar.append(i)
n = len(ar)
s1=s2=s=0
try:
    s1 = sum(ar3)
    s2 = sum(ar5)
    s = sum(ar)
except:
    pass
print(s1, s2, s)
print(ar3, ar5, ar)
for i in range(n):
    if s1+ar[i]==s2+sum(ar[0:i])+sum(a[i+1]):
        print(True)
        break
for i in range(2, n//2+1):
    t = findsum(list(combinations(ar, i)))
    if s1+t==s2:
        print('True')
        break
print('False')
    
# n = input()

# ans = split(arr,0,0)
# if ans is True:
#     print('true')
# else:
#     print('false')
