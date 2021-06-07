# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    for y in range(len(arr1)):
        answer.append([])
        for x in range(len(arr1[0])):
            answer[y].append(arr1[y][x] + arr2[y][x])
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.20ms, 10.2MB)
# 테스트 3 〉	통과 (0.50ms, 10.3MB)
# 테스트 4 〉	통과 (0.25ms, 10.2MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.25ms, 10.1MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.09ms, 10.2MB)
# 테스트 9 〉	통과 (1.33ms, 10.9MB)
# 테스트 10 〉	통과 (1.22ms, 10.7MB)
# 테스트 11 〉	통과 (0.85ms, 10.3MB)
# 테스트 12 〉	통과 (0.94ms, 10.5MB)
# 테스트 13 〉	통과 (0.89ms, 10.5MB)
# 테스트 14 〉	통과 (1.00ms, 10.6MB)
# 테스트 15 〉	통과 (1.05ms, 10.6MB)
# 테스트 16 〉	통과 (0.78ms, 10.6MB)
# 테스트 17 〉	통과 (33.97ms, 22.9MB)