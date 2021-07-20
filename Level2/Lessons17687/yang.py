# [3차] N진수 게임
A2F = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def cal(n,max):
    num_list = '0'
    num  = 1
    while(1):
        if len(num_list) >= max:
            break
        result = []
        
        tmp_num = num
        while(tmp_num):
            if (tmp_num % n) in A2F.keys():
                result.insert(0, A2F[tmp_num%n])
            else:
                result.insert(0, str(tmp_num % n))           
            tmp_num = tmp_num // n
        num_list += ''.join(result)
        num += 1
    return num_list
def solution(n, t, m, p):
    answer = ''
    max = t * m 
    string = cal(n, max)
    print(string)
    for i in range(0, len(string)):
        answer += string[(i*m+p)-1]
        if len(answer) == t:
            break
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.34ms, 10.3MB)
# 테스트 6 〉	통과 (0.29ms, 10.3MB)
# 테스트 7 〉	통과 (0.29ms, 10.2MB)
# 테스트 8 〉	통과 (0.31ms, 10.2MB)
# 테스트 9 〉	통과 (0.35ms, 10.3MB)
# 테스트 10 〉	통과 (0.32ms, 10.4MB)
# 테스트 11 〉	통과 (0.37ms, 10.3MB)
# 테스트 12 〉	통과 (0.32ms, 10.2MB)
# 테스트 13 〉	통과 (0.32ms, 10.3MB)
# 테스트 14 〉	통과 (35.45ms, 10.3MB)
# 테스트 15 〉	통과 (37.44ms, 10.4MB)
# 테스트 16 〉	통과 (38.79ms, 10.4MB)
# 테스트 17 〉	통과 (2.02ms, 10.3MB)
# 테스트 18 〉	통과 (2.57ms, 10.3MB)
# 테스트 19 〉	통과 (0.91ms, 10.2MB)
# 테스트 20 〉	통과 (1.97ms, 10.3MB)
# 테스트 21 〉	통과 (9.85ms, 10.3MB)
# 테스트 22 〉	통과 (5.11ms, 10.3MB)
# 테스트 23 〉	통과 (12.90ms, 10.4MB)
# 테스트 24 〉	통과 (19.09ms, 10.3MB)
# 테스트 25 〉	통과 (16.36ms, 10.3MB)
# 테스트 26 〉	통과 (6.27ms, 10.3MB)