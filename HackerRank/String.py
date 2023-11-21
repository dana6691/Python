def superReducedString(s):
    ls = list(s)
    while i < len(ls):
        if ls[i] == ls[i+1]:
            del ls[i]
    print(ls)

superReducedString("aaabccddd")