# 약수의 개수와 덧셈
def find(n):
    count = 0
    for i in range(1, n+ 1):
        if n % i == 0:
            count += 1
    return count
def solution(left, right):
    answer = 0
    for idx in range(left,right + 1):
        tmp = find(idx)
        if tmp % 2 == 0:
            answer += idx
        else:
            answer -= idx
    return answer

# 테스트 1 〉	통과 (21.00ms, 10.3MB)
# 테스트 2 〉	통과 (4.53ms, 10.2MB)
# 테스트 3 〉	통과 (4.50ms, 10.2MB)
# 테스트 4 〉	통과 (2.31ms, 10.2MB)
# 테스트 5 〉	통과 (19.10ms, 10.2MB)
# 테스트 6 〉	통과 (1.41ms, 10.2MB)
# 테스트 7 〉	통과 (0.76ms, 10.2MB)