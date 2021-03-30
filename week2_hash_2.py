

def solution(participant, completion):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
                'v','w','x','y','z']
    # 해시 테이블을 만든다
    hash_table = [[0] * 1 for _ in range(len(alphabet))]

    # completion 리스트를 해싱하는 부분
    # completion 리스트를 해싱하여 participant와 바교할 해시테이블을 만든다
    for name in completion:
        hash_index = alphabet.index(name[0])
        if hash_table[hash_index][0] is 0:
            hash_table[hash_index][0] = name
        else:
            hash_table[hash_index].append(name)

    no_completion_man = ''
    # 사람이름을 하나씩 빼내어 들어온 사람들 이름과 비교한다.
    for p_name in participant:
        hash_index = alphabet.index(p_name[0])
        is_completion = False
        index = 0
        while is_completion is False and index < len(hash_table[hash_index]):
            # 비교할 이름을 해시 테이블에서 빼낸다.
            compare_name = hash_table[hash_index][index]
            if p_name is compare_name:
                # 비교할 이름이 해시 테이블에 있다면 while문을 끝내 효율성을 올린다.
                inside_index = hash_table[hash_index].index(p_name)
                hash_table[hash_index].pop(inside_index)
                is_completion = True
            index += 1

        if is_completion is False:
            no_completion_man = p_name

    answer = no_completion_man
    return answer

