# 2개 이하로 다른 비트

# 맨 오른쪽 0을 1로 바꾸고 바꾼 인덱스에서 오른쪽 인덱스부터 1을 0으로 바꿈
def solution(numbers):
    answer = []
    for num in numbers:
        # 짝수일 때
        if num % 2 == 0: 
            answer.append(num+1)
            continue
        # 홀수일 때
        binNum = bin(num)[2:]

        idx0r = binNum.rfind('0')
        if idx0r == -1: 
            binNum = '1' + binNum
            idx0r = 0
        else: binNum = binNum[:idx0r] + '1' + binNum[idx0r+1:]

        idx1r = binNum.find('1',idx0r+1)
        if idx1r == -1: answer.append(int(binNum,2))
        else: answer.append(int(binNum[:idx1r] + '0' + binNum[idx1r+1:],2))

    return answer

# 시간 초과
# def solution(numbers):
#     answer = []
#     for num in numbers:
#         compNum = num
#         while True:
#             compNum += 1
#             if bin(num ^ compNum).count('1') <= 2:
#                 answer.append(compNum)
#                 break
#     return answer

'''
정확성  테스트
테스트 1 〉	통과 (1.05ms, 10.3MB)
테스트 2 〉	통과 (57.26ms, 26.2MB)
테스트 3 〉	통과 (0.10ms, 10.1MB)
테스트 4 〉	통과 (0.71ms, 10.2MB)
테스트 5 〉	통과 (0.94ms, 10.3MB)
테스트 6 〉	통과 (0.93ms, 10.2MB)
테스트 7 〉	통과 (58.15ms, 26.1MB)
테스트 8 〉	통과 (58.44ms, 25.3MB)
테스트 9 〉	통과 (53.93ms, 24.9MB)
테스트 10 〉	통과 (113.28ms, 26.8MB)
테스트 11 〉	통과 (120.63ms, 26.8MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''