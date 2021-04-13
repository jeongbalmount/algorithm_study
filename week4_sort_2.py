

def solution(array, commands):
    answer = []

    for command in commands:
        start = command[0] - 1  # 시작 index
        end = command[1]    # 끝 index
        want_number_index = command[2] - 1  # 찾고자 하는 숫자

        temp_list = array[start:end]
        temp_list = sorted(temp_list)   # 리스트 정렬
        answer.append(temp_list[want_number_index])

    return answer

