#행렬의 덧셈
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j] 
    return arr1
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.2MB)
테스트 3 〉	통과 (0.35ms, 10.3MB)
테스트 4 〉	통과 (0.17ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (0.21ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.11ms, 10.2MB)
테스트 9 〉	통과 (0.96ms, 10.9MB)
테스트 10 〉	통과 (0.98ms, 10.6MB)
테스트 11 〉	통과 (0.36ms, 10.5MB)
테스트 12 〉	통과 (0.91ms, 10.6MB)
테스트 13 〉	통과 (0.73ms, 10.3MB)
테스트 14 〉	통과 (0.86ms, 10.6MB)
테스트 15 〉	통과 (0.52ms, 10.6MB)
테스트 16 〉	통과 (0.80ms, 10.6MB)
테스트 17 〉	통과 (25.16ms, 20.7MB)
'''