# 약수의 개수와 덧셈

```python
def solution(left, right):
    answer = 0
    nums = 0
    num = []
    lft_rht = []
    #2.
    for i in range(left,right+1):
        lft_rht.append(i)
        for j in range(1,i+1):
            if i%j == 0:
                nums+=1
        num.append(nums)
        nums = 0    # nums 초기화해서 다름 수의 약수의 개수 저장하도록

    #3.
    for k in range(len(num)):
        if num[k]%2==0:
            answer+=lft_rht[k]
        else:
            answer-=lft_rht[k]
    return answer

#1. 수의 범위 : left~right
#2. 약수의 개수 구하기
#3. 약수의 개수가 짝수인 수 : +, 약수의 개수가 홀수인 수 : - => return
```

