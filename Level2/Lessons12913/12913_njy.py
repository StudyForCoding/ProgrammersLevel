#땅따먹기

def solution(land):
    size = len(land)-1
    for i in range(0, size):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    return max(land[size])

"""
정확성  테스트
테스트 1 〉	통과 (1.57ms, 10.4MB)
테스트 2 〉	통과 (1.74ms, 10.3MB)
테스트 3 〉	통과 (1.63ms, 10.3MB)
테스트 4 〉	통과 (1.81ms, 10.3MB)
테스트 5 〉	통과 (1.67ms, 10.4MB)
테스트 6 〉	통과 (1.60ms, 10.3MB)
테스트 7 〉	통과 (2.43ms, 10.4MB)
테스트 8 〉	통과 (1.88ms, 10.4MB)
테스트 9 〉	통과 (1.56ms, 10.2MB)
테스트 10 〉	통과 (1.71ms, 10.4MB)
테스트 11 〉	통과 (1.82ms, 10.4MB)
테스트 12 〉	통과 (1.81ms, 10.3MB)
테스트 13 〉	통과 (1.60ms, 10.3MB)
테스트 14 〉	통과 (1.75ms, 10.3MB)
테스트 15 〉	통과 (1.91ms, 10.3MB)
테스트 16 〉	통과 (1.78ms, 10.3MB)
테스트 17 〉	통과 (1.85ms, 10.4MB)
테스트 18 〉	통과 (1.50ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (138.44ms, 32.5MB)
테스트 2 〉	통과 (123.75ms, 32.4MB)
테스트 3 〉	통과 (122.34ms, 32.4MB)
테스트 4 〉	통과 (135.32ms, 32.4MB)
"""