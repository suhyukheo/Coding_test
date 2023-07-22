def solution(cacheSize, cities):
    cities = [x.lower() for x in cities]
    cache = {cities[0]:1}
    answer = 5
    for i in range(1,len(cities)):
        if cities[i] in cache and len(cache) == cacheSize:
            answer += 1
            for key in cache.keys():
                if key != cities[i]:
                    cache[key] +=1
                else:
                    cache[key] = 1
        elif cities[i] in cache and len(cache) < cacheSize:
            answer +=1
            for key in cache.keys():
                if key != cities[i]:
                    cache[key] +=1
                else:
                    cache[key] = 1
        elif cities[i] not in cache and len(cache) < cacheSize:
            answer +=5 
            cache[cities[i]] = 1
            for key in cache.keys():
                if key != cities[i]:
                    cache[key] +=1
                else:
                    cache[key] = 1
        else:
            try:
                x = max(cache, key=cache.get)
                del cache[x]
                for key in cache.keys():
                    if key != cities[i]:
                        cache[key] +=1
                cache[cities[i]] = 1
                answer +=5
            except:
                answer +=5
                continue
    return answer
