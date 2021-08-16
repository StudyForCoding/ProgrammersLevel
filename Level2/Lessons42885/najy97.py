#구명보트
def solution(people, limit):
    answer = 0
    start, end = 0, len(people)-1
    
    people.sort()
    
    # 혼자 타야되는 사람 컷
    for weight in people:
        if weight > limit-40:
            answer += 1
            end -= 1
    
    # 모든 사람을 구출할 때 까지 반복
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (1.51ms, 10.2MB)
테스트 2 〉	통과 (0.52ms, 10.3MB)
테스트 3 〉	통과 (1.13ms, 10.1MB)
테스트 4 〉	통과 (0.69ms, 10.1MB)
테스트 5 〉	통과 (0.46ms, 10.2MB)
테스트 6 〉	통과 (0.28ms, 10.1MB)
테스트 7 〉	통과 (0.32ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉통과 (0.69ms, 10.3MB)
테스트 11 〉통과 (0.52ms, 10.1MB)
테스트 12 〉통과 (0.51ms, 10.3MB)
테스트 13 〉통과 (0.58ms, 10.2MB)
테스트 14 〉통과 (0.61ms, 10.1MB)
테스트 15 〉통과 (0.06ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (9.28ms, 10.6MB)
테스트 2 〉	통과 (7.08ms, 10.6MB)
테스트 3 〉	통과 (9.88ms, 10.5MB)
테스트 4 〉	통과 (7.49ms, 10.5MB)
테스트 5 〉	통과 (7.17ms, 10.6MB)
'''