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

#### 4.2.3 値に代入する
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

##### 4.2.3.1 級数の値を計算する

```python {cmd=true}
import unittest
from sympy import Symbol
from functions import print_series2

class TestPrintSeries2(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        self.assertEqual(print_series2(5,12),278052/5)

if __name__ == '__main__':
    unittest.main()
```

### 4.2.4 文字列を数式に変換する

#### 4.2.4.1 数式乗算器

```python {cmd=true}
import unittest
from sympy import Symbol
from functions import product

class TestProduct(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        expr1 = x**2 + x*2 + x
        expr2 = x**3 + x*3 + x
        self.assertEqual(product(expr1,expr2),x**5 + 3*x**4 + 4*x**3 + 12*x**2)

    def test_02(self):
        x = Symbol('x')
        y = Symbol('y')
        expr1 = x*y+x
        expr2 = x*x+y
        self.assertEqual(product(expr1,expr2),x**3*y + x**3 + x*y**2 + x*y)

if __name__ == '__main__':
    unittest.main()
```

### 4.3 方程式を解く

```python {cmd=true}
import unittest
from sympy import Symbol, solve

class TestSolve(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        expr = x - 5 - 7
        self.assertEqual(solve(expr),[12])

if __name__ == '__main__':
    unittest.main()
```

#### 4.3.1 ２次方程式を解く
$x^2 + 5^x + 4$
$x^2 + x + 1$
```python {cmd=true}
import unittest
from sympy import Symbol, solve, pprint

class TestSolve(unittest.TestCase):

    def test_01(self):
        x = Symbol('x')
        expr = x**2 + 5*x + 4
        self.assertEqual(solve(expr),[-4,-1])
        self.assertEqual(solve(expr, dict=True),[{x: -4},{x: -1}])

    def test_02(self):
        x = Symbol('x')
        expr = x**2 + x + 1
        pprint(solve(expr, dict=True))

if __name__ == '__main__':
    unittest.main()
```

#### 4.3.2 １変数を他の変数について解く
$s = ut + \frac{1}{2}att$
$t:\frac{1}{a}(-u+\sqrt{2.0as ; u^2})$
$t:-\frac{1}{a}(-u+\sqrt{2.0as ; u^2})$
```python {cmd=true}
from sympy import Symbol, solve, pprint

s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr, t, dict=True)
pprint(t_expr)

```

#### 4.3.3 連立方程式を解く
$2x + 3y = 6$
$3x + 2y = 12$

```python {cmd=true}
from sympy import Symbol, solve, pprint

x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y -12
soln = solve((expr1,expr2), dict=True)
print(soln)
soln = soln[0]
expr1 = expr1.subs({x:soln[x],y:soln[y]})
print(expr1)
expr2 = expr2.subs({x:soln[x],y:soln[y]})
print(expr2)

```

### 4.4 SymPyを使ってプロットする
$y = 2x+3$
```python {cmd=true,matplotlib=true}
from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')
plot(2*x+3)
plot((2*x + 3),(x, -5, 5))
plot(2*x + 3,(x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3')
```

#### 4.4.1 ユーザが入力した式をプロットする
```python
'''
ユーザが入力した式をプロットする
'''
from sympy import Symbol, sympify, solve
from sympy.plotting import plot

def plot_expression(expr):

    y = Symbol('y')
    solutions = solve(expr, y)
    plot(expr_y)

if __name__ =='__main__':
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression
```

### 4.4.2 複数の関数をプロットする
$y=2x+3$
$y=3x+1$
```python {cmd=true,matplotlib=true}
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(2*x+3, 3*x+1)
```

```python {cmd=true,matplotlib=true}
from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x+3, 3*x+1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
```
