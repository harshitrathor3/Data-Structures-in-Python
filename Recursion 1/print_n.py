def f(n):
    if n==1:
        return 1
    print(f(n-1), end=' ')
    return n

def f1(n):
    if n==1:
        print(1, end=' ')
        return
    f1(n-1)
    print(n, end = ' ')



def n_to_1(n):
    if n==0:
        return 1
    print(n, end=' ')
    return n_to_1(n-1)


n = int(input())
print(f(n))
print()
f1(n)
print('\n')
n_to_1(n)
print()
# f(n)