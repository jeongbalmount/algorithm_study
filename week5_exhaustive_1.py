
def solution(answers):
    math_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    biggest_list = []
    biggest_value = 0

    for math_index, m_list in enumerate(math_list):
        count = 0
        for index, answer_number in enumerate(answers):
            math_list_index = index % len(m_list)   # 나머지를 통해 math_list의 원소를 가져오는 부분
            if answer_number is m_list[math_list_index]:
                count += 1

        # 만약 가장 큰수보다 count가 크면 리스트 없애고 넣고 같으면 원래 리스트에 추가
        if biggest_value < count:
            biggest_list = []
            biggest_value = count
            biggest_list.append(math_index + 1)
        elif biggest_value is count:
            biggest_list.append(math_index + 1)

    biggest_list.sort() # 제출하기전 순서 맞추기(오름차순)
    answer = biggest_list
    return answer

