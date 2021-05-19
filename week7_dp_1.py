def dp_function(dp_list, index, t_list):
    a_length = len(t_list)

    for a_index, i in enumerate(t_list):
        if a_index == 0:
            dp_list[index][0] = dp_list[index - 1][0] + i
        elif a_index == a_length - 1:
            dp_list[index][a_length - 1] = dp_list[index - 1][a_length - 2] + i
        else:
            if dp_list[index - 1][a_index - 1] >= dp_list[index - 1][a_index]:
                dp_list[index][a_index] = dp_list[index - 1][a_index - 1] + i
            else:
                dp_list[index][a_index] = dp_list[index - 1][a_index] + i
    return dp_list


def solution(triangle):
    length = len(triangle)
    dp_list = []

    for i in range(length):
        temp_list = []
        for j in range(i + 1):
            temp_list.append(0)
        dp_list.append(temp_list)

    for index, t_list in enumerate(triangle):
        if index == 0:
            dp_list[0][0] = t_list[0]
        else:
            dp_list = dp_function(dp_list, index, t_list)

    last_list = dp_list[length - 1]
    answer = max(last_list)
    return answer