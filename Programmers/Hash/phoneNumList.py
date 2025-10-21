def solution(phone_book):
    hash_map={num: True for num in phone_book}

    for number in phone_book:
        prefix=""
        for digit in number[:-1]:
            prefix+=digit
            if prefix in hash_map:
                return False
    return True