def replace(s):
    if len(s)==0:
        return s
    # ans = replace(s[1:])
    if s[0]=='a':
        return 'b'+replace(s[1:])
    else:
        return s[0]+replace(s[1:])

s = input()
print(replace(s))