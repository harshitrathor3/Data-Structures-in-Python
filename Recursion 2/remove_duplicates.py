def remove(s):
    if len(s)<2:
        return s
    if s[0]==s[1]:
        return remove(s[1:])
    else:
        return s[0]+remove(s[1:])

s = input()
print(remove(s))