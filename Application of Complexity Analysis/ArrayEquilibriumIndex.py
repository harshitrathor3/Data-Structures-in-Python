from sys import stdin

def arrayEquilibriumIndex(arr, n):
    try:

        i = 0
        l = 0
        r = sum(arr[1:])
        while i<n:
            if l-r==0:
                return i
            i+=1
            l+=arr[i-1]
            r-=arr[i]
        return -1
    except:
        return -1





#Taking input using fast I/O method
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
    print(arrayEquilibriumIndex(arr, n))

    t-= 1