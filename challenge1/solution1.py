def answer(s):
    solutes = 0
    for i in range(0,len(s)):
        if s[i] == ">":
            for char in s[i:]:
                if char == "<":
                    solutes += 2
    return solutes
