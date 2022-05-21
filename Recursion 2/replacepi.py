def replace(s):
    if len(s)==0:
        return s
    # ans = replace(s[1:])
    if s[:2]=='pi':
        return '3.14'+replace(s[2:])
    else:
        return s[0]+replace(s[1:])

s = input()
print(replace(s))