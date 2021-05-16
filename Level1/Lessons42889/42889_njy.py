# 실패율
def solution(N, stages):
    # 스테이지별 도달한 유저 수, 실패율 딕셔너리 선언
    clear = dict()
    err_rate = dict()

    # stages에 없는 스테이지의 딕셔너리도 초기화
    for i in range(N+1):
        clear[i+1] = 0
        err_rate[i+1] = 0
    # 스테이지별 도달한 유저 수 계산
    for stage in stages:
        clear[stage] += 1
    # N+1번째부터 도달한 유저가 없는 스테이지 탐색
    for zero in range(N+1,0,-1):
        if clear[zero] != 0:
            zero += 1
            break

    total = len(stages) # 전체 유저 수

    # 도달한 유저가 있는 스테이지만 연산
    for i in range(1,zero):
        err_rate[i] = clear[i]/total # 실패율 계산
        total -= clear[i] # 누적 유저수 - 이번 스테이지 유저수
    err_rate.pop(N+1) # N+1번째 스테이지에 대한 딕셔너리 삭제

    answer = sorted(err_rate, key= lambda x : err_rate[x], reverse=True) # 내림차순으로 정렬
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.3MB)
테스트 3 〉	통과 (1.34ms, 10.4MB)
테스트 4 〉	통과 (6.71ms, 10.9MB)
테스트 5 〉	통과 (16.99ms, 15MB)
테스트 6 〉	통과 (0.17ms, 10.3MB)
테스트 7 〉	통과 (1.00ms, 10.3MB)
테스트 8 〉	통과 (6.40ms, 10.8MB)
테스트 9 〉	통과 (18.41ms, 15.1MB)
테스트 10 〉	통과 (7.37ms, 10.7MB)
테스트 11 〉	통과 (7.28ms, 10.9MB)
테스트 12 〉	통과 (10.82ms, 11.3MB)
테스트 13 〉	통과 (11.12ms, 11.4MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (4.64ms, 10.6MB)
테스트 16 〉	통과 (2.55ms, 10.4MB)
테스트 17 〉	통과 (4.89ms, 10.6MB)
테스트 18 〉	통과 (2.59ms, 10.2MB)
테스트 19 〉	통과 (0.78ms, 10.4MB)
테스트 20 〉	통과 (3.37ms, 10.4MB)
테스트 21 〉	통과 (6.89ms, 10.8MB)
테스트 22 〉	통과 (18.70ms, 18.4MB)
테스트 23 〉	통과 (13.36ms, 11.7MB)
테스트 24 〉	통과 (13.06ms, 11.8MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
'''