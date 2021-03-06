# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
'''
'''
테스트 1 〉	통과 (84.01ms, 28MB)
테스트 2 〉	통과 (76.33ms, 27.9MB)
테스트 3 〉	통과 (84.00ms, 27.9MB)
테스트 4 〉	통과 (75.86ms, 28MB)
'''