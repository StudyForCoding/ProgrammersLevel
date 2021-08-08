# 핸드폰 번호 가리기

```python
def solution(phone_number):
    answer = ''
    lst = []
    for i in range(len(phone_number)):
        lst += phone_number[i]
    for i in range(len(phone_number)-4):
        lst[i] = "*"
    answer ="".join(lst)
    return answer

#phone_number를 리스트에 넣고
#리스트 - 4 의 인덱스만큼 숫자를 *로 치환
#리스트를 다시 문자열화
```

