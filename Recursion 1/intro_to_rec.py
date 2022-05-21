def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def fact1(n):
    if n==0:
        return 1
    ans = fact(n-1)
    return n*ans

n = int(input())
print(fact(n))
print(fact1(n))