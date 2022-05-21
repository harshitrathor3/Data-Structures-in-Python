## Read input as specified in the question.
## Print output as specified in the question.

def f(s):
    # print(s)
    if len(s)==0:
        return True
    if s[0]=='a':
        if len(s)==1:
            return True
        if s[1:2]=='a':
            return f(s[1:])
        if s[1:3]=='bb':
            return f(s[2:])
        return False
    if s[0]=='b':
        if len(s)==1:
            return True
        if s[1:2]=='a':
            return f(s[1:])
        return False
    return False




s = input()
if s[0]!='a':
    ans = False
else:
    ans = f(s)
print('true' if ans else 'false')
