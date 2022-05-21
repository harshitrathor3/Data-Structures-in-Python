def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)



def fib_sum(n, s=0):
    if n<=1:
        return 1
    s+=fib_sum(n-1, s)+fib_sum(n-2, s)
    return s

def fib1(n):
    if n<=2:
        print(1, end=' ')
        return 1
    ans = fib1(n-1)+fib1(n-2)
    print(ans, end=' ')
    return ans

global f1, f2
f1=f2=1

def fib_ser(cnt):
    if cnt>0:
        global f2, f1
        t = f2
        f2 = f1+f2
        f1=t
        print(f2, end=' ')
        fib_ser(cnt-1)

n = int(input())
# print(fib(n))
# print(fib_sum(n))
# fib1(n)
print(1, 1, end=' ')
fib_ser(n-1)
print()