def encrypted_instructions(encrypted_string: str) -> str:
    '''Функция шифрованные инструкции.'''
    # посылка 143142428
    stack = []
    current_num = ''
    current_str = ''
    for el in encrypted_string:
        if el.isdigit():
            current_num += el
        elif el == '[':
            stack.append((current_str, int(current_num) if current_num else 1))
            current_str = ''
            current_num = ''
        elif el == ']':
            prev_str, multiplier = stack.pop()
            current_str = prev_str + current_str * multiplier
        else:
            current_str += el        
    return current_str

#if __name__ == 'main':
sipher_str = input()
print(encrypted_instructions(sipher_str))
