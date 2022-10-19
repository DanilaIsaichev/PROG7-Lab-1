from math import cos, pi, sin


# Написание программы для численного интегрирования площади под кривой.
def integrate(f, a: float, b: float, *, n_iter: int=1000) -> float:

  if b <= a:
    raise ValueError

  # Вычисление шага
  h = (b - a) / n_iter

  # Вычисление суммы значений функции от крайних значений промежутка
  s = f(a) + f(b)

  s1 = integrate_sum(f, a, b - h, 2 * h)

  s2 = integrate_sum(f, a + 2 * h, b - 2 * h, 2 * h)
  
  g = 4 * s1 + 2 * s2

  return format(h/3 * (g + s), ".8f")


def integrate_sum(f, a: float, b: float, h: float) -> float:
    s = 0
    while a <= b:
        s += f(a)
        a += h
    return s


def my_function(x: float) -> float:
  return (2 * x * x + 0.7) ** (1 / 2) / (1.5 + (0.8 * x + 1) ** (1 / 2))


if __name__ == '__main__':
  
  # lambda
  print("---==Custom function==---")
  result = integrate(my_function, 1.2, 3)
  print("Number of iterations:", 1000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3)" -r 100 -u msec 

  result = integrate(my_function, 1.2, 3, n_iter=10000)
  print("Number of iterations:", 10000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3, n_iter=10000)" -r 100 -u msec 

  result = integrate(my_function, 1.2, 3, n_iter=100000)
  print("Number of iterations:", 100000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3, n_iter=100000)" -r 100 -u msec 

  # sin
  print("\n---==sin(x)==---")
  result = integrate(sin, 0, pi/2)
  print("Number of iterations:", 1000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate; from math import sin, pi; integrate(sin, 0, pi/2)" -r 100 -u msec 

  result = integrate(sin, 0, pi/2, n_iter=10000)
  print("Number of iterations:", 10000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate; from math import sin, pi; integrate(sin, 0, pi/2, n_iter=10000)" -r 100 -u msec 

  result = integrate(sin, 0, pi/2, n_iter=100000)
  print("Number of iterations:", 100000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate; from math import sin, pi; integrate(sin, 0, pi/2, n_iter=100000)" -r 100 -u msec 

  # cos
  print("\n---==cos(x)==---")
  result = integrate(cos, 0, pi)
  print("Number of iterations:", 1000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate; from math import cos, pi; integrate(cos, 0, pi)" -r 100 -u msec 

  result = integrate(cos, 0, pi, n_iter=10000)
  print("Number of iterations:", 10000)
  print("Result:", result)
  #python -m timeit -s "from main import integrate; from math import cos, pi; integrate(cos, 0, pi, n_iter=10000)" -r 100 -u msec 

  result = integrate(cos, 0, pi, n_iter=100000)
  print("Number of iterations:", 100000)
  print("Result:", result)
  # python -m timeit -s "from main import integrate; from math import cos, pi; integrate(cos, 0, pi, n_iter=100000)" -r 100 -u msec 
