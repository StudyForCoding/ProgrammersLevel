#12922 ���ڼ��ڼ��ڼ�?

def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += "��"
        elif i%2 == 1:
            answer += "��"
    return answer