# 소수 찾기
import math
def find(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
def solution(n):
    answer = 0
    for num in range(1,n+1):
        if find(num) == True:
            answer += 1
    return answer - 1

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.15ms, 10.2MB)
# 테스트 3 〉	통과 (0.45ms, 10.2MB)
# 테스트 4 〉	통과 (1.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.64ms, 10.2MB)
# 테스트 6 〉	통과 (6.96ms, 10.2MB)
# 테스트 7 〉	통과 (2.01ms, 10.2MB)
# 테스트 8 〉	통과 (6.30ms, 10.2MB)
# 테스트 9 〉	통과 (8.38ms, 10.2MB)
# 테스트 10 〉	통과 (583.00ms, 10.2MB)
# 테스트 11 〉	통과 (2783.02ms, 10.2MB)
# 테스트 12 〉	통과 (643.36ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (3072.63ms, 10.2MB)
# 테스트 2 〉	통과 (3116.81ms, 10.2MB)
# 테스트 3 〉	통과 (3052.76ms, 10.2MB)
# 테스트 4 〉	통과 (2979.43ms, 10.2MB)