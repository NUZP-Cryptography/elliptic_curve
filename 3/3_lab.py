import math
import random


# Решение квадратного уравнения y^2 = c mod m (возможно работает не правильно)
def solution_of_quadratic_equation(loc_c, loc_m):
	y = None
	if (loc_c ** int((loc_m - 1) / 2)) % loc_m == 1:
		if loc_m % 4 == 3:
			y = (loc_c ** int((loc_m + 1) / 4)) % loc_m
		elif loc_m % 8 == 5:
			if (loc_c ** int((loc_m - 1) / 4)) % loc_m == 1:
				y = (loc_c ** int((loc_m + 3) / 8)) % loc_m
			elif (loc_c ** int((loc_m - 1) / 4)) % loc_m != 1:
				d = 0
				while (d ** int((loc_m - 1) / 2)) % loc_m != loc_m - 1:
					d += 1
				y = ((loc_c ** int((loc_m + 3) / 8)) * (d ** int((loc_m - 1) / 4))) % loc_m
			else:
				print('!!! error 2')
		else:
			print('!!! huy error 1')
	
	elif (loc_c ** int((loc_m - 1) / 2)) % loc_m != 1:
		print('no solution')
	
	return y


# Нахождение точек эллиптической кривой y^2 = x^3 + ax + b mod p в поле GF(p)
def find_elliptic_curve_points(a, b, p):
	elliptic_curve_points = []
	for x in range(p):
		_y = (x ** 3 + a * x + b) % p
		for y in range(0, p):
			if (y ** 2 % p) == _y:
				elliptic_curve_points.append({'x': x, 'y': y})
	return elliptic_curve_points
	
	
def find(_numerator, _denominator, n):
	_lb = ((_numerator % n) / (_denominator % n)) % n
	
	i = 0
	while not _lb.is_integer():
		i += n
		
		_lb = (((_numerator % n) + i) / (_denominator % n)) % n
	
	return _lb


# Сложение двух точек
def addition_of_points(p1, p2, a, b, p):
	def find_lb(_numerator, _denominator):
		_lb = ((_numerator % p) / (_denominator % p)) % p
		
		i = 0
		while not _lb.is_integer():
			i += p
			
			_lb = (((_numerator % p) + i) / (_denominator % p)) % p
		
		return _lb
	
	x1 = p1['x']
	y1 = p1['y']
	x2 = p2['x']
	y2 = p2['y']
	
	if x1 == 0 and y1 == 0:
		return p2
	
	if x2 == 0 and y2 == 0:
		return p1
	
	if x1 != x2:
		numerator = y1 - y2
		denominator = x1 - x2
		# print(1, denominator)
		lb = find_lb(numerator, denominator)
		x3 = (lb ** 2 - x1 - x2) % p
		y3 = (lb * (x1 - x3) - y1) % p
		# print('point', {'x': int(x3), 'y': int(y3)})
		return {'x': int(x3), 'y': int(y3)}
	
	if x1 == x2:
		if y1 % p == 0 or y1 % p == -y2 % p:
			return {'x': 0, 'y': 0}
		else:
			numerator = 3 * (x1 ** 2) + a
			denominator = 2 * y1
			# print(2, denominator)
			lb = find_lb(numerator, denominator)
			x3 = (lb ** 2 - x1 - x2) % p
			y3 = (lb * (x1 - x3) - y1) % p
			return {'x': int(x3), 'y': int(y3)}


# Удвоение точки
def multiplication_point(k, point, a, b, p):
	buff_point = point
	for i in range(k):
		buff_point = addition_of_points(point, buff_point, a, b, p)
	return buff_point


# Алгоритм Шенкса
def shanks_algorithm(P, n, Q, a, b, p):
	m = math.ceil(n ** 0.5)
	table_of_points = []
	for i in range(m):
		table_of_points.append(multiplication_point(i, P, a, b, p))
	
	# print(table_of_points)
	
	_T = table_of_points[len(table_of_points) - 1]
	T = {'x': _T['x'], 'y': -(_T['y'] - p)}
	S = Q
	for i in range(m - 1):
		# print(m)
		# print("marker", S)
		if S in table_of_points:
			j = table_of_points.index(S)
			d = m * i + j + 1
			break
		else:
			_S = addition_of_points(S, T, a, b, p)
			S = {'x': _S['x'] % p, 'y': _S['y'] % p}
	return d


# Еллиптические кривые над простым полем
def elliptic_curves_over_prime_field():
	a, b, p = 6, 5, 43  # Параметры уравнения еллиптической кривой
	
	elliptic_curve_points = find_elliptic_curve_points(a, b, p)  # Точки еллиптической кривой
	group_order = len(elliptic_curve_points) + 1  # Порядок группы точек эллиптической кривой
	# print('Точки эллиптической кривой: ', elliptic_curve_points)
	# print('Порядок группы точек эллиптической кривой: ', group_order)
	
	generators_of_group = []  # Генератор группы точек эллиптической кривой
	for point in elliptic_curve_points:
		_elliptic_curve_points = elliptic_curve_points[:]
		_elliptic_curve_points.remove(point)
		p1 = p3 = point
		for i in range(group_order - 2):
			p3 = addition_of_points(p1, p3, a, b, p)
			if p3 in _elliptic_curve_points:
				_elliptic_curve_points.remove(p3)
			else:
				break
		if len(_elliptic_curve_points) == 0:
			generators_of_group.append(point)
		# print('Генератор группы: ', point)
		# print(point)
	# print('Всего генераторов группы: ', len(generators_of_group))
	
	# Порядок точки эллиптической кривой
	for point in elliptic_curve_points:
		# print('Максимальная оценка порядка точки:', int(p + 1 - 2*(p**0.5)), int(p + 1 + 2*(p**0.5)))
		_n1 = int(p + 1 - 2 * (p ** 0.5))
		_n2 = int(p + 1 + 2 * (p ** 0.5))
		n = max([_n1, _n2])
		order = shanks_algorithm(point, n, {'x': 0, 'y': 0}, a, b, p)
		print("Порядок точки", point, ": ", order)


def circle_signature():
	print(f'\nОберемо загальні параметри:')
	print(f'основне поле – скінченне поле GF({p}),')
	print(f'еліптична крива над основним полем y^2 = x^3 + {a}·x + {b} mod {p},')
	print(f'базова точка кривої P = {P["x"], P["y"]},')
	print(f'порядок базової точки n = {n}.')
	
	print(f'\nНехай число користувачів в групі дорівнює t = 3: A1, A2, A3.')
	
	array_of_c = []
	array_of_points_U = []
	array_of_d = []
	array_of_points_Q = []
	array_of_k = []
	array_of_S = []
	
	for i in range(t):
		c = random.randint(2, n - 1)
		U = multiplication_point(c - 1, P, a, b, p)
		d = random.randint(2, n - 1)
		Q = multiplication_point(d - 1, P, a, b, p)
		k = random.randint(2, n - 1)
		array_of_c.append(c)
		array_of_points_Q.append(Q)
		array_of_d.append(d)
		array_of_points_U.append(U)
		array_of_k.append(k)

	print(f'\nВідповідними особистими ключами є:')
	for i in range(t):
		print(f'(c{i+1}, d{i+1}) = ({array_of_c[i]}, {array_of_d[i]})')
	
	print(f'\nВідповідними відкритими ключами є:')
	for i in range(t):
		print(f'(U{i + 1}, Q{i + 1}) = ({array_of_points_U[i]["x"], array_of_points_U[i]["y"]}, {array_of_points_Q[i]["x"], array_of_points_Q[i]["y"]})')
	
	signatory = 0  # 0, 1, 2
	print(f'\nНехай підписантові A1 необхідно підписати електронний документ M з хеш-образом H(M) і відповідним йому числом h = {h}.')
	r = random.randint(2, n - 1)
	print(f'\nПідписант A1 обирає одноразові випадкові числа:')
	print(f'r = {r},')
	print(f'k2 = {array_of_k[1]},')
	print(f'k3 = {array_of_k[2]}')
	print(f'та обчислює координати точок S1, S2 та S3:')
	
	for i in range(t):
		if i == signatory:
			left = int(find(1, (h + array_of_c[i] + (array_of_d[i] * r)), n))
			
			hP_2 = multiplication_point(h - 1, P, a, b, p)
			Ui_2 = array_of_points_U[1]
			rQi_2 = multiplication_point(r - 1, array_of_points_Q[1], a, b, p)
			hPUi_2 = addition_of_points(hP_2, Ui_2, a, b, p)
			hPUirQi_2 = addition_of_points(hPUi_2, rQi_2, a, b, p)
			EkhPUirQi_2 = multiplication_point(array_of_k[1] - 1, hPUirQi_2, a, b, p)
			
			hP_3 = multiplication_point(h - 1, P, a, b, p)
			Ui_3 = array_of_points_U[2]
			rQi_3 = multiplication_point(r - 1, array_of_points_Q[2], a, b, p)
			hPUi_3 = addition_of_points(hP_3, Ui_3, a, b, p)
			hPUirQi_3 = addition_of_points(hPUi_3, rQi_3, a, b, p)
			EkhPUirQi_3 = multiplication_point(array_of_k[2] - 1, hPUirQi_3, a, b, p)
			
			EkhPUirQi = addition_of_points(EkhPUirQi_2, EkhPUirQi_3, a, b, p)
			_EkhPUirQi = {'x': EkhPUirQi['x'], 'y': -EkhPUirQi['y'] % p}
			right = addition_of_points(P, _EkhPUirQi, a, b, p)
			
			_S = multiplication_point(left - 1, right, a, b, p)
		else:
			_S = multiplication_point(array_of_k[i] - 1, P, a, b, p)
		array_of_S.append(_S)
	
	print(f'S1 = ... = {array_of_S[0]["x"], array_of_S[0]["y"]}')
	print(f'S2 = k2*P = {array_of_S[1]["x"], array_of_S[1]["y"]}')
	print(f'S3 = k3*P = {array_of_S[2]["x"], array_of_S[2]["y"]}')
	print(f'\nКільцевим підписом є набір <r, S1, S2, S3> = <{r}, {array_of_S[0]["x"], array_of_S[0]["y"]}, {array_of_S[1]["x"], array_of_S[1]["y"]}, {array_of_S[2]["x"], array_of_S[2]["y"]}>')


if __name__ == '__main__':
	t = 3
	a, b, p = -3, 0, 2383
	P = {'x': 81, 'y': 787}
	n = 149
	h = 68
	
	circle_signature()
