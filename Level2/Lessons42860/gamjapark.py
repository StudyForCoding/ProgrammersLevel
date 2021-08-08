# 조이스틱
def solution(name):
    answer = cursor = 0
    name_count = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    name_sum = sum(name_count)

    while True:
        answer += name_count[cursor]
        name_count[cursor] = 0
        if sum(name_count) == 0:
            return answer
        
        left = right = 1
        while name_count[cursor-left] == 0:
            left += 1
        while name_count[cursor+right] == 0:
            right += 1
            
        if left < right:
            cursor -= left
            answer += left
        else:
            cursor += right
            answer += right
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
