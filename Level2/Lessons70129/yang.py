# 이진 변환 반복하기
def cal(s):

    cnt = 0
    cnt = s.count("0")
    s = s.replace('0','')
    return bin(len(s))[2:], cnt
def solution(s):
    answer = [0, 0]
    iter = 0
    while(1):
        iter += 1
        s, cnt = cal(s)
        answer[1] += cnt
        if s == '1':
            break
    answer[0] = iter
    print(answer)
    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (1.86ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.53ms, 10.3MB)
# 테스트 10 〉	통과 (2.07ms, 10.3MB)
# 테스트 11 〉	통과 (1.59ms, 10.4MB)