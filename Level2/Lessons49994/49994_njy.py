#방문 길이
def solution(dirs):
    # 이동
    x = 0; y = 0
    route = []
    for dir in dirs:
        if dir == 'U' and y < 5:
            route.append(((x, y), (x, y+1)))
            y += 1
        elif dir == 'D' and y > -5:
            route.append(((x, y-1), (x, y)))
            y -= 1
        elif dir == 'R' and x < 5:
            route.append(((x, y), (x+1, y)))
            x += 1
        elif dir == 'L' and x > -5:
            route.append(((x-1, y), (x, y)))
            x -= 1
    route = set(route)

    return len(route)

"""
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.35ms, 10.3MB)
테스트 17 〉	통과 (0.35ms, 10.3MB)
테스트 18 〉	통과 (0.38ms, 10.2MB)
테스트 19 〉	통과 (0.35ms, 10.2MB)
테스트 20 〉	통과 (0.35ms, 10.2MB)
"""