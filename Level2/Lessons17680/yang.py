# 캐시
def solution(cacheSize, cities):
    from collections import deque
    tmp_que = deque()
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in tmp_que:
            answer += 1
            tmp_que.remove(city)
            tmp_que.append(city)
        else:
            answer += 5
            if cacheSize <= len(tmp_que):
                tmp_que.popleft()
            tmp_que.append(city)

        
        
    return answer
