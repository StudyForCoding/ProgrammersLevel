#12926 ���� ��ȣ

def solution(s, n):
    low_char = "abcdefghijklmnopqrstuvwxyz"
    up_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low_char:
            ind = low_char.find(char)+n # low ���ڿ����� ã�� �ش� ���ĺ� �ε��� + n
            answer += low_char[ind%26] # 26���� ���� �������� ����� ��� 25�� �ʰ��ϴ� ��쵵 Ȱ�� ����
        elif char in up_char:
            ind = up_char.find(char)+n
            answer += up_char[ind%26]
        else:
            answer += " "
    return answer