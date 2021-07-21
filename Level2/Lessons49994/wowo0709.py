# 방문 길이

def solution(dirs):
    paths = set() # 중복 제거
    x,y = 0,0
    for dir in dirs:
        if dir == 'U' and y < 5:
            paths.add(((x, y), (x, y+1)))
            y += 1
            
        elif dir  == 'D' and y > -5:
            paths.add(((x, y-1), (x, y)))
            y -= 1
            
        elif dir  == 'R' and x < 5:
            paths.add(((x, y), (x+1, y)))
            x += 1
            
        elif dir  == 'L' and x > -5:
            paths.add(((x-1, y), (x, y)))
            x -= 1
    return len(paths)

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.10ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.05ms, 10.3MB)
테스트 16 〉	통과 (0.24ms, 10.3MB)
테스트 17 〉	통과 (0.24ms, 10.3MB)
테스트 18 〉	통과 (0.25ms, 10.2MB)
테스트 19 〉	통과 (0.24ms, 10.2MB)
테스트 20 〉	통과 (0.27ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''