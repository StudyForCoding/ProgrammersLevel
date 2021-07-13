# 최댓값과 최솟값

def solution(s):
    n = list(map(int,s.split()))
    mymax,mymin = n[0],n[0]
    for nbr in n:
        if nbr > mymax: mymax = nbr
        elif nbr < mymin: mymin = nbr

    return " ".join([str(mymin),str(mymax)])

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''