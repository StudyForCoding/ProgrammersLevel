#2개 이하로 다른 비트
def solution(numbers):
    answer = []
    for number in numbers:
        if number%2 == 0:
            answer.append(number+1)
        else:
            bin_num = '0'+bin(number)[2:]
            for i in range(len(bin_num)-1,-1,-1):
                if bin_num[i] == '0':
                    answer.append(int(bin_num[:i]+'10'+bin_num[i+2:],2))
                    break
                    
    return answer
'''
테스트 1 〉	통과 (0.92ms, 10.3MB)
테스트 2 〉	통과 (56.66ms, 26.1MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.89ms, 10.3MB)
테스트 5 〉	통과 (0.95ms, 10.3MB)
테스트 6 〉	통과 (1.01ms, 10.3MB)
테스트 7 〉	통과 (54.24ms, 26MB)
테스트 8 〉	통과 (56.53ms, 25.2MB)
테스트 9 〉	통과 (51.19ms, 24.9MB)
테스트 10 〉	통과 (268.86ms, 26.8MB)
테스트 11 〉	통과 (251.50ms, 26.8MB)
'''