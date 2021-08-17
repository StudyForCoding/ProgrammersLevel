# 핸드폰 번호 가리기

def solution(phone_number):
    phone_number_len = len(phone_number)
    return "*"*(phone_number_len-4) + phone_number[phone_number_len-4:]

'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
'''