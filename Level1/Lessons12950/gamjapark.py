# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer


'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.14ms, 10.3MB)
테스트 3 〉	통과 (0.45ms, 10.3MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (0.23ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.13ms, 10.4MB)
테스트 9 〉	통과 (0.95ms, 10.9MB)
테스트 10 〉	통과 (1.12ms, 10.8MB)
테스트 11 〉	통과 (0.73ms, 10.5MB)
테스트 12 〉	통과 (0.98ms, 10.6MB)
테스트 13 〉	통과 (0.79ms, 10.6MB)
테스트 14 〉	통과 (0.85ms, 10.6MB)
테스트 15 〉	통과 (0.89ms, 10.6MB)
테스트 16 〉	통과 (0.86ms, 10.7MB)
테스트 17 〉	통과 (31.99ms, 22.9MB)
'''