#[1차] 캐시
#LRU : 가장 오랫동안 참조되지 않은 페이지를 교체    
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer+=5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer+=1
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (66.38ms, 17.6MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10.2MB)
테스트 14 〉	통과 (0.12ms, 10.2MB)
테스트 15 〉	통과 (0.22ms, 10.2MB)
테스트 16 〉	통과 (0.27ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.63ms, 10.3MB)
테스트 19 〉	통과 (0.97ms, 10.2MB)
테스트 20 〉	통과 (1.11ms, 10.2MB)
'''