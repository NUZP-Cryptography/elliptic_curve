

def mod_polynomials(s, f):
    _s = s[:]
    _f = f[:]

    while len(_s) > len(f) - 1:
        _t = []

        for i in range(len(_s) - len(f)):
            _f.append(0)

        for i in range(len(_s)):
            _t.append((_s[i] - _f[i]) % 2)

        while _t[0] == 0:
            _t.pop(0)
            if len(_t) == 0:
                break

        _s = _t[:]
    # if len(_s) == 0:
    #     _s = [0]
    return _s


def add_polynomials(term1, term2):
    _term1 = term1[:]
    _term2 = term2[:]

    _term1.reverse()
    _term2.reverse()

    if len(_term1) > len(_term2):
        bigger_term = _term1[:]
        smaller_term = _term2[:]
    else:
        bigger_term = _term2[:]
        smaller_term = _term1[:]

    for i in range(len(smaller_term)):
        bigger_term[i] = (bigger_term[i] + smaller_term[i]) % 2

    bigger_term.reverse()
    # print('bigger_term', bigger_term)
    # if len(bigger_term) != 0:
    while bigger_term[0] == 0:
        bigger_term.pop(0)
        if len(bigger_term) == 0:
            break
    # if len(bigger_term) == 0:
    #     bigger_term = [0]
    return bigger_term


def mult_polynomials(term1, term2):
    _term1 = term1[:]
    _term2 = term2[:]

    _term1.reverse()
    _term2.reverse()

    polynomials_mult = []
    polynomials_mult_length = len(_term1) + len(_term2) - 1

    for i in range(polynomials_mult_length):
        polynomials_mult.append(0)

    for i in range(len(_term1)):
        for j in range(len(_term2)):
            polynomials_mult[i + j] = (polynomials_mult[i + j] + _term1[i] * _term2[j]) % 2

    polynomials_mult.reverse()

    return polynomials_mult


def socrashenie(numerator, denominator):
    _numerator = numerator[:]
    _denominator = denominator[:]

    _numerator.reverse()
    _denominator.reverse()

    while _denominator[0] == 0 and _numerator[0] == 0:
        _numerator.pop(0)
        _denominator.pop(0)

    _numerator.reverse()
    _denominator.reverse()

    return [_numerator, _denominator]


def div_polynomials(numerator, denominator, f):
    res = [5]
    if len(mod_polynomials(numerator, denominator)) != 0:
        res = []
        if len(numerator) >= len(denominator):
            for i in range(len(numerator)):
                if numerator[i] == 1:
                    loc_numerator = [1]
                    for j in range(len(numerator) - i - 1):
                        loc_numerator.append(0)
                    res = add_polynomials(res, div_polynomials(loc_numerator, denominator, f))
        else:
            for i in range(len(numerator)):
                if numerator[i] == 1:
                    loc_numerator = [1]
                    for j in range(len(numerator) - i - 1):
                        loc_numerator.append(0)
                    loc_numerator = add_polynomials(loc_numerator, f)

                    socrashen = socrashenie(loc_numerator, denominator)
                    loc_numerator = socrashen[0]
                    _denominator = socrashen[1]

                    res = add_polynomials(res, div_polynomials(loc_numerator, _denominator, f))
    else:
        res = dumb_div_polynomials(numerator, denominator, f)
    return res


def dumb_div_polynomials(numerator, denominator, f):
    _numerator = numerator[:]
    _denominator = denominator[:]

    # print("Hallo Pidor", len(_numerator), _numerator, len(_denominator), _denominator)
    if len(_numerator) < len(_denominator):

        socrashen = socrashenie(_numerator, _denominator)
        _numerator = socrashen[0]
        _denominator = socrashen[1]

        # print('after', _numerator, _denominator)
        _numerator = add_polynomials(_numerator, f)
        # print('after 2', _numerator, _denominator)
        # print("Hallo", len(_numerator), _numerator, len(_denominator), _denominator)

    result = []
    for i in range(len(_numerator) - len(_denominator) + 1):
        result.append(0)

    j = 0
    while len(_numerator) > len(_denominator) - 1:
        _buff = []
        _denominator_loc = _denominator[:]
        for i in range(len(_numerator) - len(_denominator)):
            _denominator_loc.append(0)

        for i in range(len(_numerator)):
            _buff.append((_numerator[i] + _denominator_loc[i]) % 2)

        result[j] = 1

        while _buff[0] == 0:
            _buff.pop(0)
            j += 1
            if len(_buff) == 0:
                break
        _numerator = _buff[:]
    # print('result', result)
    return result


def pow_polynomials(term1, power):
    term2 = term1
    for p in range(power - 1):
        term2 = mult_polynomials(term1, term2)
    polynomials_pow = term2

    return polynomials_pow


def get_table_of_degrees(a, b, m, f):
    table_of_degrees = []
    for i in range(1, 2 ** m):
        s = [1]
        for j in range(i):
            s.append(0)
        r = mod_polynomials(s, f)
        table_of_degrees.append([s, r])
    return table_of_degrees


def get_elliptic_curve_points(a, b, m, f, table_of_degrees):
    table_of_degrees.append([[0], [0]])
    elliptic_curve_points = []

    for polynomial_x in table_of_degrees:
        for polynomial_y in table_of_degrees:
            term_y2 = mod_polynomials(pow_polynomials(polynomial_y[1], 2), f)
            term_xy = mod_polynomials(mult_polynomials(polynomial_x[1], polynomial_y[1]), f)
            left = add_polynomials(term_y2, term_xy)

            term_x3 = mod_polynomials(pow_polynomials(polynomial_x[1], 3), f)
            term_x2 = mod_polynomials(pow_polynomials(polynomial_x[1], 2), f)
            right = add_polynomials(add_polynomials(term_x3, term_x2), b)

            if left == right:
                elliptic_curve_points.append({'x': polynomial_x[1], 'y': polynomial_y[1]})

    return elliptic_curve_points


def add_curve_points(p1, p2, a, b, m, f, table_of_degrees):
    x1, y1 = p1['x'], p1['y']
    x2, y2 = p2['x'], p2['y']

    if x1 == [0] and y1 == [0]:
        return p2

    if x2 == [0] and y2 == [0]:
        return p1

    if x1 != x2:
        numerator = add_polynomials(y1, y2)
        denominator = add_polynomials(x1, x2)
        if len(numerator) == 0:
            l = [0]
            print('ND', numerator, denominator, y1, y2)
        else:
            l = div_polynomials(numerator, denominator, f)
            while len(l) == 0:
                _numerator = add_polynomials(numerator, f)
                l = div_polynomials(_numerator, denominator, f)

        _l = l[:]
        _l2 = mod_polynomials(pow_polynomials(_l, 2), f)
        _l2_l = add_polynomials(_l2, l)
        _l2_l_x1 = add_polynomials(_l2_l, x1)
        _l2_l_x1_x2 = add_polynomials(_l2_l_x1, x2)
        _l2_l_x1_x2_a = add_polynomials(_l2_l_x1_x2, a)
        x3 = _l2_l_x1_x2_a

        _x1_x3 = add_polynomials(x1, x3)
        _l_x1_x3 = mod_polynomials(mult_polynomials(_l, _x1_x3), f)
        _l_x1_x3_x3 = add_polynomials(_l_x1_x3, x3)
        _l_x1_x3_x3_y1 = add_polynomials(_l_x1_x3_x3, y1)
        y3 = _l_x1_x3_x3_y1
        # print('!=', x3, y3)
        # if len(x3) == 0:
        #     x3 = [0]
        # if len(y3) == 0:
        #     y3 = [0]
        return {'x': x3, 'y': y3}

    if x1 == x2:
        if x1 == [0] or y1 == add_polynomials(x2, y2):
            return {'x': [0], 'y': [0]}
        else:
            _x12 = mod_polynomials(pow_polynomials(x1, 2), f)
            _b_x12 = div_polynomials(b, _x12, f)
            # print("_b_x12", '=', _b_x12, '=' ,b, '/', _x12)
            _x12_b_x12 = add_polynomials(_x12, _b_x12)
            x3 = _x12_b_x12

            # print("niggers", y1, x1)

            _y1_x1 = div_polynomials(y1, x1, f)
            # print("_y1_x1", '=', _y1_x1, '=', y1, '/', x1)
            # print("jsdakfjdciwsde", _y1_x1, y1, x1)
            _x1_y1_x1 = add_polynomials(x1, _y1_x1)
            print("_x1_y1_x1", '=', _x1_y1_x1, '=', x1, '+', _y1_x1)
            _x1_y1_x1_x3 = mod_polynomials(mult_polynomials(_x1_y1_x1, x3), f)
            _x12_x1_y1_x1_x3 = add_polynomials(_x12, _x1_y1_x1_x3)
            _x12_x1_y1_x1_x3_x3 = add_polynomials(_x12_x1_y1_x1_x3, x3)
            y3 = _x12_x1_y1_x1_x3_x3
            # print('==', x3, y3)
            # if len(x3) == 0:
            #     x3 = [0]
            # if len(y3) == 0:
            #     y3 = [0]
            return {'x': x3, 'y': y3}


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
                view += 't' + str(len(polynomial) - 1 - i) + ' + '
    return view[:-3]


def get_view_of_point(point):
    point_x = get_view_of_polynomial(point['x'])
    point_y = get_view_of_polynomial(point['y'])
    return '(' + point_x + ',' + point_y + ')'


def elliptic_curves_over_the_extended_field():
    a, b, m, f = [1], [1, 0], 3, [1, 0, 1, 1]
    # a, b, m, f = 1, [1, 0, 0], 5, [1, 0, 1, 0, 0, 1]

    table_of_degrees = get_table_of_degrees(a, b, m, f)

    elliptic_curve_points = get_elliptic_curve_points(a, b, m, f, table_of_degrees)
    print('\nТочки эллиптической кривой: ')
    for point in elliptic_curve_points:
        print(get_view_of_point(point))

    elliptic_curve_order = len(elliptic_curve_points) + 1
    print('\nПорядок эллиптической кривой: ', elliptic_curve_order)

    print("socrashenie", socrashenie([1, 1, 0], [1, 0]))

    i = 1
    for point in elliptic_curve_points:
        print('- - - - - ', i, point)
        point_order = 1
        p1 = point
        p2 = point
        while p2 != {'x': [0], 'y': [0]}:
            p2 = add_curve_points(p1, p2, a, b, m, f, table_of_degrees)
            point_order += 1
            print('- - -', point_order, p2)
        print('- - - point order', point_order)
        i += 1


    # p1 = {'x': [1], 'y': [1, 0, 0]}
    # p2 = {'x': [1], 'y': [1, 0, 0]}
    # while p2 != {'x': [0], 'y': [0]}:
    #     p2 = add_curve_points(p1, p2, a, b, m, f, table_of_degrees)
    #     print("p2", p2)
    # # print(1, p1)







#
#
#
#
#


if __name__ == '__main__':
    print(mult_polynomials([1, 1], [1, 0, 0, 0, 1, 1]))
    # elliptic_curves_over_the_extended_field()

