from itertools import permutations


def solution(numbers):
    items = list(numbers)

    # 조합으로 리스트 만듬
    permutation_list = list(map(''.join, permutations(numbers)))

    # 조합 리스트에 numbers 각자 원소 더하기
    permutation_list += items

    before_called = []
    answer = 0
    for item in permutation_list:
        int_item = int(item)    # 문자열 int로 만들기

        is_prime_number = True

        if int_item not in before_called:
            if int_item is 1 or int_item is 0:  # 0과 1 소수 제외
                is_prime_number = False
            before_called.append(int_item)  # 이전에 검사했던 원소는 빼기위한 리스트

            for divide_value in range(2, int_item): # 소수를 판별하는 for 문
                if int_item % divide_value is 0:
                    is_prime_number = False

            if is_prime_number is True:
              answer += 1

        else:
            pass

    return answer

answer = solution("014")
print(answer)
