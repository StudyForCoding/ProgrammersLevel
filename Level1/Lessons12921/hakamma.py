#12921 �Ҽ� ã��

def solution(n):
    num=set(range(2,n+1)) # 2���� n+1������ ����

    for i in range(2,n+1): # 2���� n���� �ݺ���
        if i in num: # ���� i�� num ���տ� �ִٸ�
            num-=set(range(2*i,n+1,i)) # i�� ����� num ���տ��� ����
    return len(num) # num�� �����ִ� ������ ������ �Ҽ��� ����