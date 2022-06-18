from sys import stdin


def reverse(arr, i, n):
    while i<n:
        arr[i], arr[n] = arr[n], arr[i]
        i+=1
        n-=1


def rotate(arr, n, d):
    reverse(arr, 0, n-1)
    reverse(arr, 0, n-d-1)
    reverse(arr, n-d, n-1)




#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
