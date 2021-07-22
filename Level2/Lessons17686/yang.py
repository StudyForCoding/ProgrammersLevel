# [3차] 파일명 정렬
def solution(files):
    answer = []
    tmp = []
    for file in files:
        head = ''
        number = ''
        cnt = 0
        for ch in file:
            if ch.isdigit():
                break
            head += ch
            cnt += 1
        for ch in file[cnt:]:
            if not ch.isdigit():
                break
            number += ch
        tmp.append([head.lower(), int(number),file])
    for ls in sorted(tmp, key = lambda x:(x[0],x[1])):
        answer.append(ls[2])
    return answer

# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (2.54ms, 10.8MB)
# 테스트 4 〉	통과 (2.53ms, 10.7MB)
# 테스트 5 〉	통과 (2.60ms, 10.6MB)
# 테스트 6 〉	통과 (2.62ms, 10.7MB)
# 테스트 7 〉	통과 (2.69ms, 10.7MB)
# 테스트 8 〉	통과 (2.40ms, 10.7MB)
# 테스트 9 〉	통과 (2.47ms, 10.7MB)
# 테스트 10 〉	통과 (2.47ms, 10.8MB)
# 테스트 11 〉	통과 (2.35ms, 10.7MB)
# 테스트 12 〉	통과 (2.37ms, 10.7MB)
# 테스트 13 〉	통과 (2.16ms, 10.5MB)
# 테스트 14 〉	통과 (2.49ms, 10.8MB)
# 테스트 15 〉	통과 (2.55ms, 10.8MB)
# 테스트 16 〉	통과 (2.51ms, 10.7MB)
# 테스트 17 〉	통과 (2.01ms, 10.8MB)
# 테스트 18 〉	통과 (2.09ms, 10.5MB)
# 테스트 19 〉	통과 (2.28ms, 10.4MB)
# 테스트 20 〉	통과 (2.31ms, 10.5MB)