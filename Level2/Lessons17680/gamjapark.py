#  [1차] 캐시
# Least Recently Used: 캐시에서 메모리를 다루기 위해 사용되는 알고리즘
# 제한된 리소스 내에서 데이터를 빠르게 저장하고 접근할 수 있어야함
# 메모리 상 가장 최근에 사용된 적 없는 캐시의 메모리부터 대체해 새 데이터 갱신
# cache hit: 값을 cache에서 가져오는 경우
# cache miss: 값을 메모리에서 가져오는 경우

def solution(cacheSize, cities):
    answer = 0
    cities = list(map(lambda x:x.lower(), cities))
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if city in cache:   # hit
            answer += 1
            cache.pop(cache.index(city))
        else:               # miss
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
        cache.append(city)
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (70.39ms, 24.5MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.12ms, 10.2MB)
테스트 14 〉	통과 (0.17ms, 10.2MB)
테스트 15 〉	통과 (0.26ms, 10.2MB)
테스트 16 〉	통과 (0.35ms, 10.3MB)
테스트 17 〉	통과 (0.23ms, 10.3MB)
테스트 18 〉	통과 (0.79ms, 10.2MB)
테스트 19 〉	통과 (1.01ms, 10.2MB)
테스트 20 〉	통과 (1.27ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''