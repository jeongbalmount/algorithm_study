from itertools import permutations


def solution(numbers):
    permutaion_list = []
    for number in numbers:
        permutaion_list.append(str(number))
    # permutation으로 전체 나올수 있는 값 리스트에 집어 넣기
    permu_list = list(permutations(permutaion_list, len(permutaion_list)))

    number_list = []
    for permu in permu_list:
        temp_element = ''
        for var in permu:
            temp_element += var
        # String 형식으로 들어간 값을 int형식으로 바꾸어 리스트에 집어넣기
        number_list.append(int(temp_element))

    sorted_list = sorted(number_list)   # 정렬
    answer = str(sorted_list.pop()) # 가장 큰수 뽑아내기

    return answer


