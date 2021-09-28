# 방금그곡

```python
def solution(m, musicinfos):
    dic = {}
    #사용되는 음이 아닌 문자로 변환
    m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    for i in musicinfos:
    	#콤마를 기준으로 변수에 저장
        start, end, title, music = i.split(",")
        #끝난시각-시작시간을 분단위로 저장
        start = [int(i) for i in start.split(":")]
        end = [int(i) for i in end.split(":")]
        
        
        time = (end[0] - start[0]) *60 + (end[1] - start[1])
        music = music.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        #몫, 나머지를 이용해 실제로 재생된 멜로디 저장
        music = music * (time // len(music)) + music[:time % len(music) + 1]
        dic[title] = music
        
    answer = ["", ""]
    for key, value in dic.items():
        if m in value:
            if len(answer[1]) < len(value):
                answer[0] = key
                answer[1] = value
    
    return "(None)" if len(answer[0])==0 else answer[0]
```

