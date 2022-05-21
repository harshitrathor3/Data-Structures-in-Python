## Read input as specified in the question.
## Print output as specified in the question.

def calcsum(s):
    if len(s)==0:
        return 0
    return int(s[0])+int(calcsum(s[1:]))

from sys import setrecursionlimit
setrecursionlimit(11000)
n = input()
print(calcsum(n))