# 조이스틱
def move_vertical(s1,s2):
    dist = abs(ord(s1) - ord(s2) )
    return dist if dist <= 13 else 26-dist

def move_horizontal(N, s, cur):
    for dx in range(1,N//2+1):
        next = cur + dx if cur + dx < N else cur + dx - N
        if s[next] != 'A': return dx, next
        next = cur - dx if cur - dx >= 0 else N + cur - dx
        if s[next] != 'A': return dx, next
    return 0,cur

def solution(name):
    answer = 0
    N, cur = len(name), 0
    while True:
        # 상하이동
        answer += move_vertical(name[cur], 'A')   
        name = name[:cur] + 'A' + name[cur+1:]
        # 좌우이동
        moves_x,cur = move_horizontal(N, name, cur)
        answer += moves_x
        # 변환 완료
        if moves_x == 0: return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''