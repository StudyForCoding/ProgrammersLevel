# 소수 찾기

def solution(numbers):
    from itertools import permutations
    splited_nums = list(numbers)
    made_nums = set()
    for n in range(1,len(splited_nums)+1):
        made_nums |= set(map(int, map(''.join,permutations(splited_nums,n))))

    maxnum = max(made_nums)
    is_prime = [False, False] + [True]*(maxnum-1)
    for i in range(2,int(maxnum**0.5)+1):
        if not is_prime[i]: continue
        for j in range(2*i, maxnum+1, i):
            is_prime[j] = False

    return sum([True for num in made_nums if is_prime[num]])
    

'''
정확성  테스트
테스트 1 〉	통과 (0.34ms, 10.5MB)
테스트 2 〉	통과 (63.43ms, 20.3MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (30.18ms, 15MB)
테스트 5 〉	통과 (373.02ms, 61.1MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.26ms, 10.5MB)
테스트 8 〉	통과 (840.86ms, 94.9MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉	통과 (99.93ms, 25.3MB)
테스트 11 〉	통과 (8.34ms, 11.6MB)
테스트 12 〉	통과 (4.31ms, 11MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

def solution(numbers):
    from itertools import permutations
    splited_nums = list(numbers)
    made_nums = set()
    for n in range(1,len(splited_nums)+1):
        made_nums |= set(map(int, map(''.join,permutations(splited_nums,n))))

    # 소수 리스트를 따로 만들지 않고 소수가 아니면 바로 집합에서 제외
    # continue 문이 없어서 시간은 더 걸림
    maxnum = max(made_nums)
    for i in range(2,int(maxnum**0.5)+1):
        made_nums -= set(range(2*i, maxnum+1,i))

    # 0과 1 제외
    made_nums -= set([0,1])
    return len(made_nums)


'''
정확성  테스트
테스트 1 〉	통과 (0.65ms, 10.5MB)
테스트 2 〉	통과 (222.60ms, 44.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (81.88ms, 20MB)
테스트 5 〉	통과 (1272.84ms, 145MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.72ms, 10.5MB)
테스트 8 〉	통과 (2463.58ms, 280MB)
테스트 9 〉	통과 (0.08ms, 10.4MB)
테스트 10 〉	통과 (343.40ms, 51.1MB)
테스트 11 〉	통과 (23.90ms, 13.7MB)
테스트 12 〉	통과 (12.55ms, 13.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''