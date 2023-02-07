import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

import crypto_ec as ec
import crypto_ec_num as ecn
from study_log import StudyLog
import math

def compare_point(point1: ecn.PointNum, point2: ecn.PointNum):
    if point1.x != point2.x: return False
    if point1.y != point2.y: return False
    return True

if __name__ == '__main__':
    log = StudyLog()

    m = 233
    ƒ =  ec.Element.from_string('t^233+t^9+t^4+t+1').toInt()
    a = 1
    EC5 = ecn.EllipticCurveNum(ƒ, m)

    n_hex = '1000000000000000000000000000013E974E72F8A6922031D2603CFE0D7'
    n = int(n_hex, base=16)

    b_hex = '06973B15095675534C7CF7E64A21BD54EF5DD3B8A0326AA936ECE454D2C'
    b = int(b_hex, base=16)

    X_hex = '3FCDA526B6CDF83BA1118DF35B3C31761D3545F32728D003EEB25EFE96'
    Y_hex = '9CA8B57A934C54DEEDA9E54A7BBAD95E3B2E91C54D32BE0B9DF96D8D35'
    X = 3
    Y = int(Y_hex, base=16)

    EE5 = ecn.EllipticEquation(a, b, EC5)
    log.given({"a": a, "b": b_hex, "n_hex": n_hex, "ƒ": ƒ, "X": X_hex, "Y": Y_hex})

    q = 2 ** (ecn.len_number(ƒ) - 1)
    max_point = math.floor(q + 1 + 2 * (q ** 0.5))
    k = math.ceil(max_point ** 0.5)
    j = n % k
    i = int((n - j) / k)

    log.task(f"Знайти точку з порядком n ({n})")
    zeroPoint = ecn.PointNum(ecn.MyNum(0), ecn.MyNum(0))
    point = zeroPoint.copy()
    n_point = zeroPoint.copy()
    log.add_point("Знайдемо точку чий порядок n =", log.green(n))
    for x in range(1, ƒ):
        point = EE5.define_y(EC5.input(ecn.MyNum(x)))
        log.add_point(f"Знайдемо точку P за відомим x ({x}):", log.yellow(point))
        n_point = EE5.mul_number_point(n, point.copy())
        log.add_point(f"Перевіримо порядок точки P:", log.yellow(n_point), "\n точка має порядок n" if compare_point(n_point, zeroPoint) else "\n точка не має порядок n")
        if compare_point(n_point, zeroPoint): break

    log.task("Перевірити приналежність точки елептичній кривій")
    oldPoint = EE5.define_y(EC5.input(point.x))
    log.add_point("Знайдемо Y за відомим X (", log.green(point.x), f"):{oldPoint.y}")
    log.add_point("Перевіримо рівність наданого Y зі знайденим Y", log.yellow(point.y), '=', log.yellow(oldPoint.y))

    log.answer({"Point": "належить еліптичній кривій" if point.y == oldPoint.y else "не належить цій еліптичній кривій", "Порядок": f"задана еліптична крива має порядок n ({n})" if n_point == zeroPoint else "не відповіда заданому порядку"})
    log.print()
