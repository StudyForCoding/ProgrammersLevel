# 약수의 개수와 덧셈
def solution(left, right):
    answer=0
    for num in range(left,right+1):
        cnt  = 0
        for i in range(1,num+1):
            if num%i == 0:
                cnt += 1
        if cnt%2 == 0:
            answer += num
        else:
            answer -= num
    return answer
'''
테스트 1 〉	통과 (19.56ms, 10.3MB)
테스트 2 〉	통과 (5.09ms, 10.1MB)
테스트 3 〉	통과 (4.68ms, 10.1MB)
테스트 4 〉	통과 (2.26ms, 10.2MB)
테스트 5 〉	통과 (17.77ms, 10.2MB)
테스트 6 〉	통과 (1.52ms, 10.3MB)
테스트 7 〉	통과 (0.66ms, 10.1MB)
'''