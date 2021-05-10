# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    # 0개 1개 ... 6개 동일할 때 등수
    rank = [6,6,5,4,3,2,1]
    
    # 당첨번호 카운터
    count_lottos = {}
    count_win = {}
    count = 0
    
    # 0이 없는 경우 대비
    count_lottos[0] = 0

    # 당첨번호 카운트
    for num in win_nums:
        count_lottos[num] = 0
        count_win[num] = 1

    # 추첨번호 카운트
    for num in lottos:
        try:count_lottos[num] += 1
        except:count_lottos[num] = 1

    # 등수 계산
    for num in win_nums:
        if count_lottos[num] == count_win[num]:
            count += 1
            
    # 최대
    answer.append(rank[count+count_lottos[0]])
    # 최소
    answer.append(rank[count])
    
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉    통과 (0.01ms, 10.2MB)
테스트 11 〉    통과 (0.01ms, 10.1MB)
테스트 12 〉    통과 (0.01ms, 10.2MB)
테스트 13 〉    통과 (0.01ms, 10.2MB)
테스트 14 〉    통과 (0.01ms, 10.2MB)
테스트 15 〉    통과 (0.01ms, 10.3MB)
"""