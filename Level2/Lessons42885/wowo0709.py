# 구명보트
def solution(people, limit):
    from collections import deque
    dq = deque(sorted(people))
    ans = 0
    while people:
        if dq[-1] + dq[0] <= limit: dq.pop();dq.popleft()
        else: dq.pop()
        ans += 1
    return ans