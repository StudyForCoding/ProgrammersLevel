def solution(new_id):
    import re
    import copy
    answer = ''
    answer = new_id.lower()
    answer = re.sub(r"[^-_.a-z0-9]","",answer)
    answer = list(answer)
    prev = '!'
    answer_copy = copy.deepcopy(answer)
    for idx in reversed(range(len(answer_copy))):
      if answer_copy[idx] == prev and prev == '.':
        del answer[idx]
      prev = answer_copy[idx]
    if answer[0] == '.':
      answer = answer[1:]
    if len(answer) >= 1:
      if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) == 0:
      answer += 'a'
    if len(answer) >= 16:
      answer = answer[:15]
      if answer[-1] == '.':
        answer = answer[:-1]
    while(len(answer) <= 2):
      answer += answer[-1]
    answer = ''.join(answer)
    return answer