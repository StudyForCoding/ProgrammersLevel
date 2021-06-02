# 음양 더하기

def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))])

'''
테스트 1 〉	통과 (0.15ms, 10.1MB)
테스트 2 〉	통과 (0.16ms, 10.2MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.17ms, 10.1MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (0.15ms, 10.2MB)
테스트 7 〉	통과 (0.15ms, 10.2MB)
테스트 8 〉	통과 (0.17ms, 10.2MB)
테스트 9 〉	통과 (0.17ms, 10.2MB)
'''
