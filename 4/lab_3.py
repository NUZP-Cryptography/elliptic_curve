import math
import random


# Решение квадратного уравнения y^2 = c mod m (возможно работает не правильно)
def solution_of_quadratic_equation(loc_c, loc_m):
    y = None
    if (loc_c ** int((loc_m - 1) / 2)) % loc_m == 1:
        if loc_m % 4 == 3:
            y = (loc_c ** int((loc_m + 1) / 4)) % loc_m
        elif loc_m % 8 == 5:
            if (loc_c ** int((loc_m - 1) / 4)) % loc_m == 1:
                y = (loc_c ** int((loc_m + 3) / 8)) % loc_m
            elif (loc_c ** int((loc_m - 1) / 4)) % loc_m != 1:
                d = 0
                while (d ** int((loc_m - 1) / 2)) % loc_m != loc_m - 1:
                    d += 1
                y = ((loc_c ** int((loc_m + 3) / 8)) * (d ** int((loc_m - 1) / 4))) % loc_m
            else:
                print('!!! error 2')
        else:
            print('!!! huy error 1')

    elif (loc_c ** int((loc_m - 1) / 2)) % loc_m != 1:
        print('no solution')

    return y


# Нахождение точек эллиптической кривой y^2 = x^3 + ax + b mod p в поле GF(p)
def find_elliptic_curve_points(a, b, p):
    elliptic_curve_points = []
    for x in range(p):
        _y = (x ** 3 + a * x + b) % p
        for y in range(0, p):
            if (y ** 2 % p) == _y:
                elliptic_curve_points.append({'x': x, 'y': y})
    return elliptic_curve_points


# Сложение двух точек
def addition_of_points(p1, p2, a, b, p):
    def find_lb(_numerator, _denominator):
        _lb = ((_numerator % p) / (_denominator % p)) % p

        i = 0
        while not _lb.is_integer():
            i += p

            _lb = (((_numerator % p) + i) / (_denominator % p)) % p

        return _lb

    x1 = p1['x']
    y1 = p1['y']
    x2 = p2['x']
    y2 = p2['y']

    if x1 == 0 and y1 == 0:
        return p2

    if x2 == 0 and y2 == 0:
        return p1

    if x1 != x2:
        numerator = y1 - y2
        denominator = x1 - x2
        # print(1, denominator)
        lb = find_lb(numerator, denominator)
        x3 = (lb ** 2 - x1 - x2) % p
        y3 = (lb * (x1 - x3) - y1) % p
        # print('point', {'x': int(x3), 'y': int(y3)})
        return {'x': int(x3), 'y': int(y3)}

    if x1 == x2:
        if y1 % p == 0 or y1 % p == -y2 % p:
            return {'x': 0, 'y': 0}
        else:
            numerator = 3 * (x1 ** 2) + a
            denominator = 2 * y1
            # print(2, denominator)
            lb = find_lb(numerator, denominator)
            x3 = (lb ** 2 - x1 - x2) % p
            y3 = (lb * (x1 - x3) - y1) % p
            return {'x': int(x3), 'y': int(y3)}


# Удвоение точки
def multiplication_point(k, point, a, b, p):
    buff_point = point
    for i in range(k):
        buff_point = addition_of_points(point, buff_point, a, b, p)
    return buff_point


# Алгоритм Шенкса
def shanks_algorithm(P, n, Q,  a, b, p):
    m = math.ceil(n**0.5)
    table_of_points = []
    for i in range(m):
        table_of_points.append(multiplication_point(i, P, a, b, p))

    # print(table_of_points)

    _T = table_of_points[len(table_of_points) - 1]
    T = {'x': _T['x'], 'y': -(_T['y'] - p)}
    S = Q
    for i in range(m - 1):
        # print(m)
        # print("marker", S)
        if S in table_of_points:
            j = table_of_points.index(S)
            d = m*i + j + 1
            break
        else:
            _S = addition_of_points(S, T, a, b, p)
            S = {'x': _S['x'] % p, 'y': _S['y'] % p}
    return d


# Еллиптические кривые над простым полем
def elliptic_curves_over_prime_field():
    a, b, p = 35, 8, 83  # Параметры уравнения еллиптической кривой
    # p1232 = multiplication_point(15, {'x': 4, 'y': 11}, a, b, p)
    # # print(p1232)
    # t = {'x': 64, 'y': 20}
    # t2 = multiplication_point(4, t, a, b, p)
    # print('t', t2)

    elliptic_curve_points = find_elliptic_curve_points(a, b, p)  # Точки еллиптической кривой
    group_order = len(elliptic_curve_points) + 1  # Порядок группы точек эллиптической кривой
    print('Точки эллиптической кривой: ', elliptic_curve_points)
    print('Порядок группы точек эллиптической кривой: ', group_order)

    generators_of_group = []  # Генератор группы точек эллиптической кривой
    for point in elliptic_curve_points:
        _elliptic_curve_points = elliptic_curve_points[:]
        _elliptic_curve_points.remove(point)
        p1 = p3 = point
        for i in range(group_order - 2):
            p3 = addition_of_points(p1, p3, a, b, p)
            if p3 in _elliptic_curve_points:
                _elliptic_curve_points.remove(p3)
            else:
                break
        if len(_elliptic_curve_points) == 0:
            generators_of_group.append(point)
            print('Генератор группы: ', point)
            # print(point)
    print('Всего генераторов группы: ', len(generators_of_group))

    # for point in elliptic_curve_points:
    #     i = 0
    #     while True:
    #         i += 1
    #         if multiplication_point(i, point, a, b, p) == {'x': 0, 'y': 0}:
    #             break
    #     print("Порядок точки", point, ": ",  i + 1)
    # print('- - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    # Порядок точки эллиптической кривой
    for point in elliptic_curve_points:
        # print('Максимальная оценка порядка точки:', int(p + 1 - 2*(p**0.5)), int(p + 1 + 2*(p**0.5)))
        _n1 = int(p + 1 - 2 * (p ** 0.5))
        _n2 = int(p + 1 + 2 * (p ** 0.5))
        n = max([_n1, _n2])
        order = shanks_algorithm(point, n, {'x': 0, 'y': 0}, a, b, p)
        print("Порядок точки", point, ": ",  order)


def ECDH_encryption():
    a, b, p = 35, 8, 83  # Параметры уравнения еллиптической кривой
    P = {'x': 68, 'y': 80}
    n = 37
    print('Базова точка P = ', P)

    c = random.randint(1, n)
    print('Випадкове таємне число "c" абонента А = ', c)
    Q = multiplication_point(c - 1, P, a, b, p)
    print('Точка Q абонента А = ', Q)

    d = random.randint(1, n)
    print('Випадкове таємне число "d" абонента B = ', d)
    R = multiplication_point(d - 1, P, a, b, p)
    print('Точка R абонента B = ', R)

    S = multiplication_point(c - 1, R, a, b, p)
    print('Абонент А, використовуючи отриману точку R абонента B та відкриті параметри, обчислює значення точки S (спільний ключ) = ', S)

    T = multiplication_point(d - 1, Q, a, b, p)
    print('Абонент B, використовуючи отриману точку Q абонента A та відкриті параметри, обчислює значення точки T (спільний ключ) = ', T)
    print('Знайдені абонентами А і В значення та співпадають і утворюють спільний секретний ключ', T)


def ECDH_decryption():
    a, b, p = 35, 8, 83  # Параметры уравнения еллиптической кривой
    P = {'x': 68, 'y': 80}

    Q = {'x': 78, 'y': 17}
    R = {'x': 11, 'y': 8}
    n = 37

    print('Перехоплена точка Q абонента А = ', Q)
    print('Перехоплена точка R абонента B = ', R)

    c = shanks_algorithm(P, n, Q, a, b, p)
    print('Таємне число "с", отримане криптоаналітиком після розв\'язання задачі дискретного логарифмування (за допомогою алгоритма Шенкса): ', c)
    print('Проверка: ', multiplication_point(14, P, a, b, p))
    d = shanks_algorithm(P, n, R, a, b, p)
    print('Таємне число "d", отримане криптоаналітиком після розв\'язання задачі дискретного логарифмування (за допомогою алгоритма Шенкса): ', d)
    S = multiplication_point(c - 1, R, a, b, p)
    print('Отримано спільний секретний ключ абонентів А і B S (S = c*R) :', S)
    T = multiplication_point(d - 1, Q, a, b, p)
    print('Отримано спільний секретний ключ абонентів А і B T (T = d*Q) :', T)


def ECDSA():  # Стандарт цифровой подписи ECDSA (генерация)
    a, b, p = 6, 5, 43  # Параметры уравнения еллиптической кривой
    P = {'x': 42, 'y': 27}  # Базовая точка
    n = 37  # Порядок базовой точки
    h = 30  # Десятичное число после хеширования сообщения
    d = random.randint(2, n - 2)  # Секретный ключ абонента А
    k = random.randint(2, n - 2)  # Случайное число

    Q = multiplication_point(d - 1, P, a, b, p)  # Точка Q

    C = multiplication_point(k - 1, P, a, b, p)  # Точка С
    xC = C['x']  # Координата х точки С
    r = xC % p  # r из пары чисел цифровой подписи
    while r == 0:  # пока r 0 - генерируем новый случайный параметр л и заново вычисляем r
        k = random.randint(2, n - 2)
        C = multiplication_point(k - 1, P, a, b, p)  # Точка С
        xC = C['x']  # Координата х точки С
        r = xC % p  # r из пары чисел цифровой подписи

    s = ((h + d * r) / k) % n  # s из пары чисел цифровой подписи
    i = 0
    while not s.is_integer():  # пока s не является целым числом добавляем n и заново вычисляем s
        i += n
        s = (((h + d * r) + i) / k) % n  # s из пары чисел цифровой подписи

    s = int(s)

    digital_signature = {'r': r, 's': s}  # Цифровая подпись
    print('Базова точка P = ', P)
    print('Відкритим ключем абонента А є точка кривої Q = ', Q)
    print('Секретним ключем абонента А є число d = ', d)
    print('Для формування підпису абонент А хеширує повідомлення M та отримує відповідне десяткове число h = ', h)
    print('Далі абонент А обирає випадкове число k = ', k, 'та обчислює точку C = k*P = ', C)
    print('Звідси число r = Xc mod n = ', r)
    print('З використанням секретного ключа d та числа h абонент А обчислює параметр s = ', s)
    print('Цифровим підписом є пара чисел r та s : ', digital_signature)


def ECDSA_check():  # Стандарт цифровой подписи ECDSA (проверка)
    a, b, p = 35, 8, 83  # Параметры уравнения еллиптической кривой
    P = {'x': 68, 'y': 80}  # Базовая точка
    n = 37  # Порядок базовой точки
    h = 21  # Десятичное число после хеширования сообщения
    Q = {'x': 78, 'y': 17}  # Точка Q
    r = 20  # r из пары чисел цифровой подписи
    s = 11  # s из пары чисел цифровой подписи

    u = (h / s) % n
    i = 0
    while not u.is_integer():
        i += n
        u = ((h + i) / s) % n
    u = int(u)

    v = (r / s) % n
    i = 0
    while not v.is_integer():
        i += n
        v = ((r + i) / s) % n
    v = int(v)

    uP = multiplication_point(u - 1, P, a, b, p)
    vQ = multiplication_point(v - 1, Q, a, b, p)
    point = addition_of_points(uP, vQ, a, b, p)
    _r = point['x'] % n

    print('Базова точка P = ', P)
    print('Відкритим ключем абонента є точка кривої Q = ', Q)
    print('Обчислимо два параметри:')
    print('u = (h/s) mod n = ', u)
    print('v = (r/s) mod n = ', v)
    print('Знайдемо точку еліптичної кривої u*P + v*Q = ', point)
    print('r = r\' =', _r)


if __name__ == '__main__':
    elliptic_curves_over_prime_field()

    # ECDH_encryption()
    # print('------------------------------------')
    ECDH_decryption()

    # ECDSA()
    print('------------------------------------')
    # ECDSA_check()
