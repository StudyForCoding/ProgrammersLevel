# 행렬의 곱셉

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (3.83ms, 10.2MB)
테스트 2 〉	통과 (76.16ms, 10.9MB)
테스트 3 〉	통과 (82.93ms, 11.2MB)
테스트 4 〉	통과 (3.11ms, 10.3MB)
테스트 5 〉	통과 (55.40ms, 10.9MB)
테스트 6 〉	통과 (32.30ms, 11.1MB)
테스트 7 〉	통과 (2.01ms, 10.2MB)
테스트 8 〉	통과 (0.65ms, 10.2MB)
테스트 9 〉	통과 (0.50ms, 10.1MB)
테스트 10 〉	통과 (56.31ms, 10.5MB)
테스트 11 〉	통과 (5.15ms, 10.2MB)
테스트 12 〉	통과 (1.16ms, 10.2MB)
테스트 13 〉	통과 (41.38ms, 10.9MB)
테스트 14 〉	통과 (84.75ms, 11.1MB)
테스트 15 〉	통과 (25.40ms, 10.5MB)
테스트 16 〉	통과 (7.61ms, 10.7MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''