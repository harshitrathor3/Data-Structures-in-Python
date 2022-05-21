def removex(s):
    if len(s)==0:
        return s
    # ans = removex(s[1:])
    if s[0]=='x':
        return removex(s[1:])
    else:
        return s[0]+removex(s[1:])


s = input()
print(removex(s))