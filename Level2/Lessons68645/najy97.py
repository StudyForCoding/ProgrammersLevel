#삼각 달팽이
def solution(n):
    triangle = [[0 for _ in range(0, _)] for _ in range(1, n + 1)]
    x = -1
    y = 0
    k = 1
    for a in range(n):
        for b in range(a, n):
            if a % 3 == 0:
                x += 1
            elif a % 3 == 1:
                y += 1
            elif a % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = k
            k += 1 
    answer = sum(triangle, [])
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (2.33ms, 10.9MB)
테스트 5 〉	통과 (2.35ms, 11MB)
테스트 6 〉	통과 (1.39ms, 10.8MB)
테스트 7 〉	통과 (1689.78ms, 58.7MB)
테스트 8 〉	통과 (2452.74ms, 58.9MB)
테스트 9 〉	통과 (2141.98ms, 57MB)
'''