def f(s, ans):
    if len(s)==0:
        return 0
    ans1 = ans+int(s[0])+(10*f(s[1:], ans))
    return ans1
    



s = input()

ans = 0
print(f(s[::-1], ans))
