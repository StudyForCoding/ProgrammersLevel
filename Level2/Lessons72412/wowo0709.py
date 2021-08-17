# 순위 검색

def solution(infos, querys):
    # 조건 해쉬맵 생성
    from itertools import combinations
    info_dict = dict()
    for info in infos:
        conds = info.split()
        for n in range(5):                            # "-" 를 0~4개 삽입 가능
            idx_list = list(combinations(range(4),n)) # "-"를 삽입하는 위치에 대한 콤비네이션
            for idxs in idx_list:      # 각 위치(인덱스 리스트)에 대해
                tmp = conds[:4].copy() # 조건(점수 제외) 복사
                for idx in idxs:   # 각 인덱스에 대해
                    tmp[idx] = "-" # 인덱스에 "-" 삽입
                info_dict_key = "_".join(tmp)
                '''dict.get() 쓰면 시간 2배 이상 걸림'''
                # info_dict[info_dict_key] = info_dict.get(info_dict_key,[]) + [int(conds[4])]
                if info_dict_key in info_dict: info_dict[info_dict_key].append(int(conds[4]))
                else: info_dict[info_dict_key] = [int(conds[4])]
    '''먼저 정렬하지 않고 탐색 시마다 정렬하면 시간 초과'''
    # 점수 정렬 -> 이진 탐색 알고리즘
    for values in info_dict.values(): 
        values.sort()
    
    # 조건 비교
    from bisect import bisect_left
    ans = []
    for query in querys:
        query = [q for q in query.split() if q != "and"]
        info_dict_key = "_".join(query[:4])
        if info_dict_key in info_dict: # 조건을 만족하는 후보에 한해 커트라인 점수를 적용 
            candidates = info_dict[info_dict_key]
            cnt = len(candidates) - bisect_left(candidates,int(query[4]))
        else:                          # 조건을 만족하는 후보가 없음
            cnt = 0
        ans.append(cnt)

    return ans


''' dict.get() 안 썼을 때
정확성  테스트
테스트 1 〉	통과 (0.92ms, 10.3MB)
테스트 2 〉	통과 (2.26ms, 10.4MB)
테스트 3 〉	통과 (1.24ms, 10.4MB)
테스트 4 〉	통과 (1.89ms, 10.5MB)
테스트 5 〉	통과 (3.16ms, 10.4MB)
테스트 6 〉	통과 (91.08ms, 10.5MB)
테스트 7 〉	통과 (4.74ms, 10.7MB)
테스트 8 〉	통과 (83.77ms, 11.5MB)
테스트 9 〉	통과 (116.94ms, 13.3MB)
테스트 10 〉	통과 (75.92ms, 13.9MB)
테스트 11 〉	통과 (3.78ms, 10.5MB)
테스트 12 〉	통과 (10.95ms, 10.7MB)
테스트 13 〉	통과 (3.74ms, 10.7MB)
테스트 14 〉	통과 (56.83ms, 12.1MB)
테스트 15 〉	통과 (53.62ms, 12MB)
테스트 16 〉	통과 (5.76ms, 10.4MB)
테스트 17 〉	통과 (8.37ms, 10.7MB)
테스트 18 〉	통과 (43.91ms, 12.1MB)
효율성  테스트
테스트 1 〉	통과 (982.25ms, 64.4MB)
테스트 2 〉	통과 (992.74ms, 63.9MB)
테스트 3 〉	통과 (984.64ms, 63.8MB)
테스트 4 〉	통과 (875.99ms, 64.4MB)
채점 결과
정확성: 40.0
효율성: 60.0
합계: 100.0 / 100.0
'''

''' dict.get() 썼을 대
정확성  테스트
테스트 1 〉	통과 (1.07ms, 10.4MB)
테스트 2 〉	통과 (1.10ms, 10.4MB)
테스트 3 〉	통과 (1.66ms, 10.3MB)
테스트 4 〉	통과 (3.68ms, 10.5MB)
테스트 5 〉	통과 (3.37ms, 10.4MB)
테스트 6 〉	통과 (18.59ms, 10.4MB)
테스트 7 〉	통과 (3.81ms, 10.7MB)
테스트 8 〉	통과 (307.80ms, 11.6MB)
테스트 9 〉	통과 (290.81ms, 13.4MB)
테스트 10 〉	통과 (429.54ms, 14.1MB)
테스트 11 〉	통과 (5.84ms, 10.5MB)
테스트 12 〉	통과 (19.18ms, 10.8MB)
테스트 13 〉	통과 (6.81ms, 10.7MB)
테스트 14 〉	통과 (117.25ms, 12.2MB)
테스트 15 〉	통과 (121.46ms, 12.1MB)
테스트 16 〉	통과 (4.99ms, 10.5MB)
테스트 17 〉	통과 (41.35ms, 10.7MB)
테스트 18 〉	통과 (107.22ms, 12.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0
'''


# 정확성 성공, 효율성 실패 (초기 코드)
def solution(infos, querys):
    # 각 원소를 리스트로 변환
    infos = sorted(list(map(lambda i: i.split(), infos)), key = lambda i:int(i[4]))
    score_list = [int(i[4]) for i in infos]
    # 조건 비교
    ans = [0 for _ in range(len(querys))]
    for e,q in enumerate(querys):
        q = list(ch for ch in q.split() if ch != 'and')
        # 최저 점수 커트라인 
        from bisect import bisect_left
        limit_idx = bisect_left(score_list,int(q[4]))
        # 커트라인 이상인 대상들에 한해 조건 비교
        for i in infos[limit_idx:]:
            for idx in range(4):
                if q[idx] == '-': continue
                if q[idx] != i[idx]: break
            else: 
                ans[e] += 1

    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.48ms, 10.3MB)
테스트 2 〉	통과 (0.54ms, 10.4MB)
테스트 3 〉	통과 (1.57ms, 10.4MB)
테스트 4 〉	통과 (6.01ms, 10.4MB)
테스트 5 〉	통과 (42.09ms, 10.5MB)
테스트 6 〉	통과 (66.00ms, 10.6MB)
테스트 7 〉	통과 (24.66ms, 10.6MB)
테스트 8 〉	통과 (133.67ms, 13.2MB)
테스트 9 〉	통과 (129.67ms, 13.4MB)
테스트 10 〉	통과 (120.34ms, 13.5MB)
테스트 11 〉	통과 (19.80ms, 10.5MB)
테스트 12 〉	통과 (82.27ms, 10.7MB)
테스트 13 〉	통과 (21.95ms, 10.5MB)
테스트 14 〉	통과 (95.18ms, 11.9MB)
테스트 15 〉	통과 (119.80ms, 11.8MB)
테스트 16 〉	통과 (21.95ms, 10.5MB)
테스트 17 〉	통과 (44.35ms, 10.6MB)
테스트 18 〉	통과 (95.29ms, 11.9MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0
'''


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
        ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),
        sep='\n')