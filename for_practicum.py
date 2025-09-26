import string

ALL_DIGITS = set(string.digits)


def encrypted_instructions(encrypted_string: str) -> str:
    '''Функция шифрованные инструкции.'''
    # посылка 143213005
    stack: list[tuple] = []
    current_num: str = ''
    current_str: str = ''
    for char in encrypted_string:
        if char in ALL_DIGITS:
            current_num += char
        elif char == '[':
            stack.append((current_str, int(current_num)))
            current_str = ''
            current_num = ''
        elif char == ']':
            prev_str, multiplier = stack.pop()
            current_str = prev_str + current_str * multiplier
        else:
            current_str += char
    return current_str


if __name__ == 'main':
    print(encrypted_instructions(input()))
