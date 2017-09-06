[TOC]

## SymPyで代数と式を計算する

### 4.1 式の記号と記号演算を定義する
$2x + 1$
$2xy$
$2x^2$
$(x+2)(y+3)$

```python {cmd=true}
import unittest
from sympy import Symbol
from sympy import symbols

class TestSymPy(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        expect = x + x + 1
        self.assertEqual(expect,2*x + 1)

    def test_02(self):
        a = Symbol('x')
        expect = a + a + 1
        self.assertEqual(expect,2*a + 1)

    def test_03(self):
        x = Symbol('x')
        y = Symbol('y')
        s = x*y + x*y
        self.assertEqual(s,2*x*y)

        x,y = symbols('x,y')
        s = x*y + x*y
        self.assertEqual(s,2*x*y)

    def test_04(self):
        x = Symbol('x')
        y = Symbol('y')
        p = x*(x + x)
        self.assertEqual(p,2*x**2)

        x,y = symbols('x,y')
        p = x*(x + x)
        self.assertEqual(p,2*x**2)

    def test_05(self):
        x = Symbol('x')
        y = Symbol('y')
        p = (x + 2)*(x + 3)
        self.assertEqual(p,(x + 2)*(x + 3))

        x,y = symbols('x,y')
        p = (x + 2)*(x + 3)
        self.assertEqual(p,(x + 2)*(x + 3))


if __name__ == '__main__':
    unittest.main()
```

### 4.2 式を扱う

#### 4.2.1 式の因数分解と展開
$x^2-y^2$ = $(x-y)(x+y)$
$x3 + 3x^2y + 3xy^2 + y^3$ = $(x + y)^3$
$x + y + xy$ = $xy + x + y$

```python {cmd=true}
import unittest
from sympy import Symbol
from sympy import factor, expand

class TestSymPy(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x**2 - y**2
        self.assertEqual(factor(expr),(x-y)*(x+y))

    def test_02(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x**2 - y**2
        factors = factor(expr)
        self.assertEqual(expand(factors),x**2 - y**2)

    def test_03(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
        factors = factor(expr)
        self.assertEqual(factors,(x + y)**3)
        self.assertEqual(expand(factors),x**3 + 3*x**2*y + 3*x*y**2 + y**3)

    def test_04(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x + y + x*y
        self.assertEqual(factor(expr), x*y + x + y)


if __name__ == '__main__':
    unittest.main()
```

#### 4.2.2 プリティプリント
$x^2 + 2xy + y^2$
$2x^2 + 2x + 1$
$1 + 2x + 2x^2$

```python {cmd=true}
from sympy import Symbol
from sympy import pprint
from sympy import init_printing

if __name__ == '__main__':
    x = Symbol('x')
    y = Symbol('y')
    expr = x*x + 2*x*y + y*y
    print(expr)
    pprint(expr, use_unicode=True)
    expr = 1 + 2*x + 2*x**2
    pprint(expr, use_unicode=True)
    init_printing(order='rev-lex')
    pprint(expr, use_unicode=True)
```

##### 4.2.2.1 級数を出力する
$x + \frac{x^2}{2} + \frac{x^3}{3} + \frac{x^4}{4} + ... + \frac{x^n}{n}$

```python {cmd=true}
import unittest
from sympy import Symbol
from functions import print_series

class TestPrintSeries(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        self.assertEqual(print_series(1),x)
        self.assertEqual(print_series(2),x**2/2 + x)
        self.assertEqual(print_series(3),x**3/3 + x**2/2 + x)
        self.assertEqual(print_series(4),x**4/4 + x**3/3 + x**2/2 + x)

if __name__ == '__main__':
    unittest.main()
```

### 4.2.3 値に代入する
$xx + xy + xy + yy$
$x = 1, y = 2$
$9$
$x = y - 1$
$y^2 + 2y(-y + 1)+(-y + 1)^2$
$y^2 - 2y^2 + 2y + y^2 -2y + 1$
$1$

```python {cmd=true}
import unittest
from sympy import Symbol
from sympy import factor, expand, simplify

class TestSymPy(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x*x + x*y + x*y + y*y
        self.assertEqual(expr.subs({x:1, y:2}),9)

    def test_02(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x*x + x*y + x*y + y*y
        self.assertEqual(expr.subs({x:1-y}),y**2 + 2*y*(-y + 1)+(-y + 1)**2)

    def test_03(self):
        x = Symbol('x')
        y = Symbol('y')
        expr = x*x + x*y + x*y + y*y
        expr_subs = expr.subs({x:1-y})
        self.assertEqual(simplify(expr_subs),1)


if __name__ == '__main__':
    unittest.main()
```
