import numpy as np
from typing import TypeVar
import math

SelfPoint = TypeVar("SelfPoint", bound="Point")
SelfElement = TypeVar("SelfElement", bound="Element")
SelfEllipticCurve = TypeVar("SelfEllipticCurve", bound="EllipticCurve")

class Point:
    def __init__(self: SelfPoint, x: SelfElement, y:SelfElement) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point\x1b[31m*\x1b[0m\n   x: \x1b[32m{self.x}\x1b[0m \n   y: \x1b[32m{self.y}\x1b[0m'
    
    def __eq__(self, other: SelfPoint) -> bool:
        if(self.x != other.x): return False
        reversed_y = self.x + self.y
        if(self.y != other.y and reversed_y != other.y): return False
        return True
    
    def negative(self, f: SelfElement = None) -> SelfPoint:
        y = f and (self.x + self.y) % f or self.x + self.y
        return Point(self.x, y)
    
    def copy(self) -> SelfPoint:
        return Point(self.x.copy(), self.y.copy())

class Element:
    def __init__(self: SelfElement, *args:list[int]) -> SelfElement:
        self.args = Element.normalize(np.array(args))
    
    def __add__ (self, other: SelfElement) -> SelfElement:
        return Element(*Element.normalize(np.polyadd(self.args, other.args)))

    def __mul__ (self, other: SelfElement) -> SelfElement:
        return Element(*Element.normalize(np.polymul(self.args, other.args)))

    def __truediv__ (self, other: SelfElement) -> SelfElement:
        return Element(*Element.normalize(np.polydiv(self.args, other.args)[0]))

    def __mod__(self, other: SelfElement) -> SelfElement:
        return Element(*Element.normalize(np.polydiv(self.args, other.args)[1]))
    
    def __eq__(self, other: SelfElement) -> bool:
        return np.array_equal(self.args, other.args)

    def __pow__(self, other: int):
        _point = self.copy()
        for i in range(other - 1):
            _point = _point * self
        if(other < 0 ): return Element(1) % _point
        return _point
    
    def __str__(self) -> str:
        string = ""
        length = self.len() - 1
        for i in range(0, length + 1):
            if self.args[i] != 0:
                if len(string) != 0:
                    string += ' + '
                if length - i != 0:
                    string += 't'
                else:
                    string += '1'
                if length - i > 1:
                    string += '^' + str(length - i)
            if self.args[i] == 0 and length == 0:
                string = '0'
        return f"( {string} ) \x1b[34mmod \x1b[33m2\x1b[0m"
            
    def len(self) -> int:
        return len(self.args)

    def delete(self, positions: int) -> None:
        self.args = Element.normalize(np.delete(self.args, positions, 0))

    def append(self, elem: SelfElement) -> None:
        self.args = Element.normalize(np.append(self.args, elem.args))
    
    def copy(self) -> SelfElement:
        return Element(*self.args)

    @staticmethod
    def normalize(value):
        for i in range(len(value)):
            value[i] = value[i] % 2
        while value[0] == 0 and len(value) != 1:
            value = np.delete(value, 0, 0)
        return value
    @staticmethod
    def from_number(value: int):
        bit_number = [int(x) for x in bin(value)[2:]]
        return Element(*bit_number)
    @staticmethod
    def from_pow(value: int):
        pow_list = np.zeros(value + 1)
        pow_list[value] = 1
        return Element(*(np.flipud(pow_list)))
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
        return Element(*(np.flipud(element_list)))
        
class EllipticCurve:
    polynomial_table: list[list[Element]] = []

    def __init__(self, f:SelfElement, m:int) -> None:
        self.f = f
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
            polynomial = Element(1)
            for j in range(i):
                polynomial.append(Element(0))
            remainder = polynomial % self.f
            print(i, remainder)
            self.polynomial_table.append([polynomial, remainder])

    def mod (self, value: Element) -> Element:
        return (value % self.f)
    
    def input (self, value: int) -> Element:
        el = Element.from_number(value)
        return self.mod(el)
    
    def add_elements(self, el1: Element, el2: Element) -> Element:
        el = el1 + el2
        return self.mod(el)

    def mul_elements(self, el1: Element, el2: Element) -> Element:
        el = el1 * el2
        return self.mod(el)

    def pow_elements(self, el: Element, power: int) -> Element:
        power_el = (el ** abs(power)) % self.f
        if(power > 0): return power_el
        else:
            power_el = self.div_elements(Element(1), power_el)
            if(power_el): return power_el
        raise Exception(f'Can`t pow {el} on this elliptic curve (\x1b[32m{self.f}\x1b[0m)')

    def div_elements(self, el1: Element, el2: Element) -> Element:
        numerator = el1.copy()
        for i in range(1, 2 ** self.m):
            # print('\x1b[32m', numerator, '\x1b[0m%\x1b[33m', el2, '\x1b[0m=\x1b[31m', numerator % el2, '\x1b[0m')
            if((numerator % el2) == Element(0)): return (numerator / el2) % self.f
            numerator = numerator + (self.f * (Element.from_pow(i) % self.f))

    def trace_of_element(self, el: Element) -> Element:
        local_el = el.copy()
        for i in range(0, self.m - 1):
            local_el = self.add_elements(self.pow_elements(local_el, 2), el)
        return local_el

    def semitrace_of_element(self, el: Element) -> Element:
        local_el = el.copy()
        for i in range(0, int((self.m - 1) / 2)):
            local_el = self.add_elements(self.pow_elements(local_el, 4), el)
        return local_el

class EllipticEquation:
    def __init__(self, a:SelfElement, b:SelfElement, ec :EllipticCurve) -> None:
        self.a = a
        self.b = b
        self.ec = ec

    def __str__(self) -> str:
        return f'EllipticEquation\x1b[31m*\x1b[0m\n {self.ec} a: \x1b[32m{self.a}\x1b[0m b: \x1b[32m{self.b}\x1b[0m'

    def add_points(self, point1: SelfPoint, point2: SelfPoint) -> Point:
        if not (point1 == point2):
            numerator = point1.y.copy() + point2.y.copy()
            denominator = point1.x + point2.x

            result_of_div = self.ec.div_elements(numerator, denominator)

            copy_rod: Element = result_of_div.copy()
            x_full = (copy_rod * copy_rod) + result_of_div + point1.x + point2.x + self.a
            x = self.ec.mod(x_full)
            y_full = (point1.x + x) * result_of_div + x + point1.y
            y = self.ec.mod(y_full)

            return Point(x, y)
        
        if point1 == point2:
            if point1.x == Element(0) or point1.y == (point2.x + point2.y):
                return Point(Element(0), Element(0))
            else:
                squ_x = self.ec.mod(point1.x**2)
                x = self.ec.mod(self.ec.div_elements(self.b, squ_x) + squ_x)
                copy_y = ((self.ec.div_elements(point1.y, point1.x) + point1.x) * x) + squ_x
                y = self.ec.mod(copy_y + x)

                return Point(x, y)
    
    def mul_number_point (self, k: int, point: Point) -> Point:
        _point_1 = k >= 0 and point or point.negative( self.ec.f )
        _point_2 = k >= 0 and point or point.negative( self.ec.f )
        k = abs(k)
        for i in range(k - 1):
            _point_2 = self.add_points(_point_1, _point_2)
        return _point_2

    def define_y(self, x: Element) -> Point:
        w = self.ec.mod((x**3) + (self.a*(x**2)) + self.b)
        if(x == Element.from_number(0)):
            y = self.ec.pow_elements(w, (-2))
            return Point(x, y)
        elif(w == Element.from_number(0)):
            y = Element.from_number(0)
            return Point(x, y)
        else:
            s = self.ec.mul_elements(w, self.ec.pow_elements(x, -2))
            tr = self.ec.trace_of_element(s)
            if(tr == Element.from_number(1)):
                y = Element.from_number(0)
                return Point(x, y)
            else:
                s_tr = self.ec.semitrace_of_element(s)
                y = self.ec.mod(s_tr * x)
                return Point(x, y)
        raise Exception(f'Can`t find point by x (\x1b[32m{x}\x1b[0m)')

    def order_of_point (self, point: Point) -> int:
        q = 2 ** (self.ec.f.len() - 1)
        max_point = math.floor(q + 1 + 2 * (q ** 0.5))
        k = math.ceil(max_point ** 0.5)
        table_of_point: list[Point] = [point]
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