# 콜라츠 추측
def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return i
        elif num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return -1

# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.16ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.16ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.1MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.16ms, 10MB)
# 테스트 11 〉	통과 (0.17ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.04ms, 10.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.2MB)
# 테스트 16 〉	통과 (0.03ms, 10.2MB)