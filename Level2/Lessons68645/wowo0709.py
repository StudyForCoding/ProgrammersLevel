# 삼각 달팽이
def solution(n):
    from itertools import chain
    snail = [[0 for col in range(row+1)] for row in range(n)]
    i, j = -1, 0  # 행, 열
    num = 1
    for dir in range(n):
        for _ in range(dir, n):
            # 0: 왼쪽 아래, 1: 오른쪽, 2: 왼쪽 위
            if dir % 3 == 0: i += 1
            elif dir % 3 == 1: j += 1
            elif dir % 3 == 2: i, j = i-1, j-1
      
            snail[i][j] = num
            num += 1

    return list(chain.from_iterable(snail))


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (1.05ms, 10.8MB)
테스트 5 〉	통과 (1.07ms, 10.9MB)
테스트 6 〉	통과 (2.00ms, 10.9MB)
테스트 7 〉	통과 (141.24ms, 59.9MB)
테스트 8 〉	통과 (171.58ms, 60MB)
테스트 9 〉	통과 (133.95ms, 59.9MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''