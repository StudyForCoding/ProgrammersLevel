# 구명보트
def solution(people, limit):
    people.sort()
    ans = 0
    start, end = 0, len(people)-1
    while start <= end:
        if people[start] + people[end] <= limit: start, end = start+1, end-1
        else: end -= 1
        ans += 1
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.80ms, 10.1MB)
테스트 2 〉	통과 (0.68ms, 10.1MB)
테스트 3 〉	통과 (0.57ms, 10.2MB)
테스트 4 〉	통과 (0.51ms, 10.3MB)
테스트 5 〉	통과 (0.31ms, 10.1MB)
테스트 6 〉	통과 (0.18ms, 10.2MB)
테스트 7 〉	통과 (0.46ms, 10.1MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10MB)
테스트 10 〉	통과 (0.54ms, 10.2MB)
테스트 11 〉	통과 (0.47ms, 10.1MB)
테스트 12 〉	통과 (0.42ms, 10.2MB)
테스트 13 〉	통과 (0.58ms, 10.1MB)
테스트 14 〉	통과 (0.71ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (8.58ms, 10.6MB)
테스트 2 〉	통과 (8.86ms, 10.6MB)
테스트 3 〉	통과 (8.34ms, 10.6MB)
테스트 4 〉	통과 (9.34ms, 10.6MB)
테스트 5 〉	통과 (8.53ms, 10.5MB)
채점 결과
정확성: 75.0
효율성: 25.0
합계: 100.0 / 100.0
'''