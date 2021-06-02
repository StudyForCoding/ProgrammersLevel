#나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (3.22ms, 13.4MB)
테스트 7 〉	통과 (0.27ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.19ms, 10.2MB)
테스트 10 〉	통과 (0.13ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.1MB)
테스트 13 〉	통과 (0.44ms, 10.3MB)
테스트 14 〉	통과 (0.28ms, 10.3MB)
테스트 15 〉	통과 (0.14ms, 10.3MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''