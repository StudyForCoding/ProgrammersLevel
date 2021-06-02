# 비밀지도
def solution(n, arr1, arr2):
    # nxn으로 binary를 저장할 배열 생성
    barr1=[[] for i in range(n)]
    barr2=[[] for i in range(n)]

    # 1xn으로 answer를 저장할 배열 생성
    answer=['' for i in range(n)]

    # arr의 각 행을 binary로 변환(str타입) 후 하나씩 뽑아 int 타입으로 변환한 결과를 list에 저장 
    for i in range(n):
        barr1[i] = list(map(int,format(arr1[i],'b')))
        barr2[i] = list(map(int,format(arr2[i],'b')))
        # 자리수가 n보다 작으면 앞자리를 0으로 채움
        while len(barr1[i])<n:
            barr1[i].insert(0,0)
        while len(barr2[i])<n:
            barr2[i].insert(0,0)
        # 두 배열의 합이 0이면 공백, 그 외의 경우 #
        for idx in range(n):
            if barr1[i][idx]+barr2[i][idx] == 0: 
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer
'''
테스트 1 〉	통과 (0.10ms, 10.3MB)
테스트 2 〉	통과 (0.22ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.12ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.4MB)
테스트 6 〉	통과 (0.13ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.5MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
'''