### Вычисление времени выполнения функции

#### Для своей функции:

```python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3, n_iter=10000)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate, my_function; integrate(my_function, 1.2, 3, n_iter=100000)" -r 100 -u msec```  

#### Sin(x):

```python -m timeit -s "from main import integrate; from math import(sin, pi); integrate(sin, 0, pi/2)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate; from math import(sin, pi); integrate(sin, 0, pi/2, n_iter=10000)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate; from math import(sin, pi); integrate(sin, 0, pi/2, n_iter=100000)" -r 100 -u msec```  

#### Cos(x):

```python -m timeit -s "from main import integrate; from math import(cos, pi); integrate(cos, 0, pi)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate; from math import(cos, pi); integrate(cos, 0, pi, n_iter=10000)" -r 100 -u msec```  
```python -m timeit -s "from main import integrate; from math import(cos, pi); integrate(cos, 0, pi, n_iter=100000)" -r 100 -u msec```  