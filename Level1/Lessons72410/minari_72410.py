```
def solution(new_id):
    available_id=[]
    new_id = new_id.lower()   #1.대문자를 소문자로 바꿈
    #2.알파벳 소문자,숫자,-,_,. 면 available_id(리스트)에 더한 후, new_id에 리스트->str로 변환
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in '-_.':       
            available_id.append(new_id[i])
    new_id = "".join(available_id)
    #3.마침표 2개 이상->1개로 교환
    for i in range(len(new_id)):
        new_id=new_id.replace("..",".")
    #4. 처음이나 끝에 위치한 . 제거
    new_id=new_id.strip(".")
    #6.new_id 길이>15일 때 15까지만 나타내기
    if len(new_id)>15:
        new_id=new_id[:15]
    #6.처음&끝의 마침표 제거
    new_id=new_id.strip('.')
    #5.new_id가 비었을 때 a 대입
    if new_id=="":
        new_id +=  ("a")   
        
    #7.new_id 길이늘리기
    while len(new_id)<3:
        new_id += (new_id[-1])

    answer=new_id
    return answer
```



