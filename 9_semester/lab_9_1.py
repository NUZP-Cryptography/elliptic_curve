import sys
# adding modules from parent directory to the system path
sys.path.append('../crypto')

import crypto_ec as ec

if __name__ == '__main__':
    print("\x1b[33m---Дано\x1b[0m")
    m, f = 5, "t^5+t^3+1"
    EC5 = ec.EllipticCurve(ec.Element.from_string(f), m)
    element = EC5.input(27)
    print("\x1b[32m m=\x1b[0m", m)
    print("\x1b[32m f=\x1b[0m", f)
    print("\x1b[32m EC5=\x1b[0m", EC5)


    print("\x1b[33m---Завдання 1\x1b[0m")
    print(f"\x1b[32mСлід елементу \x1b[35m{element}\x1b[31m:\x1b[0m     ", EC5.trace_of_element(element))
    print(f"\x1b[32mНапівслід елементу \x1b[35m{element}\x1b[31m:\x1b[0m", EC5.semitrace_of_element(element))

    print("\x1b[33m---Завдання 2\x1b[0m")
    EC211 = ec.EllipticCurve(ec.Element.from_string("t^211+t^12+t^6+t+1"), 211)
    print("\x1b[32m EC211=\x1b[0m", EC211)
    print(f"\x1b[32mСлід елементу \x1b[35m{element}\x1b[31m:\x1b[0m     ", EC211.trace_of_element(element))
    print(f"\x1b[32mНапівслід елементу \x1b[35m{element}\x1b[31m:\x1b[0m", EC211.semitrace_of_element(element))
    