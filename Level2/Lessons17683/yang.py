# 방금 그곡 (4개 실패)
def pre(m):
    m = m.replace('C#','1')
    m = m.replace('D#','2')
    m = m.replace('F#','3')
    m = m.replace('G#','4')
    m = m.replace('A#','5')
    return m
def solution(m, musicinfos):
    answer = ''
    t = 0
    m = pre(m)
    for info in musicinfos:
        music = ''
        info = info.split(',')
        info[3] = pre(info[3])
        time = (int(info[1][:2])-int(info[0][:2]))*60+(int(info[1][3:])-int(info[0][3:]))

        i = -1
        flag = 0
        while(flag == 0):
            i += 1
            music += info[3][i%len(info[3])]
            if m in music:
                if t < time:
                    answer = info[2]
                    t = time
                flag = 1
            if i == time:
                flag = 1
        
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.04ms, 10.4MB)
# 테스트 5 〉	통과 (0.04ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (1.43ms, 10.4MB)
# 테스트 8 〉	통과 (1.50ms, 10.4MB)
# 테스트 9 〉	통과 (1.57ms, 10.4MB)
# 테스트 10 〉	통과 (0.92ms, 10.4MB)
# 테스트 11 〉	통과 (1.19ms, 10.5MB)
# 테스트 12 〉	통과 (1.12ms, 10.4MB)
# 테스트 13 〉	통과 (1.68ms, 10.4MB)
# 테스트 14 〉	통과 (1.49ms, 10.5MB)
# 테스트 15 〉	통과 (1.44ms, 10.4MB)
# 테스트 16 〉	통과 (0.96ms, 10.4MB)
# 테스트 17 〉	통과 (1.26ms, 10.5MB)
# 테스트 18 〉	통과 (1.47ms, 10.5MB)
# 테스트 19 〉	통과 (1.03ms, 10.4MB)
# 테스트 20 〉	통과 (0.50ms, 10.5MB)
# 테스트 21 〉	통과 (1.75ms, 10.4MB)
# 테스트 22 〉	실패 (1.28ms, 10.5MB)
# 테스트 23 〉	실패 (1.35ms, 10.4MB)
# 테스트 24 〉	실패 (1.19ms, 10.5MB)
# 테스트 25 〉	통과 (0.05ms, 10.4MB)
# 테스트 26 〉	통과 (0.05ms, 10.4MB)
# 테스트 27 〉	통과 (0.05ms, 10.4MB)
# 테스트 28 〉	통과 (0.04ms, 10.4MB)
# 테스트 29 〉	실패 (7.22ms, 10.5MB)
# 테스트 30 〉	통과 (7.51ms, 10.5MB)