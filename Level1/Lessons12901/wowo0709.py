import sys
input = sys.stdin.readline

def solution(a, b):
    answer = ''
    dates = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    days = {0:"FRI",1:"SAT",2:"SUN",3:"MON",4:"TUE",5:"WED",6:"THU"}
    gap = sum(dates[1:a]) + b - 1
    answer = days[gap%7]
    return answer
