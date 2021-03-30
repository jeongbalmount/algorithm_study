

def solution(phone_book):

    # phone_book의 길이 만큰 0이 10개 있는 리스트 만들기
    hash_table = [[0]*10 for _ in range(len(phone_book))]
    first_number_list = []

    # phone_number를 도는 for문
    for index, phone_number in enumerate(phone_book):
        for number_index, number in enumerate(phone_number):
            number = int(number)
            if number_index is 0:
                # 첫번째로 연결리스트에 들어 갔을 경우
                first_number_list.append(number)

                # 첫번째가 아닌 경우
            if hash_table[index][number] is 0:
                ex_list = [number, True]
                hash_table[index][number] = ex_list

    is_no_match_number = True

    # 현재 first_number_list에 부합하는 숫자가 hash_table에 있는지 확인하는 for문
    for first_index, first_number in enumerate(first_number_list):
        for index, number_list in enumerate(hash_table):
            if index is first_index:
                pass
            else:
                if number_list[first_number] is not 0:
                    is_no_match_number = False

    answer = is_no_match_number
    return answer
    # first_number_list각 원소마다 hash_table[][]을 돌면서 같은 값이 있으면 바로 return


