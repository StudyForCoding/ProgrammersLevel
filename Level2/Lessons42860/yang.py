# 조이스틱
def solution(name):
    moves = []
    for s in name:
        if ord(s) < 77.5:
            moves.append(ord(s) - ord('A'))
        else:
            moves.append(ord('Z') - ord(s) + 1)
    idx = 0
    answer = 0
    while True:
        answer += moves[idx]
        moves[idx] = 0

        if sum(moves) == 0:
            break

        left_A = 1
        right_A = 1

        while moves[idx - left_A] == 0:
            left_A += 1

        while moves[idx + right_A] == 0:
            right_A += 1

        if left_A >= right_A:
            idx += right_A
            answer += right_A

        else:
            idx -= left_A
            answer += left_A

    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)