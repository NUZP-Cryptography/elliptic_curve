import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

import crypto_ec as ec
from study_log import StudyLog
import math

if __name__ == '__main__':
    log = StudyLog()

    m = 5
    a = ec.Element.from_number(0)
    b = ec.Element.from_string('1+t+t^3+t^4')
    ƒ = ec.Element.from_string('t^5+t^3+1')
    EC5 = ec.EllipticCurve(ƒ, m)
    EE5 = ec.EllipticEquation(a, b, EC5)
    P = ec.Point(ec.Element.from_string('t^3+t'), ec.Element.from_string('t^2+t+1'))

    log.given({"a":a, "b":b, "EC5": EC5, "P": P})
    log.header("Розвʼязок")

    q = 2 ** (EC5.f.len() - 1)
    max_point = math.floor(q + 1 + 2 * (q ** 0.5))
    log.add_point("Обчислимо максимальну оцінку по теоремі Хасе: n = q + 1 + 2√q =", log.green(max_point), f'(q = 2^m = {q})')
    k = math.ceil(max_point ** 0.5)
    log.add_point("Знайдемо коефіцієнт k: k = |√n| =", log.green(k))
    table_of_point: list[ec.Point] = [P]
    alpha = EE5.mul_number_point(-k, P)
    log.add_point("Обчислимо α, α = -kP =", log.green(alpha))
    gama = alpha.copy()

    log.task('Побудуємо таблицю')
    for i in range(1, k):
        table_of_point.append(EE5.mul_number_point(i, P))
        log.add_point(f'{i}P =', table_of_point[i])
    log.end_task()

    log.task("Знайдемо порядок точки")
    log.add_point(f"i = 0, γ = γ + α =", log.green(gama))
    i, j = 1, 0 # can break
    while not(gama in table_of_point): 
        if(i > q): raise Exception(f'Can`t find order of point (\x1b[32m{P}\x1b[0m)')
        gama = EE5.add_points(alpha, gama)
        log.add_point(f"i = {i}, γ = γ + α =", log.green(gama))
        i += 1
    log.end_task()

    for j in range(1, len(table_of_point)):
        if(table_of_point[j] == gama): break
    log.add_point(f"Так як γ = {j}P, то j = ", log.green(j), ", i = ", log.green(i))

    order_of_point = k*i+j
    log.add_point(f"Обчислимо порядок точки: order = k*i + j = ", log.green(order_of_point))

    log.answer({"Порядок точки": order_of_point})

    log.print()

    # print(EE5.define_y(EC5.input(10)))
    # m1 = 7
    # a1 = ec.Element.from_number(1)
    # b1 = ec.Element.from_string('t+1')
    # ƒ1 = ec.Element.from_string('t^7+t^5+t^3+t+1')
    # EC7 = ec.EllipticCurve(ƒ1, m1)
    # EE7 = ec.EllipticEquation(a1, b1, EC7)
    # P1 = ec.Point(ec.Element.from_string('t^4+t^3+1'), ec.Element.from_string('t^4+t^3+t+1'))

    # order = EE7.order_of_point(P1)
    # test = EE7.mul_number_point(33, P1)
    # test_1 = EE7.mul_number_point(-34, P1)
    # print(order)
    # print(test)
    # print(test_1)