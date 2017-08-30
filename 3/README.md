## データを統計量で記述する

3.1 平均を求める

```python {cmd=true}
import unittest
from functions import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_01(self):
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        mean = calculate_mean(donations)
        N = len(donations)
        self.assertEqual( mean, 477)
        self.assertEqual( N, 12)

if __name__ == '__main__':
    unittest.main()
```

3.2 中央値を求める

```python {cmd=true}
import unittest
from functions import calculate_median

class TestListCalaculateMedian(unittest.TestCase):

    def test_01(self):
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        median = calculate_median(donations)
        N = len(donations)
        self.assertEqual( median, 500)

    def test_02(self):
        donations = [60, 70, 100, 900]
        median = calculate_median(donations)
        N = len(donations)
        self.assertEqual( median, 85)

    def test_03(self):
        donations = [60, 70, 100]
        median = calculate_median(donations)
        N = len(donations)
        self.assertEqual( median, 70)


if __name__ == '__main__':
    unittest.main()
```

3.3 最頻値を求め度数分布表を作る

3.3.1 一番多い要素を見つける

```python {cmd=true}
simplelist = [4, 2, 1, 3, 4]
from collections import Counter
c = Counter(simplelist)
print(c.most_common())
print(c.most_common(1))
print(c.most_common(2))

mode = c.most_common(1)
print(mode)
print(mode[0][0])
```

3.3.2 最頻値を探す

```python {cmd=true}
import unittest
from functions import calculate_mode

class TestListCalaculateMode(unittest.TestCase):

    def test_01(self):
        scores = [7,8,9,2,10,9,9,9,9,4,5,6,15,6,7,8,6,1,10]
        mode = calculate_mode(scores)
        self.assertEqual( mode, 9)

if __name__ == '__main__':
    unittest.main()
```

```python {cmd=true}
import unittest
from functions import calculate_modes

class TestListCalaculateModes(unittest.TestCase):

    def test_01(self):
        scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
        modes = calculate_modes(scores)
        self.assertEqual( modes, [4, 5])

if __name__ == '__main__':
    unittest.main()
```

3.3.3 度数分布表を作る

|点数|頻度|
|-|-|
|1|2|
|2|1|
|4|1|
|5|2|
|6|3|
|7|2|
|8|2|
|9|5|
|10|2|

```python {cmd=true}
from functions import frequency_table

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)
```

```python {cmd=true}
from functions import frequency_sorted_table

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_sorted_table(scores)
```
