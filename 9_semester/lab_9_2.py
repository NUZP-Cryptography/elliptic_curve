import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

import crypto_ec as ec
from study_log import StudyLog

if __name__ == '__main__':
    log = StudyLog()
    m = 5
    a = ec.Element.from_number(0)
    b = ec.Element.from_string('1+t+t^3+t^4')
    f = ec.Element.from_string('t^5+t^3+1')

    log.given({"m":m, "a":a, "b":b, "f":f})

    EC5 = ec.EllipticCurve(f, m)

    log.header("Розвʼязок")
    u = x = EC5.input(10)
    log.add_point('Оберемо випадкове число та прирівняємо до х = u =', log.green(u))

    w = EC5.mod((u**3) + (a*(u**2)) + b)
    log.add_point('Виконаємо розрахунок w = u^3 + a*x^2 + b mod (f, 2) =', log.green(w))

    log.task("Розв’язання квадратного рівняння в основному полі")
    if(u == ec.Element.from_number(0)):
        q = y = EC5.pow_elements(w, (-2))
        log.add_point('Так як u = 0, то q = y = w^(-2) =', log.green(q))
        log.answer({"Точка": ec.Point(x, y)})
    elif(w == ec.Element.from_number(0)):
        q = y = ec.Element.from_number(0)
        log.add_point('Так як w = 0, то q = y =', log.green(q))
        log.answer({"Точка": ec.Point(x, y)})
    else:
        s = EC5.mul_elements(w, EC5.pow_elements(x, -2))
        log.add_point('Виконаємо розрахунок s = w * x^2 =', log.green(s))

        tr = EC5.trace_of_element(s)
        log.add_point('Виконаємо розрахунок сліду елемента s: tr = f_tr(s) =', log.green(s))

        if(tr == ec.Element.from_number(1)):
            q = y = ec.Element.from_number(0)
            log.add_point('Так як слід елемента s = 0, то q = y = ', log.green(q))
            log.answer({"Точка": ec.Point(x, y)})
        else:
            s_tr = EC5.semitrace_of_element(s)
            log.add_point('Виконаємо розрахунок напівсліду елемента s: s_tr = f_str(s) =', log.green(s))
    
            q = y = EC5.mod(s_tr * u)
            log.add_point('Обчислимоелемент основного поля q = y = s_tr * u =', log.green(y))
            log.answer({"Точка": ec.Point(x, y)})
    log.print()