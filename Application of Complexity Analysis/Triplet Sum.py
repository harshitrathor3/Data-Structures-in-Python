from sys import stdin
from math import factorial

def comb(n):
    return factorial(n)//(2*factorial(n-2))


def tripletSum(arr, n, num):
    arr.sort()
    count = 0
    for r in range(n-2):
        i = r+1
        j = n-1
        
        
        while i<j:
            # print("i, j = ",i, j)
            s = arr[r] + arr[i] + arr[j]
            if s<num:
                i+=1
            elif s>num:
                j-=1
            else:
                t1 = 1
                t2 = 1

                if arr[i]==arr[j]:
                    count+=comb(j-i+1)
                    break

                while arr[i]==arr[i+1] and i+1<j:
                    # print(i)
                    i+=1
                    t1+=1
                while arr[j]==arr[j-1] and j-1>i:
                    j-=1
                    t2+=1
                # print(t1, t2)

                count = count + (t1*t2)
                i+=1
                j-=1
    return count

#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1