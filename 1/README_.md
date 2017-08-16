## 数を扱う
  
1.1 基本数学演習
  
```python
import unittest
class TestArithmeticOperations(unittest.TestCase):
    def test_additon(self):
        self.assertEqual( 1 + 2, 3)
        self.assertEqual( 1 + 3.5, 4.5)
        self.assertEqual( -1 + 2.5, 1.5)
        self.assertEqual( -1.1 + 5, 3.9)
    def test_subtract(self):
        self.assertEqual( 100 - 45, 55)
    def test_multipliction(self):
        self.assertEqual( 3 * 2, 6)
        self.assertEqual( 3.5 * 1.5, 5.25)
        self.assertEqual( 2 ** 2, 4)
        self.assertEqual( 2 ** 10, 1024)
        self.assertEqual( 1 ** 10, 1)
        self.assertEqual( 8 ** (1/3), 2.0)
    def test_division(self):
        self.assertEqual( 3 / 2, 1.5)
        self.assertEqual( 4 / 2, 2)
        self.assertEqual( 3 // 2, 1)
        self.assertEqual( -3 // 2, -2)
        self.assertEqual( 9 % 2, 1)
    def test_muliti_operation(self):
        self.assertEqual(5 + 5 * 5, 30)
        self.assertEqual((5 + 5) * 5, 50)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
</pre>
  
1.2 ラベル：名前に数を割り当てる
  
```python
import unittest
class TestLabelOperations(unittest.TestCase):
    def test_additon(self):
        a = 3
        self.assertEqual( a + 1, 4)
        a = 5
        self.assertEqual( a + 1, 6)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
</pre>
  
1.3 様々な種類の数
  
```python
import unittest
class TestNumberType(unittest.TestCase):
    def test_int(self):
        assert type(3) is int
        assert type(int(3.8)) is int
        assert type(int(3.0)) is int
    def test_float(self):
        assert type(3.5) is float
        assert type(3.0) is float
        assert type(float(3)) is float
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
</pre>
  
1.3.1 分数を扱う
  
```python
import unittest
from fractions import Fraction
class TestFraction(unittest.TestCase):
    def test_01(self):
        f = Fraction(3, 4)
        self.assertEqual( f, 3/4)
    def test_02(self):
        f = Fraction(3, 4) + 1 + 1.5
        self.assertEqual( f, 3.25)
    def test_03(self):
        f = Fraction(3, 4) + 1 + Fraction(1/4)
        self.assertEqual( f, 2/1)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
</pre>
  
1.3.2 複素数
```python
import unittest
class TestComplexNumber(unittest.TestCase):
    def test_01(self):
        a = 2 + 3j
        assert type(a) is complex
    def test_02(self):
        a = complex(2, 3)
        self.assertEqual( a, 2+3j)
    def test_03(self):
        a = complex(2, 3)
        b = 3 + 3j
        self.assertEqual(a + b, 5+6j)
    def test_04(self):
        a = complex(2, 3)
        b = 3 + 3j
        self.assertEqual(a * b, -3+15j)
        self.assertEqual(a / b, 0.8333333333333334+0.16666666666666666j)
    def test_05(self):
        z = 2 + 3j
        self.assertEqual(z.real, 2.0)
        self.assertEqual(z.imag, 3.0)
        self.assertEqual(z.conjugate(), 2-3j)
        self.assertEqual((z.real ** 2 + z.imag ** 2)**0.5, 3.605551275463989)
        self.assertEqual(abs(z), 3.605551275463989)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
</pre>
  
1.4 ユーザ入力を受け取る
  
```python
a = input()
```
  
1.4.1 例外と不当入力の処理
  
```python
import unittest
from exception import exception
class TestException(unittest.TestCase):
    def test_01(self):
        with self.assertRaises(ValueError):
            exception('Hoge')
    def test_02(self):
        self.assertFalse(1.1.is_integer())
        self.assertTrue(1.0.is_integer())
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
An invalid number
</pre>
  
1.4.2 分数と複素数を入力
```python
import unittest
from exception2 import exception2
from exception3 import exception3
class TestException(unittest.TestCase):
    def test_01(self):
        with self.assertRaises(ZeroDivisionError):
            exception2(3/0)
    def test_02(self):
        with self.assertRaises(ValueError):
            exception3('2 + 3j')
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
</pre>
  
1.5 数学を行うプログラムを書く
1.5.1 整数の因数を計算する
```python
import unittest
from functions import is_factor
from functions import factors
class TestFactor(unittest.TestCase):
    def test_01(self):
        self.assertTrue(is_factor(4,1024))
    def test_02(self):
        self.assertEqual(factors(25),[1,5,25])
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
1
5
25
</pre>
  
1.5.2 乗算表を生成する
```python
import unittest
from functions import multi_table
class TestMultiTable(unittest.TestCase):
    def test_01(self):
        expect = ['5 x 1 = 5',
        '5 x 2 = 10',
        '5 x 3 = 15',
        '5 x 4 = 20',
        '5 x 5 = 25',
        '5 x 6 = 30',
        '5 x 7 = 35',
        '5 x 8 = 40',
        '5 x 9 = 45',
        '5 x 10 = 50']
        self.assertEqual(multi_table(5),expect)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
</pre>
1.5.3 測定単位を変換する
```python
import unittest
from functions import km_miles
from functions import miles_km
class TestUnitConverter(unittest.TestCase):
    def test_01(self):
        self.assertEqual(km_miles(160.9),100)
    def test_02(self):
        self.assertEqual(miles_km(100), 160.9)
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
Distance in miles: 100.0
Distance in kilometers: 160.9
</pre>
1.5.4 2次方程式の解を求める
  
<img src="https://latex.codecogs.com/gif.latex?x_1 = {-b + &#x5C;sqrt{b^2-fac} &#x5C;over 2a}"/>
  
<img src="https://latex.codecogs.com/gif.latex?x_2 = {-b - &#x5C;sqrt{b^2-fac} &#x5C;over 2a}"/>
  
```python
import unittest
from functions import roots
class TestRoots(unittest.TestCase):
    def test_01(self):
        self.assertEqual(roots(1,2,1),(-1.0,-1.0))
    def test_02(self):
        self.assertEqual(roots(1,1,1),(-0.49999999999999994+0.8660254037844386j,-0.5-0.8660254037844386j))
if __name__ == '__main__':
    unittest.main()
```
<pre class="language-text">..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
x1: -1.0
x2: -1.0
x1: (-0.49999999999999994+0.8660254037844386j)
x2: (-0.5-0.8660254037844386j)
</pre>
  