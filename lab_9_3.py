import crypto_ec as ec
from study_log import StudyLog

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
    log.task("Перевірить приналежність точки P")

    left = EC5.mod((P.y**2) + (P.y*P.x))
    log.add_point('Обчислимо ліву частину виразу y^2 + yx =', log.green(left))
    right = EC5.mod((P.x**3) + (a * P.x) + b)
    log.add_point('Обчислимо праву частину виразу y^2 + yx =', log.green(right))
    log.end_task()

    log.add_point(log.green('P'), 'належить заданій елептичній кривій оскільки:', log.green(left), '=', log.green(right))

    log.task("Для точки P обчислить 2P, 3P, 4P, …")
    for i in range(2, 10):
        log.add_point(f'Обчислимо {i}P =', log.green(EE5.mul_number_point(i, P)))
    
    log.print()
    # P_test = ec.Point(ec.Element.from_string('t+1'), ec.Element.from_string('t+1'))
    # ƒ3 = ec.Element.from_string('t^3+t+1')
    # EC3 = ec.EllipticCurve(ƒ3, m)
    # EE3 = ec.EllipticEquation(ec.Element.from_number(1), ec.Element.from_number(1), EC3)
    # c = EE3.add_points(P_test, P_test)
    # c3 = EE3.mul_number_point(3, P_test)
    # c4 = EE3.mul_number_point(4, P_test)
    # c5 = EE3.mul_number_point(5, P_test)
    # print(c)
    # print(c3)
    # print(c4)
    # print(c5)