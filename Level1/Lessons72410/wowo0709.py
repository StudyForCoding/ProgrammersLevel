def solution(new_id):
    # Step 1
    new_id = new_id.lower()
    # Step 2
    tmp_id = ''
    for cur in new_id:
        if cur.isalpha() or cur.isdigit() or (cur in ['-','_','.']):
            tmp_id += cur
    # Step 3
    for i in range(len(tmp_id)):
        tmp_id = tmp_id.replace('..','.')
    # Step 4
    tmp_id = tmp_id.strip('.')
    # Step 5
    if not tmp_id: tmp_id = 'a'
    # Step 6
    if len(tmp_id) >= 16: tmp_id = tmp_id[:15]
    tmp_id = tmp_id.rstrip('.')
    # Step 7
    while len(tmp_id) < 3: tmp_id += tmp_id[-1]
    # return
    answer = tmp_id
    return answer