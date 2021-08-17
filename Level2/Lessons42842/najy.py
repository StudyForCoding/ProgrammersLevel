# 카펫

def solution(brown, yellow):
    x,y = 0,0
    const = brown/2 + 2
    c1, c2 = -1*const, brown+yellow
    while(True):
        if y**2+c1*y+c2 == 0:
            x = const-y
            return [x,y]
        y += 1
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.42ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.16ms, 10.2MB)
테스트 7 〉	통과 (0.36ms, 10.2MB)
테스트 8 〉	통과 (0.43ms, 10.2MB)
테스트 9 〉	통과 (0.44ms, 10.1MB)
테스트 10 〉	통과 (0.63ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
'''