신규 아이디 추천

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for word in new_id:
        if word.isalpha() or word.isdigit() or word in '-' or word in '.' or word in '_':
            answer += word
    
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer.strip('.')

    if answer == '':
        answer = 'a'
    
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer)<=2:
        answer = answer + answer[-1] * (3-len(answer))
    
    return answer