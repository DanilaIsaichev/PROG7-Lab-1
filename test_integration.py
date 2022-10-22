import unittest

from main import integrate, my_function


class TestStringMethods(unittest.TestCase):
  def test_precision_1(self):
    self.assertAlmostEqual(float(integrate(my_function, 1.2, 3)), 1.763677931866679, delta=0.01)


  def test_precision_2(self):
    self.assertAlmostEqual(float(integrate(my_function, 1.2, 3, n_iter=10000)), 1.763677931866679, delta=0.001)


  def test_precision_3(self):
    self.assertAlmostEqual(float(integrate(my_function, 1.2, 3, n_iter=1000000)), 1.763677931866679, delta=0.0001)


  def test_precision_4(self):
    self.assertAlmostEqual(float(integrate(my_function, 1.2, 3, n_iter=10000000)), 1.763677931866679, delta=0.00001)


  def test_zero(self):
    with self.assertRaises(ValueError):
      integrate(lambda x: x + 1, 0, 0)


if __name__ == '__main__':
    unittest.main()
