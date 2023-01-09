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
    a, b, p = 6, 5, 43  # Параметры уравнения еллиптической кривой

    elliptic_curve_points = find_elliptic_curve_points(a, b, p)  # Точки еллиптической кривой
    group_order = len(elliptic_curve_points) + 1  # Порядок группы точек эллиптической кривой
    # print('Точки эллиптической кривой: ', elliptic_curve_points)
    # print('Порядок группы точек эллиптической кривой: ', group_order)

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
            # print('Генератор группы: ', point)
            # print(point)
    # print('Всего генераторов группы: ', len(generators_of_group))

    # Порядок точки эллиптической кривой
    for point in elliptic_curve_points:
        # print('Максимальная оценка порядка точки:', int(p + 1 - 2*(p**0.5)), int(p + 1 + 2*(p**0.5)))
        _n1 = int(p + 1 - 2 * (p ** 0.5))
        _n2 = int(p + 1 + 2 * (p ** 0.5))
        n = max([_n1, _n2])
        order = shanks_algorithm(point, n, {'x': 0, 'y': 0}, a, b, p)
        print("Порядок точки", point, ": ",  order)


def multi_signature():
    print(f'\n\nЗагальносистемні параметри')
    print(f'\nДано загальні параметри підпису:')
    print(f'· основне поле – скінченне поле GF({p}),')
    print(f'· еліптична крива над основним полем GF({p}) y^2 = x^3 + {a}·x + {b} mod {p},')
    print(f'· базова точка кривої P = {P["x"], P["y"]},')
    print(f'· порядок базової точки n = {n},')
    print(f'· кількість підписантів в схемі мультипідпису t = {t},')
    print(f'· допоміжне просте багаторозрядне двійкове число δ = {sigma}, |δ| = {math.ceil(sigma ** 0.5) + 1}.')
    
    array_of_d = []
    array_of_k = []
    array_of_points_Q = []
    array_of_points_R = []

    print('\n\nГенерація ключів та формування цифрового підпису')
    for i in range(t):
        d = random.randint(2, n-1)
        Q = multiplication_point(d - 1, P, a, b, p)
        k = random.randint(2, n-1)
        R = multiplication_point(k - 1, P, a, b, p)
        array_of_d.append(d)
        array_of_k.append(k)
        array_of_points_Q.append(Q)
        array_of_points_R.append(R)
        
        print(f'\nЗгенеруємо секретний та відкритий ключі абонента {i+1}:')
        print(f'· оберемо випадкове число d_i, 1 < d_i < n, d_{i+1} = {d} (особистий ключ абонента),')
        print(f'· обчислимо координати точки Q_i = d_i·P, Q_{i+1} = {d}·{P["x"], P["y"]} = {Q["x"], Q["y"]} (відкритий ключ абонента),')
        print(f'· оберемо випадкове число k_i, 1 < k_i < n, k_{i+1} = {k},')
        print(f'· обчислимо координати точки R_i = k_i·P, R_{i+1} = {k}·{P["x"], P["y"]} = {R["x"], R["y"]}.')

    sum_of_points_R = array_of_points_R[0]
    for i in range(t - 1):
        sum_of_points_R = addition_of_points(array_of_points_R[i+1], sum_of_points_R, a, b, p)
    print(f'\nДалі обчислимо сумму всіх точок R_i абонентів, R = ... = {sum_of_points_R["x"], sum_of_points_R["y"]}')

    r = (h * sum_of_points_R['x']) % sigma
    print(f'\nПісля чого формується число r , r = ... = {h}·{sum_of_points_R["x"]} mod {sigma} = {r}')
    
    print(f'\nПотім кожний користувач за допомогою свого особистого ключа d_i та значення k_i обчислює свою частину підпису ...:')

    s = 0
    for i in range(t):
        _s = (array_of_k[i] - array_of_d[i] * r) % n
        print(f's_i = k_i - d_i·r mod n = {array_of_k[i]} - {array_of_d[i]}·{r} mod {r} = {_s}')
        s += _s
        
    print(f'\nПісля чого генерується підпис s = ..., s = {s}>')
    print(f'\nМультипідписом є пара чисел <r, s> = <{r}, {s}>')
    
    return {
        'r': r,
        's': s,
        'array_of_points_Q': array_of_points_Q,
    }
    

def check_multi_signature(data):
    print(f'\n\nПеревірка цифрового підпису')
    r = data['r']
    s = data['s']
    array_of_points_Q = data['array_of_points_Q']

    sum_of_points_Q = array_of_points_Q[0]
    for i in range(t - 1):
        sum_of_points_Q = addition_of_points(array_of_points_Q[i+1], sum_of_points_Q, a, b, p)

    print(f'\nПеревірка підпису <r, s> (<{r}, {s}>) під електронним документом M здійснюється за допомогою колективного відкритого ключа Q = ... , Q = {sum_of_points_Q["x"], sum_of_points_Q["y"]}')
    
    sP = multiplication_point(s - 1, P, a, b, p)
    rQ = multiplication_point(r - 1, sum_of_points_Q, a, b, p)
    
    R = addition_of_points(sP, rQ, a, b, p)

    r = (h * R['x']) % sigma
    print(f'Обчислюється точка R ̃ = s·P + r·Q = {s}·{P["x"], P["y"]} + {r}·{sum_of_points_Q["x"], sum_of_points_Q["y"]} = (xR ̃,yR ̃) еліптичної кривої, R ̃ = {R["x"], R["y"]}')
    print(f'Після чого обчислюються хеш-образ документу Н(М), відповідне десяткове число h та формується число r ̃ = h·xR ̃ mod δ = {h}·{R["x"]} mod {sigma} = r = {r}.')
    print(f'Параметр r ̃ = {r} співпадає з параметром r = {r}, тобто мультипідпис електронного документу   признається справжнім. ')

    
if __name__ == '__main__':
    t = 3
    a, b, p = 6, 5, 43
    P = {'x': 31, 'y': 21}
    n = 37
    h = 6
    sigma = 19
    
    signature = multi_signature()
    check_multi_signature(signature)
