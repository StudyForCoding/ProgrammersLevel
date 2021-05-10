# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    tmp = [1 if l in win_nums else -1 if l != 0 else 0 for l in lottos]
    return [min(6, 7 - (tmp.count(1) + tmp.count(0))), min(6, 7 - tmp.count(1))]

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
'''