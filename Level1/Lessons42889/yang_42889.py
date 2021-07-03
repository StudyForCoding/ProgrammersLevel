# 실패율
def solution(N, stages):
    rate = dict()
    total = len(stages)
    for cnt in range(1, N + 1):
        if total == 0:
            rate[cnt] = 0
            continue
        rate[cnt] = stages.count(cnt) / total
        total -= stages.count(cnt)
    return sorted(rate, key=lambda x: rate[x], reverse=True)

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.41ms, 10.2MB)
# 테스트 3 〉	통과 (121.01ms, 10.4MB)
# 테스트 4 〉	통과 (609.96ms, 10.8MB)
# 테스트 5 〉	통과 (2706.15ms, 14.8MB)
# 테스트 6 〉	통과 (1.67ms, 10.2MB)
# 테스트 7 〉	통과 (19.78ms, 10.3MB)
# 테스트 8 〉	통과 (608.06ms, 10.8MB)
# 테스트 9 〉	통과 (2731.82ms, 15MB)
# 테스트 10 〉	통과 (242.35ms, 10.8MB)
# 테스트 11 〉	통과 (618.67ms, 10.8MB)
# 테스트 12 〉	통과 (353.06ms, 11.3MB)
# 테스트 13 〉	통과 (718.98ms, 11.3MB)
# 테스트 14 〉	통과 (0.08ms, 10.1MB)
# 테스트 15 〉	통과 (19.85ms, 10.6MB)
# 테스트 16 〉	통과 (9.32ms, 10.4MB)
# 테스트 17 〉	통과 (23.43ms, 10.5MB)
# 테스트 18 〉	통과 (9.97ms, 10.3MB)
# 테스트 19 〉	통과 (2.59ms, 10.1MB)
# 테스트 20 〉	통과 (17.38ms, 10.2MB)
# 테스트 21 〉	통과 (33.05ms, 10.9MB)
# 테스트 22 〉	통과 (1941.65ms, 18.3MB)
# 테스트 23 〉	통과 (18.98ms, 11.6MB)
# 테스트 24 〉	통과 (96.23ms, 11.6MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)