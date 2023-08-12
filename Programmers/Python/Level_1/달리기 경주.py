def solution(players, callings):
    dictionary ={p : i for i,p in enumerate(players)}
    for i in callings:
        n = dictionary[i]
        dictionary[i],dictionary[players[n-1]] = dictionary[players[n-1]],dictionary[i]
        players[n],players[n-1] = players[n-1],players[n]
        
    return players
