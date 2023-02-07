import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

import crypto_ec as ec
import crypto_ec_num as ecn
from study_log import StudyLog
import random

if __name__ == '__main__':
    log = StudyLog()

    m = 233
    ƒ =  ec.Element.from_string('t^233+t^9+t^4+t+1').toInt()
    EC5 = ecn.EllipticCurveNum(ƒ, m)
    M_hex = '81145db239c3f973e1ba8cf166ace238d1ab5a90a4280af7b093f48241841e3d'
    m_hash = ecn.MyNum(int(M_hex, base=16))

    a = 1
    b_hex = '06973B15095675534C7CF7E64A21BD54EF5DD3B8A0326AA936ECE454D2C'
    b = int(b_hex, base=16)

    n_hex = '1000000000000000000000000000013E974E72F8A6922031D2603CFE0D7'
    n = int(n_hex, base=16)

    X_hex = '3FCDA526B6CDF83BA1118DF35B3C31761D3545F32728D003EEB25EFE96'
    Y_hex = '9CA8B57A934C54DEEDA9E54A7BBAD95E3B2E91C54D32BE0B9DF96D8D35'
    X = ecn.MyNum(int(X_hex, base=16))
    Y = ecn.MyNum(int(Y_hex, base=16))
    P = ecn.PointNum(X, Y)

    EE5 = ecn.EllipticEquation(a, b, EC5)
    log.given({"a": a, "b": b_hex,  "ƒ": 't^233+t^9+t^4+t+1', "P": P, "Порядок точки": n,})

    log.task("Згенеруємо секретний та відкритий ключі абонента А")
    d = 6
    # d = random.randint(2, n - 2)
    print(d, n)
    log.add_point("Оберемо випадкове число d, 2 ≤ d ≤ n-2:", log.green(d))
    Q = EE5.mul_number_point(-d, P)
    log.add_point("Обчислимо точку Q = -d * P", log.blue(Q))
    log.add_point("Число d є секретним ключем а точка Q є відкритим ключем")

    log.task("Формування цифрового підпису")
    m_hash = EC5.input(m_hash)
    log.add_point("Конвертуємо хеш повідомлення в елемент поля:", log.green(m_hash))
    k = 4
    # k = random.randint(1, n - 1)
    log.add_point("Оберемо випадкове число k, 1 < k ≤ n-1:", log.green(k))
    R = EE5.mul_number_point(k, P)
    log.add_point("Обчислимо точку R = k * P: R =", log.yellow(R))
    y = EC5.mul_elements(m_hash.copy(), R.x)
    log.add_point("Обчислимо елемент поля y = h * Rx: y =", log.green(y))
    r = y % ecn.MyNum(n - 1)
    log.add_point("Молодші n розрядів числа y це r: r =", log.green(r))
    s = (k + (d * r.num)) % n
    log.add_point("Обчислимо значення s = k + d * y: s =", log.green(s))
    log.add_point("Цифровий підпис повідомлення М = <", log.green(y), ',', log.green(s), ">")

    log.task("Перевірка цифрового підпису")
    O = EE5.add_points(EE5.mul_number_point(s, P), EE5.mul_number_point(r.num, Q))
    log.add_point("Обчислимо точку O = s * P + r * Q: O =", log.yellow(O))
    new_y = EC5.mul_elements(m_hash.copy(), O.x)
    log.add_point("Обчислимо елемент поля y = h * Ox: y =", log.green(new_y))
    new_r = new_y % ecn.MyNum(n - 1)
    log.add_point("Молодші n розрядів числа y це r1: r1 =", log.green(new_r))

    # print(r, new_r)

    log.answer({"": f"Ми сформували та перевірили підпис: r = r1 ({log.green(r)} == {log.green(new_r)})"})
    log.print()
