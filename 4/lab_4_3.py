from functools import reduce

S_BOX = [
    ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
    ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
    ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
    ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
    ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
    ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
    ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
    ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
    ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
    ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
    ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
    ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
    ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
    ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
    ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
    ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
]

INV_S_BOX = [
    ['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
    ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
    ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
    ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
    ['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
    ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
    ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
    ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
    ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
    ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
    ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
    ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
    ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
    ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
    ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
    ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']
]


def log(msg, matrix):
    print(f'{msg}')
    for row in matrix:
        print(f'   {row[0]} {row[1]} {row[2]} {row[3]} ')


def string_to_unicode_string(string):
    unicode_string = ''
    for char in string:
        unicode_string += hex(ord(char))[2:].upper().zfill(2)

    return unicode_string


def unicode_string_to_matrix(unicode_string):
    state = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            state[j].append(unicode_string[((i*8) + (j*2)):((i*8) + (j*2) + 2)])

    return state


def matrix_to_unicode_string(matrix):
    unicode_string = ''
    for i in range(4):
        for j in range(4):
            unicode_string += (matrix[j][i])

    return unicode_string


def unicode_string_to_string(string):
    ASCII_values = []
    for i in range(int(len(string) / 2)):
        ASCII_values.append(string[i * 2: i * 2 + 2])
    ASCII_string = "".join([chr(int(value, 16)) for value in ASCII_values])

    return ASCII_string


def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            _tmp = int(round_key[i][j], 16) ^ int(state[i][j], 16)
            state[i][j] = hex(_tmp)[2:].upper().zfill(2)

    return state


def byte_sub(state, inverse=False):
    for i in range(4):
        for j in range(4):
            current = state[i][j]
            if not inverse:
                state[i][j] = S_BOX[int(current[0], base=16)][int(current[1], base=16)]
            else:
                state[i][j] = INV_S_BOX[int(current[0], base=16)][int(current[1], base=16)]

    return state


def shift_row(state, inverse=False):
    for i in range(4):
        if inverse:
            state[i].reverse()
        for t in range(i):
            state[i].append(state[i][0])
            state[i].pop(0)
        if inverse:
            state[i].reverse()

    return state


def mix_column(state, inverse=False):
    def mul(p1: int, p2: int):
        """
        Multiplies binary polynomials in Galois field(2 ** 8).
        This corresponds to the `•` operation mentioned in FIPS 197.
        """
        result = 0
        for exp in range(0, p2.bit_length() + 1):
            if p2 & (1 << exp):
                result ^= p1 << exp
        while result.bit_length() > 8:
            result ^= 0b100011011 << (result.bit_length() - 9)

        return result

    if not inverse:
        matrix = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2]
        ]
    else:
        matrix = [
            [14, 11, 13, 9],
            [9, 14, 11, 13],
            [13, 9, 14, 11],
            [11, 13, 9, 14],
        ]

    _state = state[:]

    for i in range(4):
        new_col = []
        col = []
        for c in range(4):
            col.append(_state[c][i])

        for j in range(4):
            terms = (mul(int(x, 16), y) for x, y in zip(col, matrix[j]))
            new_col.append(hex(reduce(lambda a, b: a ^ b, terms))[2:].zfill(2).upper())

        for c in range(4):
            state[c][i] = new_col[c]

    return state


def fips_197_encode(plain_text):
    print(f'\n1. Обрано довільній текст довжиною 16 літер: {plain_text}')

    unicode_string = string_to_unicode_string(plain_text)
    print(f'Кожну літеру заміняємо відповідним шістнадцятирічним ASCII-кодом: {unicode_string}')

    S0 = unicode_string_to_matrix(unicode_string)
    log('Формуємо матрицю - 4 стовпця по 4 шістнадцятирічних числа та отримуємо початковий State S_0:', S0)

    R0 = unicode_string_to_matrix('000102030405060708090A0B0C0D0E0F')
    log('За заданим 128-бітним ключем нульового раунду (R_0 = "000102030405060708090A0B0C0D0E0F") формуємо відповідну State матрицю – 4 стовпця по 4 шістнадцятирічних числа:', R0)

    S1 = add_round_key(S0, R0)
    log('Обчислюємо перетворення додавання раундового ключа AddRoundKey(S_0, R_0). Новий State познаємо S_1:', S1)

    S2 = byte_sub(S1)
    log('2. Обчислюємо перетворення заміна байтів ByteSub(S_1) для кожного елементу State S_1. Новий State познаємо S_2:', S2)

    S3 = shift_row(S2)
    log('3. Обчислюємо перетворення зрушення рядків ShiftRow(S_2) для рядків матриці State S_2. Новий State познаємо S_3:', S3)

    S4 = mix_column(S3)
    log('4. Обчислюємо перетворення MixColumn(S_3) перемішування стовпців матриці State S_3. Новий State познаємо S_4:', S4)

    R1 = unicode_string_to_matrix('D6AA74FDD2AF72FADAA678F1D6AB76FE')
    log('5. За заданим 128-бітним ключем першого раунду (R_1 = "D6AA74FDD2AF72FADAA678F1D6AB76FE") формуємо відповідну State матрицю – 4 стовпця по 4 шістнадцятирічних числа:', R0)

    _S = add_round_key(S4, R1)
    log('Обчислюємо перетворення додавання раундового ключа AddRoundKey(S_4, R_1). Кінцевий State познаємо S`:', _S)

    C = matrix_to_unicode_string(_S)
    print(f'6. Перетворюємо кінцевий внутрішній стан S` на текст: {C}')
    return C


def fips_197_decode(encrypted_unicode_string):
    print('Відомі ключі першого і нульового раундів відповідно R_1 і R_0:')
    print('R_1 = "D6AA74FDD2AF72FADAA678F1D6AB76FE"')
    print('R_0 = "000102030405060708090A0B0C0D0E0F"')

    inv_S = unicode_string_to_matrix(encrypted_unicode_string)
    log('Формуємо матрицю - 4 стовпця по 4 шістнадцятирічних числа та отримуємо початковий State S`:', inv_S)

    print('Знайдємо відкритий текст повідомлення T.')
    print('Для цього:')

    invR1 = unicode_string_to_matrix('D6AA74FDD2AF72FADAA678F1D6AB76FE')
    log('За заданим 128-бітним ключем першого раунду (R_1 = "D6AA74FDD2AF72FADAA678F1D6AB76FE") формуємо відповідну State матрицю – 4 стовпця по 4 шістнадцятирічних числа:', invR1)

    invS4 = add_round_key(inv_S, invR1)
    log('Обчислимо перетворення додавання раундового ключа AddRoundKey(S`, R_1), новий State позначимо S`_4:', invS4)

    invS3 = mix_column(invS4, inverse=True)
    log('Обчислимо зворотне перетворення InvMixColumn(S`_4) – перемішування стовпців матриці State S`_4, новий State позначимо S`_3:', invS3)

    invS2 = shift_row(invS3, inverse=True)
    log('Обчислимо зворотне перетворення зрушення рядків InvShiftRow(S`_3) для рядків матриці State S`_3, новий State позначимо S`_2:', invS2)

    invS1 = byte_sub(invS2, inverse=True)
    log('Обчислимо зворотне перетворення заміна байтів InvByteSub(S`_2) для кожного елементу State S`_2, новий внутрішній стан позначимо S`_1:', invS1)

    invR0 = unicode_string_to_matrix('000102030405060708090A0B0C0D0E0F')
    log('За заданим 128-бітним ключем нульового раунду (R_0 = "000102030405060708090A0B0C0D0E0F") формуємо відповідну State матрицю – 4 стовпця по 4 шістнадцятирічних числа:', invR0)

    invS0 = add_round_key(invS1, invR0)
    log('Обчислимо перетворення додавання раундового ключа AddRoundKey(S`_1, R_0), новий State позначимо S`_0', invS0)

    T = matrix_to_unicode_string(invS0)
    # print(f'{T} - decrypted unicode string')
    print(f'Перетворемо внутрішній стан S`_0 на текст T: {unicode_string_to_string(T)}')


def main():
    # Nikita
    # plain_text = 'hello good world'
    # Danil
    plain_text = 'gachimuchi test '
    # Vanya
    # plain_text = 'cryptography 128'
    # Vadym
    # plain_text = 'lorem ipsum     '

    encrypted_text = fips_197_encode(plain_text)
    print('\nПеревіремо коректність зашифрування обраного тексту:')
    fips_197_decode(encrypted_text)
    # Nikita
    # _C = '3CD28B7174C2D1937E97B8BBEE505F04'
    # Danil
    _C = 'C483C4FAF20E03B6932C861CCCCE60C8'
    # Vanya
    # _C = '718F314FC6124F5BC05CA95C3BE67B24'
    # Vadym
    # _C = '21FBB567F6AFF8C2FC0D6EA3B0D24FAB'

    print(f'\n7. Отримано 128-бітне зашифроване повідомлення {_C}. Після 9-того раунду розшифрування обчислено State S ̄ (згідно з номером варіанту N).')
    fips_197_decode(_C)


if __name__ == "__main__":
    main()
