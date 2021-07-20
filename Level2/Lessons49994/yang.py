# 방문 길이
def solution(dirs):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    dic = {"U": 0, "L":1, "D":2, "R": 3}

    road = set()
    x, y = 0, 0
    for dir in dirs:
        i = dic[dir]
        nx, ny = x + dx[i], y + dy[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in road:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))
        x, y = nx, ny

    return len(road)/2
# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 테스트 11 〉	통과 (0.04ms, 10.2MB)
# 테스트 12 〉	통과 (0.08ms, 10.4MB)
# 테스트 13 〉	통과 (0.07ms, 10.2MB)
# 테스트 14 〉	통과 (0.08ms, 10.3MB)
# 테스트 15 〉	통과 (0.07ms, 10.3MB)
# 테스트 16 〉	통과 (0.26ms, 10.3MB)
# 테스트 17 〉	통과 (0.29ms, 10.2MB)
# 테스트 18 〉	통과 (0.33ms, 10.3MB)
# 테스트 19 〉	통과 (0.27ms, 10.2MB)
# 테스트 20 〉	통과 (0.27ms, 10.2MB)