from typing import TypeVar
import math

SelfPoint = TypeVar("SelfPoint", bound="PointNum")
SelfMyNum = TypeVar("SelfMyNum", bound="MyNum")
SelfEllipticCurve = TypeVar("SelfEllipticCurve", bound="EllipticCurveNum")

def len_number(value: int):
    bit_number = [int(x) for x in bin(value)[2:]]
    return len(bit_number)

class MyNum:
    len = 0
    def __init__(self, arg:int):
        self.num = arg
        self.len = len_number(arg)
    
    def __add__ (self, other: SelfMyNum):
        return MyNum(self.num ^ other.num)

    def __mul__ (self, other: SelfMyNum):
        bit_number = ([int(x) for x in bin(other.num)[2:]])
        bit_number.reverse()
        num = 0
        bit_number_len = len(bit_number)
        for i in range(bit_number_len):
            num = num ^ ((self.num << i) * bit_number[i])
        return MyNum(num)

    def __truediv__ (self, other: SelfMyNum):
        num = self.num + 0
        res_div = 0
        other_bit_num = ([int(x) for x in bin(other.num)[2:]])
        other_len = len(other_bit_num)
        self_bit_num = ([int(x) for x in bin(num)[2:]])
        self_len = len(self_bit_num)
        while (self_len >= other_len):
            num ^= other.num << (self_len - other_len)
            res_div += 1 << (self_len - other_len)
            if(num == 0): break
            self_bit_num = ([int(x) for x in bin(num)[2:]])
            self_len = len(self_bit_num)
        return MyNum(res_div)

    def __mod__(self, other: SelfMyNum):
        num = self.num + 0
        other_bit_num = ([int(x) for x in bin(other.num)[2:]])
        other_len = len(other_bit_num)
        self_bit_num = ([int(x) for x in bin(num)[2:]])
        self_len = len(self_bit_num)
        while (self_len >= other_len):
            num ^= other.num << (self_len - other_len)
            if(num == 0): break
            self_bit_num = ([int(x) for x in bin(num)[2:]])
            self_len = len(self_bit_num)
        return MyNum(num)
    
    def __eq__(self, other: SelfMyNum) -> bool:
        return self.num == other.num

    def __pow__(self, other: int):
        _point = self.copy()
        for i in range(other - 1):
            _point = _point * self
        return _point
    
    def __str__(self) -> str:
        return f"( {self.num} ) \x1b[34mmod \x1b[33m2\x1b[0m"

    def append(self, elem: int = 1) -> None:
        self.num = self.num * 2 * elem
    
    def copy(self):
        return MyNum(self.num)

    # @staticmethod
    # def normalize(value):
    #     for i in range(len(value)):
    #         value[i] = value[i] % 2
    #     while value[0] == 0 and len(value) != 1:
    #         value = np.delete(value, 0, 0)
    #     return value
    @staticmethod
    def from_string(value: str, var: str = 't'):
        list_str = value.split('+')
        num_list = []
        for el in list_str:
            if el == '1': 
                num_list.append(0)
                continue
            if el == 't': 
                num_list.append(1)
                continue
            num_list.append(int(el.split(f'{var}^')[1]))
        num_list.sort()
        element_list = np.zeros(num_list[-1] + 1)
        for el in num_list:
            element_list[el] += 1
        
def true_div(numerator: MyNum, enumerator:MyNum, mod:MyNum) -> MyNum:
    if (enumerator%mod).num == 1: return (numerator%mod)
    k = (true_div((numerator%enumerator), (mod%enumerator), enumerator) * mod)
    return (numerator + k) / enumerator

class PointNum:
    def __init__(self: SelfPoint, x: MyNum, y:MyNum) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point\x1b[31m*\x1b[0m\n   x: \x1b[32m{self.x}\x1b[0m \n   y: \x1b[32m{self.y}\x1b[0m'
    
    def __eq__(self, other: SelfPoint) -> bool:
        if(self.x != other.x): return False
        reversed_y = self.x + self.y
        # if(self.y != other.y and reversed_y != other.y): return False
        return True
    
    def negative(self, f: MyNum = None):
        y = f and (self.x + self.y) % f or self.x + self.y
        return PointNum(self.x, y)
    
    def copy(self):
        return PointNum(self.x, self.y)

class EllipticCurveNum:
    polynomial_table: list[list[MyNum]] = []

    def __init__(self, f:int, m:int) -> None:
        self.f = MyNum(f)
        self.m = m
        # self.get_polynomial_power_table()

    def __str__(self) -> str:
        polytab = ''
        for polynomial in self.polynomial_table:
            polytab += f'  \x1b[32m{polynomial[0]}\x1b[0m = {polynomial[1]}\n'
        if(polytab):
            return f'EllipticCurve\x1b[31m*\x1b[0m\n Polynomial:\n{polytab} \x1b[0m Function: \x1b[32m{self.f}\x1b[0m'
        return f'EllipticCurve\x1b[31m*\x1b[0m\n \x1b[0m Function: \x1b[32m{self.f}\x1b[0m'

    def get_polynomial_power_table(self) -> None:
        for i in range(1, 2 ** self.m):
            polynomial = MyNum(1)
            for j in range(i):
                polynomial.append(0)
            remainder = polynomial % self.f
            self.polynomial_table.append([polynomial, remainder])

    def mod (self, value: MyNum) -> MyNum:
        return value % self.f
    
    def input (self, value: MyNum) -> MyNum:
        return self.mod(value)
    
    def add_elements(self, el1: MyNum, el2: MyNum) -> MyNum:
        el = el1 + el2
        return self.mod(el)

    def mul_elements(self, el1: MyNum, el2: MyNum) -> MyNum:
        el = el1 * el2
        return self.mod(el)

    def pow_elements(self, el: MyNum, power: int) -> MyNum:
        power_el = (el ** abs(power)) % self.f
        if(power > 0): return power_el
        else:
            power_el = self.div_elements(MyNum(1), power_el)
            if(power_el): return power_el
        raise Exception(f'Can`t pow {el} on this elliptic curve (\x1b[32m{self.f}\x1b[0m)')

    def div_elements(self, el1: MyNum, el2: MyNum) -> MyNum:
        return true_div(el1, el2, self.f)

    def trace_of_element(self, el: MyNum) -> MyNum:
        local_el = el.copy()
        for i in range(0, self.m - 1):
            local_el = self.add_elements(self.pow_elements(local_el, 2), el)
        return local_el

    def semitrace_of_element(self, el: MyNum) -> MyNum:
        local_el = el.copy()
        for i in range(0, int((self.m - 1) / 2)):
            local_el = self.add_elements(self.pow_elements(local_el, 4), el)
        return local_el

class EllipticEquation:
    def __init__(self, a:int, b:int, ec :EllipticCurveNum) -> None:
        self.a = MyNum(a)
        self.b = MyNum(b)
        self.ec = ec

    def __str__(self) -> str:
        return f'EllipticEquation\x1b[31m*\x1b[0m\n {self.ec} a: \x1b[32m{self.a}\x1b[0m b: \x1b[32m{self.b}\x1b[0m'

    def add_points(self, point1: PointNum, point2: PointNum) -> PointNum:
        if not (point1 == point2):
            numerator = point1.y + point2.y
            denominator = point1.x + point2.x
            result_of_div = self.ec.div_elements(numerator, denominator)
            copy_rod: MyNum = result_of_div.copy()
            x_full = (copy_rod * copy_rod) + result_of_div + point1.x + point2.x + self.a
            x = self.ec.mod(x_full)
            y_full = (point1.x + x) * result_of_div + x + point1.y
            y = self.ec.mod(y_full)
            return PointNum(x, y)
        
        if point1 == point2:
            if point1.x == MyNum(0) or point1.y == (point2.x + point2.y):
                return PointNum(MyNum(0), MyNum(0))
            else:
                squ_x = self.ec.mod(point1.x**2)
                x = self.ec.mod(self.ec.div_elements(self.b, squ_x) + squ_x)
                copy_y = ((self.ec.div_elements(point1.y, point1.x) + point1.x) * x) + squ_x
                y = self.ec.mod(copy_y + x)
                return PointNum(x, y)
        raise Exception(f'Cant\'t add points')
    
    def mul_number_point (self, k: int, point: PointNum) -> PointNum:
        _point_1 = k >= 0 and point or point.negative( self.ec.f )
        _point_2 = _point_1.copy()
        answer: PointNum = _point_2
        k = abs(k)
        steps = [int(x) for x in bin(k)[2:]]
        steps.reverse()
        pows = []
        for j in range(len(steps)):
            if(steps[j] != 0):
                pows.append(2**j)
        i = 1
        d = 0
        lengthUs = len(pows)
        while d != lengthUs:
            # print("\x1b[33m", d, '\x1b[32m', len(pows))
            if(i in pows):
                print("\x1b[33m", i, '\x1b[32m', d, '\x1b[34m', lengthUs, '\x1b[0m')
                if d < 1: answer = _point_2
                else: answer = self.add_points(answer.copy(), _point_2)
                d += 1
            if d == len(pows): break
            if(i < 1 or i + i > k):
                _point_2 = self.add_points(_point_1, _point_2)
                i += 1
            else:
                _point_2 = self.add_points(_point_2.copy(), _point_2)
                i += i

        return answer

    def define_y(self, x: MyNum or int) -> PointNum:
        if type(x) is int: x = MyNum(x)
        w = self.ec.mod((x**3) + (self.a*(x**2)) + self.b)
        if(x == MyNum(0)):
            y = self.ec.pow_elements(w, (-2))
            return PointNum(x, y)
        elif(w == MyNum(0)):
            y = MyNum(0)
            return PointNum(x, y)
        else:
            s = self.ec.mul_elements(w, self.ec.pow_elements(x, -2))
            tr = self.ec.trace_of_element(s)
            if(tr == MyNum(1)):
                y = MyNum(0)
                return PointNum(x, y)
            else:
                s_tr = self.ec.semitrace_of_element(s)
                y = self.ec.mod(s_tr * x)
                return PointNum(x, y)
        raise Exception(f'Can`t find point by x (\x1b[32m{x}\x1b[0m)')

    def order_of_point (self, point: PointNum) -> int:
        q = 2 ** (len_number(self.ec.f.num) - 1)
        max_point = math.floor(q + 1 + 2 * (q ** 0.5))
        k = math.ceil(max_point ** 0.5)
        table_of_point: list[PointNum] = [point]
        alpha = self.mul_number_point(-k, point)
        gama = alpha.copy()
        for i in range(1, k):
            table_of_point.append(self.mul_number_point(i, point))
        i, j = 1, 0 # can break
        while not(gama in table_of_point): 
            if(i > q): raise Exception(f'Can`t find order of point (\x1b[32m{point}\x1b[0m)')
            i += 1
            gama = self.add_points(alpha, gama)
        for j in range(1, len(table_of_point)):
            if(table_of_point[j] == gama): break
        return k * i + j 
    
    def get_point_by_order(self, order: int) -> list[PointNum]:
        q = 2 ** (self.ec.f.len - 1)
        max_point = math.floor(q + 1 + 2 * (q ** 0.5))
        k = math.ceil(max_point ** 0.5)
        j = order % k
        i = int((order - j) / k)

        res: list[PointNum] = []

        for x in range(1, self.ec.f.num):
            try:
                point = self.define_y(self.ec.input(MyNum(x)))
                k_point = self.mul_number_point(-k, point.copy())
                j_point = self.mul_number_point(j, point.copy())
                i_point = self.mul_number_point(i, k_point.copy())
                if(j_point != i_point): continue
                res.append(point)
            except:
                continue
        return res