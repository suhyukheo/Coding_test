    word = words[0][-1]
    arr = []
    arr.append(words[0])
    for i in range(len(words)):
        r = (i//n)+1
        o = (i%n)+1
        if i>0 : 
            if word == words[i][0] and words[i] not in arr:
                word = words[i][-1]
                arr.append(words[i])
            else:
                return [o,r]
    return [0,0]
