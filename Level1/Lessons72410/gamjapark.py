import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^-._a-z0-9]','', new_id)

    while new_id.find('..') != -1:
        new_id = new_id.replace('..','.')

    new_id = new_id.strip('.')
    
    if new_id == "":
        new_id = "a"
        
    new_id = new_id[:15].rstrip('.')
    
    str_len = len(new_id)
    c = new_id[-1]
    if str_len == 1:
        new_id += (c + c)
    elif str_len == 2:
        new_id += c
    return new_id