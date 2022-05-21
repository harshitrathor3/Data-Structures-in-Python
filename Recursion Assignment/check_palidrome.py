## Read input as specified in the question.
## Print output as specified in the question.

def palin(s):
    if len(s)<=1:
        return True
    
    ans = s[0]==s[-1]
    return ans and palin(s[1:-1])



s = input()
print('true' if palin(s) else 'false')