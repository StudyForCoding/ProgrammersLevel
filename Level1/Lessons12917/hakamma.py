#12917 ���ڿ� ������������ ��ġ�ϱ�

def solution(s):
    answer = ''
    s1 = s.lower()
    upper_char = []
    lower_char = []
    for i in range(len(s)):
        if s[i] == s1[i]:
            lower_char.append(s[i])
        else:
            upper_char.append(s[i])
    upper_char.sort(reverse=True)
    lower_char.sort(reverse=True)
    answer = "".join(lower_char) + "".join(upper_char)
    return answer