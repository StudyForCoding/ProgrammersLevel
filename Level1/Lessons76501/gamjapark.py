# 음양 더하기

def solution(absolutes, signs):
    return sum([x if y else -x for x, y in zip(absolutes, signs)])

'''
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.2MB)
테스트 3 〉	통과 (0.11ms, 10.2MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.12ms, 10.3MB)
테스트 6 〉	통과 (0.11ms, 10.2MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.12ms, 10.3MB)
테스트 9 〉	통과 (0.12ms, 10.2MB)
'''