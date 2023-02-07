import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

from study_log import StudyLog
import math

def euclid(sml, big):
    #When the smaller value is zero, it's done, gcd = b = 0*sml + 1*big.
    if sml == 0:
        return (big, 0, 1)
    else:
        #Repeat with sml and the remainder, big%sml.
        g, y, x = euclid(big % sml, sml)
        #Backtrack through the calculation, rewriting the gcd as we go. From the values just
        #returned above, we have gcd = y*(big%sml) + x*sml, and rewriting big%sml we obtain
        #gcd = y*(big - (big//sml)*sml) + x*sml = (x - (big//sml)*y)*sml + y*big.
        return (g, x - (big//sml)*y, y)

def mult_inv(a, n):	#    return b, for which: a * b ===  1 (mod n), or return tuple with gcd
    g, x, y = euclid(a, n)
    #If gcd(a,n) is not one, then a has no multiplicative inverse.
    if g != 1:
        #raise ValueError('multiplicative inverse does not exist for value a mod n =', a, "mod", n);
        #return str('multiplicative inverse does not exist for value a mod n = ')+str(a)+str(" mod ")+str(n);
        return ("gcd!=1", g);    # if value have no modular inverse - don't show error and just return tuple, with gcd.
    #If gcd(a,n) = 1, and gcd(a,n) = x*a + y*n, x is the multiplicative inverse of a.
    else:
        return x % n

class Point:
    def __init__ (self, x: int, y: int):
        self.x = x
        self.y = y
        self.inf = False

    def __str__(self) -> str:
        return f'Point\x1b[31m*\x1b[0m\n   x: \x1b[32m{self.x}\x1b[0m \n   y: \x1b[32m{self.y}\x1b[0m'

    #Construct the point at infinity.
    @classmethod
    def atInfinity(cls):
        P = cls(0, 0)
        P.inf = True
        return P
    
    def __eq__(self, other):
        if self.inf:
            return other.inf
        elif other.inf:
            return self.inf
        else:
            return self.x == other.x and self.y == other.y
    
    def revers(self, n: int):
        return Point(self.x, n - self.y)
    
    def is_infinite(self):
        return self.inf

class EllipticCurve:
    S = []

    def __init__ (self, a: int, b: int, c: int, ƒ: int):
        self.a, self.b, self.char = a, b, ƒ
        ƒ_copy, step, sum = (ƒ-1), (ƒ-1)//3, 0
        print(ƒ_copy, step)
        while ƒ_copy > 0:
            if ƒ_copy > step:
                ƒ_copy -= step + 1
                first = (sum + 1) if sum > 0 else 0
                self.S.append([first, first + step])
                sum = first + step
            else:
                first = (sum + 1) if sum > 0 else 0
                self.S.append([first, first + ƒ_copy])
                ƒ_copy -= step + 1

    def add(self, P_1: Point, P_2: Point):
        y_diff = (P_2.y - P_1.y) % self.char
        x_diff = (P_2.x - P_1.x) % self.char
        if P_1.is_infinite():
            return P_2
        elif P_2.is_infinite():
            return P_1
        elif x_diff == 0 and y_diff != 0:
            return Point.atInfinity()
        elif x_diff == 0 and y_diff == 0:
            if P_1.y == 0:
                return Point.atInfinity()
            else:
                ld = ((3*P_1.x*P_1.x + 2*self.a*P_1.x + self.b) * mult_inv(2*P_1.y, self.char)) % self.char
        else:
            ld = (y_diff * mult_inv(x_diff, self.char)) % self.char
        nu = (P_1.y - ld*P_1.x) % self.char
        x = (ld*ld - self.a - P_1.x - P_2.x) % self.char
        y = (-ld*x - nu) % self.char
        return Point(x,y)
        
    def double(self, P):
        return self.add(P,P)

    def mult(self, P, k) -> Point:
        if P.is_infinite():
            return P
        elif k == 0:
            return Point.atInfinity()
        else:
            b = bin(k)[2:]
            return self.repeat_additions(P, b, 1)

    def repeat_additions(self, P, b, n) -> Point:
        if b == '0':
            return Point.atInfinity()
        elif b == '1':
            return P
        elif b[-1] == '0':
            return self.repeat_additions(self.double(P), b[:-1], n+1)
        elif b[-1] == '1':
            return self.add(P, self.repeat_additions(self.double(P), b[:-1], n+1))
        return self.add(P, self.repeat_additions(self.double(P), b[:-1], n+1))

    def find_slice(self, z_prev: int):
        s = 0
        for i in range(0, len(self.S)):
            s = i
            if (z_prev >= self.S[i][0] and z_prev <= self.S[i][1]):
                break
        return s

    def a_nex(self, a_prev: int, z_prev: int) -> int:
        s = self.find_slice(z_prev)
        if s == 0:
            return 2 * a_prev
        elif s == 1:
            return a_prev + 1
        else:
            return a_prev

    def b_nex(self, b_prev: int, z_prev: int) -> int:
        s = self.find_slice(z_prev)
        if s == 0:
            return 2 * b_prev
        elif s == 1:
            return b_prev 
        else:
            return b_prev + 1

def ZiZj(Ai: int, Bi: int, Aj: int, Bj: int, n: int):
    numerator = (Aj - Ai)
    denominator = (Bi - Bj)
    while numerator % denominator != 0:
        numerator += n
    d = ((numerator/denominator)) % n
    return d

def Zi_Zj(Ai: int, Bi: int, Aj: int, Bj: int, n: int):
    numerator = (Aj + Ai)
    denominator = (Bi + Bj)
    while numerator % denominator != 0:
        numerator += n
    d = (-(numerator/denominator)) % n
    return d

def ZiP(Ai: int, Bi: int, Aj: int, Bj: int, n:int):
    numerator = (1 -  Ai)
    denominator = (Bi)
    while numerator % denominator != 0:
        numerator += n
    d = ((numerator/denominator)) % n
    return d

def ZiQ(Ai: int, Bi: int, Aj: int, Bj: int, n: int):
    numerator = (Ai)
    denominator = (1 - Bi)
    while numerator % denominator != 0:
        numerator += n
    d = ((numerator/denominator)) % n
    return d

def ZiO(Ai: int, Bi: int, Aj: int, Bj: int, n: int):
    numerator = (Ai)
    denominator = (Bi)
    while numerator % denominator != 0:
        numerator += n
    d = (-(numerator/denominator)) % n
    return d

if __name__ == '__main__':
    log = StudyLog()

    ƒ = 83
    a = 0
    b = 35
    c = 8
    n = 37

    EE = EllipticCurve(a, b, c, ƒ)

    P = Point(61, 58)
    Q = Point(11, 8)
    A = A0 = 1
    B = B0 = 0

    log.given({ "ƒ": f"y^2 = x^3 + 35x + 8 mod 83", "n": n, "P": P, "Q": Q})


    P2 = EE.mult(P, A)
    Q2 = EE.mult(Q, B)
    Z0 = EE.add(P2, Q2)
    # log.add_point("P2", P2)
    # log.add_point("Z0", Z0)
    # print("Z0", Z0)
    # print("Z0", EE.S)
    # print("-----", Point(40, 39) == Point(40, 8))

    ZI = Z0
    array_of_Z = [Z0]
    array_of_A = [A0]
    array_of_B = [B0]

    f = 0
    d = -1
    index = -1

    while d < 0:
        s = EE.find_slice(ZI.x)
        if s == 0:
            A = EE.a_nex(A, ZI.x)
            B = EE.b_nex(B, ZI.x)
            ZI = EE.mult(ZI, 2)
        elif s == 1:
            A = EE.a_nex(A, ZI.x)
            B = EE.b_nex(B, ZI.x)
            ZI = EE.add(ZI, P)
        elif s == 2:
            A = EE.a_nex(A, ZI.x)
            B = EE.b_nex(B, ZI.x)
            ZI = EE.add(ZI, Q)
        for i in range(len(array_of_Z)):
            # print(array_of_Z[i], ZI)
            if ZI == array_of_Z[i]: d = ZiZj(A, B, array_of_A[i], array_of_B[i], n)
            if ZI == array_of_Z[i].revers(n): d = Zi_Zj(A, B, array_of_A[i], array_of_B[i], n)
            if ZI == P: d = ZiP(A, B, array_of_A[i], array_of_B[i], n)
            if ZI == Q: d = ZiQ(A, B, array_of_A[i], array_of_B[i], n)
            if ZI == Point(0, 0): d = ZiO(A, B, array_of_A[i], array_of_B[i], n)
            index = i
            if d >= 0: break

        array_of_Z.append(ZI)
        array_of_A.append(A)
        array_of_B.append(B)

    log.task("Знайдемо Zi та Zj")
    log.add_point("ZI =", ZI)
    log.add_point("Z0 =", array_of_Z[index])
    log.add_point("ZI == Z0 :", ZI == array_of_Z[index])
   
    log.task("Знайдемо Ai, Bi, Aj та Bj")
    log.add_point("A", A)
    log.add_point("B", B)
    log.add_point("A0", array_of_A[index])
    log.add_point("B0", array_of_B[index])

    log.answer({"d": d})

    log.print()
    