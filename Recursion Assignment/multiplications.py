## Read input as specified in the question.
## Print output as specified in the question.
try:

    def mul(n1, n2):
        if n1<=0:
            return 0

        return n2+mul(n1-1, n2)
except:
    pass

from sys import setrecursionlimit
setrecursionlimit(11000)
n1 = int(input())
n2 = int(input())
print(mul(n1, n2))
