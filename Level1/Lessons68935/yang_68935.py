def solution(n):
    answer = 0
    y = []
    while(1):
        if n < 3:
            y.insert(0,n)
            break;
        y.insert(0,n % 3)
        n //= 3
      
    for idx in range(len(y)-1,-1,-1):
        answer += y[idx] * (3 ** idx)
    return answer