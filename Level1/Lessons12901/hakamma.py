2016년 연습문제 (날짜)

def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    x = 0
    for i in range(0, a-1):
        x = x+month[i]
    
    answer = day[(x+b-1)%7]
    return answer