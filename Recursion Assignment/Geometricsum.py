## Read input as specified in the question.
## Print output as specified in the question.
def f(n):
    if n==0:
        return 1
    return 1/(2**n)+f(n-1)


n = int(input())
print('%.5f'%f(n))