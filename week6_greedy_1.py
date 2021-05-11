from itertools import combinations


def solution(number, k):
    items = list(number)

    number_tuples = list(combinations(items, k))    # combination으로 k만큼 조합 만들기
    biggest_value_list = list()

    for number_tuple in number_tuples:
        number_list = list(number_tuple)

        temp_list = items[:]    # 얕은 복사 -> 복사한 값이 바뀌어도 원래 값 바뀌지 않음

        # 만든 조합 리스트와 같은 원소 빼기
        for number in number_list:
            for index, temp in enumerate(temp_list):
                if number == temp:
                    temp_list.pop(index)
                    break

        # 만들어진 값 리스트에 집어 넣기
        biggest_value_list.append(int("".join(temp_list)))

    # 리스트에서 가장 큰 값 리턴
    answer = str(max(biggest_value_list))
    return answer

