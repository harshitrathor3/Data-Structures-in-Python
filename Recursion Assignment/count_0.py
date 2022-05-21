## Read input as specified in the question.
## Print output as specified in the question.


def f(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+f(n//10)
    else:
        return f(n//10)

n = int(input())
if n==0:
    print(1)
else:
    print(f(n))
