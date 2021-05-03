def solution(a, b):
    answer = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
    tmp = [0,3,3,6,1,4,6,2,5,0,3,5]
    return answer[(6 + tmp[a-1] + b)%7] if a > 2 else answer[(6 + tmp[a-1] + b)%7-1]