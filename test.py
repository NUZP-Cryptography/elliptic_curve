import math
import numpy as np

N = 0
polynomial_power_table = []


# # 1 lab Nikita variant (18)
# N = 18
# a = np.array([1])
# b = np.array([1, 0, 0])
# m = 5
# f = np.array([1, 0, 1, 0, 0, 1])

# # 1 lab Vanya variant (6)
# N = 6
# a = np.array([1])
# b = np.array([1, 1, 0])
# m = 3
# f = np.array([1, 1, 0, 1])

# 1 lab Danil variant (14)
# N = 14
# a = np.array([0])
# b = np.array([1, 1, 1])
# m = 3
# f = np.array([1, 1, 0, 1])

# # 1 lab Vadym variant (8)
# N = 8
# a = np.array([0])
# b = np.array([1])
# m = 3
# f = np.array([1, 1, 0, 1])


def normalise_polynomial(polynomial):
    for i in range(len(polynomial)):
        polynomial[i] = polynomial[i] % 2

    while polynomial[0] == 0 and len(polynomial) != 1:
        polynomial = np.delete(polynomial, 0, 0)

    return polynomial


def smart_polydiv(numerator, denumerator):
    global _one

    if np.array_equal(numerator, np.array([0])):
        return np.array([0])
    numerator = normalise_polynomial(np.polydiv(numerator, f)[1])
    denumerator = normalise_polynomial(np.polydiv(denumerator, f)[1])

    while numerator[len(numerator) - 1] == 0 and denumerator[len(denumerator) - 1] == 0:
        if len(numerator) == 1 or len(denumerator) == 1:
            break
        numerator = np.delete(numerator, len(numerator) - 1, 0)
        denumerator = np.delete(denumerator, len(denumerator) - 1, 0)

    for polynomial in polynomial_power_table:
        if np.array_equal(numerator, polynomial[1]):
            numerator = polynomial[0]
        if np.array_equal(denumerator, polynomial[1]):
            denumerator = polynomial[0]

    while numerator[len(numerator) - 1] == 0 and denumerator[len(denumerator) - 1] == 0:
        if len(numerator) == 1 or len(denumerator) == 1:
            break
        numerator = np.delete(numerator, len(numerator) - 1, 0)
        denumerator = np.delete(denumerator, len(denumerator) - 1, 0)

    for polynomial in polynomial_power_table:
        if np.array_equal(np.array([1]), polynomial[1]):
            _one = polynomial[0]

    _result = np.polydiv(np.polymul(numerator, _one), denumerator)[0]
    result = np.polydiv(_result, f)[1]

    return normalise_polynomial(result)


def get_polynomial_power_table():
    for i in range(1, 2 ** m):
        polynomial = [1]
        for j in range(i):
            polynomial.append(0)
        polynomial = np.array(polynomial)
        remainder = np.polydiv(polynomial, f)[1]
        remainder = normalise_polynomial(remainder)
        polynomial_power_table.append([polynomial, remainder])


def get_elliptic_curve_points():

    polynomial_power_table.append([np.array([0]), np.array([0])])

    elliptic_curve_points = []

    for polynomial_x in polynomial_power_table:
        for polynomial_y in polynomial_power_table:
            term_y2 = np.polydiv(np.polymul(polynomial_y[1], polynomial_y[1]), f)[1]
            term_xy = np.polydiv(np.polymul(polynomial_x[1], polynomial_y[1]), f)[1]
            left = np.polyadd(term_y2, term_xy)
            left = normalise_polynomial(left)

            term_x2 = np.polydiv(np.polymul(polynomial_x[1], polynomial_x[1]), f)[1]
            term_x2_a = np.polydiv(np.polymul(term_x2, a), f)[1]
            term_x3 = np.polydiv(np.polymul(term_x2, polynomial_x[1]), f)[1]
            term_x3_x2_a = np.polyadd(term_x3, term_x2_a)
            right = np.polyadd(term_x3_x2_a, b)
            right = normalise_polynomial(right)

            if np.array_equal(left, right):
                elliptic_curve_points.append({'x': polynomial_x[1], 'y': polynomial_y[1]})

    return elliptic_curve_points


def add_elliptic_curve_points(p1, p2):
    x1, y1 = p1['x'], p1['y']
    x2, y2 = p2['x'], p2['y']
    if not np.array_equal(x1, x2):
        numerator = normalise_polynomial(np.polyadd(y1, y2))
        denominator = normalise_polynomial(np.polyadd(x1, x2))

        l = smart_polydiv(numerator, denominator)

        _l = l[:]
        _l2 = normalise_polynomial(np.polydiv(np.polymul(_l, _l), f)[1])
        _l2_l = normalise_polynomial(np.polyadd(_l2, _l))
        _l2_l_x1 = normalise_polynomial(np.polyadd(_l2_l, x1))
        _l2_l_x1_x2 = normalise_polynomial(np.polyadd(_l2_l_x1, x2))
        _l2_l_x1_x2_a = normalise_polynomial(np.polyadd(_l2_l_x1_x2, a))
        x3 = normalise_polynomial(_l2_l_x1_x2_a)

        _x1_x3 = normalise_polynomial(np.polyadd(x1, x3))
        _l_x1_x3 = normalise_polynomial(np.polydiv(np.polymul(_l, _x1_x3), f)[1])
        _l_x1_x3_x3 = normalise_polynomial(np.polyadd(_l_x1_x3, x3))
        _l_x1_x3_x3_y1 = normalise_polynomial(np.polyadd(_l_x1_x3_x3, y1))
        y3 = normalise_polynomial(_l_x1_x3_x3_y1)

        return {'x': x3, 'y': y3}

    if np.array_equal(x1, x2):
        if np.array_equal(x1, np.array([0])) or np.array_equal(y1, normalise_polynomial(np.polyadd(x2, y2))):  # ???
            return {'x': np.array([0]), 'y': np.array([0])}
        else:
            _x12 = np.polydiv(np.polymul(x1, x1), f)[1]
            _b_x12 = smart_polydiv(b, _x12)
            _x12_b_x12 = normalise_polynomial(np.polyadd(_x12, _b_x12))
            x3 = _x12_b_x12

            _y1_x1 = smart_polydiv(y1, x1)
            _x1_y1_x1 = np.polyadd(x1, _y1_x1)
            _x1_y1_x1_x3 = np.polydiv(np.polymul(_x1_y1_x1, x3), f)[1]
            _x12_x1_y1_x1_x3 = np.polyadd(_x12, _x1_y1_x1_x3)
            _x12_x1_y1_x1_x3_x3 = normalise_polynomial(np.polyadd(_x12_x1_y1_x1_x3, x3))
            y3 = _x12_x1_y1_x1_x3_x3

            return {'x': x3, 'y': y3}


def doubling_elliptic_curve_point(k, point):
    _point = point
    for i in range(k - 1):
        _point = add_elliptic_curve_points(point, _point)
    return _point


def get_view_of_polynomial(polynomial):
    view = ''
    for i in range(len(polynomial)):
        if len(polynomial) == 1 and polynomial[0] == 0:
            view += '0' + ' + '
        elif polynomial[i] != 0:
            if str(len(polynomial) - 1 - i) == '0':
                view += '1' + ' + '
            elif str(len(polynomial) - 1 - i) == '1':
                view += 't' + ' + '
            else:
                view += 't^' + str(len(polynomial) - 1 - i) + ' + '
    return view[:-3]


def get_view_of_point(point):
    point_x = get_view_of_polynomial(point['x'])
    point_y = get_view_of_polynomial(point['y'])

    return '(' + point_x + ', ' + point_y + ')'


def elliptic_curves_over_the_extended_field():
    print('\nПараметри')
    print(f'· a = {get_view_of_polynomial(a)},')
    print(f'· b = {get_view_of_polynomial(b)},')
    print(f'· m = {m},')
    print(f'· f = {get_view_of_polynomial(f)},')
    print(f'взяті з таблиці 1 згідно з номером варіанта {N}.')

    print(f'\nДано еліптичну криву над розширеним полем GF(2^{m}):')
    if np.array_equal(a, np.array([0])):
        print(f'y^2 + x·y = x^3 + {get_view_of_polynomial(b)} mod (2, f(t)).')
    else:
        print(f'y^2 + x·y = x^3 + {get_view_of_polynomial(a)}·x^2 + {get_view_of_polynomial(b)} mod (2, {get_view_of_polynomial(f)}).')

    print(f'\nДля виконання операцій в полі GF(2^{m}) скористаємося таблицею степенів многочлена t за модулем f(t) = {get_view_of_polynomial(f)} (розрахунок даних виконаний за допомогою функції get_polynomial_power_table) :')
    get_polynomial_power_table()
    for row in polynomial_power_table:
        top = get_view_of_polynomial(row[0])
        bottom = get_view_of_polynomial(row[1])
        print(top.ljust(3), '=', bottom)

    elliptic_curve_points = get_elliptic_curve_points()
    print(f'\nЕліптична крива містить {len(elliptic_curve_points)} точок (розрахунок даних виконаний за допомогою функції get_elliptic_curve_points):')

    for point in elliptic_curve_points:
        point_order = 1
        p1 = point
        p2 = point
        while not np.array_equal(p2, {'x': np.array([0]), 'y': np.array([0])}):
            p2 = add_elliptic_curve_points(p1, p2)
            point_order += 1
        print(f'{get_view_of_point(point)}, порядок точки {point_order}')

    print('та нескінченно віддалена точка О\n')
    print(f'Отже, порядок єліптичної кривої дорівнює {len(elliptic_curve_points) + 1}.')
    print(f'\nТочки, порядок яких дорівнює порядку єліптичної кривої ({len(elliptic_curve_points) + 1}), є базовими точками.')

#
# - - - - - - - - - - - - - - - - - - - - - - - -
#

# # 2_1 lab Nikita variant (18)
# a = np.array([1])
# b = np.array([1, 0, 0, 0, 1])
# m = 5
# f = np.array([1, 0, 0, 1, 0, 1])
# P = {'x': np.array([1, 0, 0, 0]), 'y': np.array([1, 1, 0])}
# n = 19
# h = np.array([1, 1, 0, 0, 1])
# d = 6
# k = 14

# # 2_1 lab Vanya variant (6)
# a = np.array([1])
# b = np.array([1, 0, 0, 0, 1])
# m = 5
# f = np.array([1, 0, 0, 1, 0, 1])
# P = {'x': np.array([1, 0, 0, 0]), 'y': np.array([1, 1, 0])}
# n = 19
# h = np.array([1, 0, 0, 0])
# d = 4
# k = 8

# # 2_1 lab Danil variant (14)
# a = np.array([1])
# b = np.array([1, 0, 0, 0, 1])
# m = 5
# f = np.array([1, 0, 0, 1, 0, 1])
# P = {'x': np.array([1, 0, 0, 0]), 'y': np.array([1, 1, 0])}
# n = 19
# h = np.array([1, 0, 1, 0, 0])
# d = 12
# k = 3
#
# 2_1 lab Vadym variant (8)
a = np.array([1])
b = np.array([1, 0, 0, 0, 1])
m = 5
f = np.array([1, 0, 0, 1, 0, 1])
n = 19

if __name__ == '__main__':
    elliptic_curves_over_the_extended_field()

