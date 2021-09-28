# n진수 게임

```python
def solution(n, t, m, p):
    # n = 진법, t = 미리 구할 숫자 갯수, m = 게임에 참여하는 인원, p = 튜브의 순서
    
    def notation(n, base):
        string = "0123456789ABCDEF"
        q,r = divmod(n, base) #q = n//base, r = n%base
        if q == 0:
            return string[r]
        else:
            return notation(q, base) + string[r]
    
    answer = ''
    lst = []
    
    for i in range(t*m):
        candi = notation(i,n)
        for c in candi:
            lst.append(c)
        
    for i in range(p-1,t*m,m):
        answer += lst[i]
        
    return answer

#1. 진법 계산할 함수만들면?
#2. t*m = 게임에 참여하는 사람들이 처음~끝까지 외칠 숫자
#3. 2 중 튜브가 외칠 숫자만 따로 빼서 작성
```

