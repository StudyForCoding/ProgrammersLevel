# 캐시
def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache: # cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:             # cache miss
            cache.append(city) 
            answer += 5
            if len(cache) > cacheSize: cache.pop(0)

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (65.28ms, 17.5MB)
테스트 12 〉	통과 (0.04ms, 10.1MB)
테스트 13 〉	통과 (0.09ms, 10.1MB)
테스트 14 〉	통과 (0.14ms, 10.2MB)
테스트 15 〉	통과 (0.18ms, 10.2MB)
테스트 16 〉	통과 (0.27ms, 10.2MB)
테스트 17 〉	통과 (0.44ms, 10.3MB)
테스트 18 〉	통과 (0.67ms, 10.3MB)
테스트 19 〉	통과 (0.85ms, 10.3MB)
테스트 20 〉	통과 (1.37ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''