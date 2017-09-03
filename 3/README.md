[TOC]

## データを統計量で記述する

### 3.1 平均を求める

```python {cmd=true}
import unittest
from functions import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_01(self):
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        mean = calculate_mean(donations)
        N = len(donations)
        self.assertEqual( mean, 477.75)
        self.assertEqual( N, 12)

if __name__ == '__main__':
    unittest.main()
```

### 3.2 中央値を求める

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

### 3.3 最頻値を求め度数分布表を作る

#### 3.3.1 一番多い要素を見つける

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

#### 3.3.2 最頻値を探す

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
        self.assertEqual( modes, [5, 4])

if __name__ == '__main__':
    unittest.main()
```

#### 3.3.3 度数分布表を作る

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

### 3.4 散らばりを測る

#### 3.4.1 数集合の範囲を求める

```python {cmd=true}
import unittest
from functions import find_range

class TestFindRange(unittest.TestCase):

    def test_01(self):
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        lowest, highest, r = find_range(donations)
        self.assertEqual( lowest, 60)
        self.assertEqual( highest, 1200)
        self.assertEqual( r,1140)

if __name__ == '__main__':
    unittest.main()
```

#### 3.4.2 分散と標準偏差を求める
$\frac{\sum(x_i - x_{avg})^2}{n}$

```python {cmd=true}
import unittest
from functions import calculate_variance

class TestCalculateVariance(unittest.TestCase):

    def test_01(self):
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        variance = calculate_variance(donations)
        self.assertEqual( variance, 141047.35416666666)
        std = variance**0.5
        self.assertEqual( std, 375.5627166887931)

if __name__ == '__main__':
    unittest.main()
```

### 3.5 2つのデータセットの相関を計算する
#### 3.5.1 相関係数を計算する

$\frac{n\sum xy - \sum x\sum y}{\sqrt{n \sum x^2 -(\sum x)^2(n\sum y^2 - (\sum y)^2)}}$

$\sum xy$　2つの数集合$x$と$y$の個別要素の積和
$\sum x$　 集合$x$の数の和
$\sum y$　 集合$y$の数の和
$(\sum x)^2$　集合$x$の数の和の2乗
$(\sum y)^2$　集合$y$の数の和の2乗
$\sum x^2$　 集合$x$の数の和の2乗
$\sum y^2$　 集合$y$の数の和の2乗

```python {cmd=true}
import unittest
from functions import find_corr_x_y

class TestFindCorr(unittest.TestCase):

    def test_01(self):
        x = [1, 2, 3]
        y = [1, 2, 3]
        corr = find_corr_x_y(x,y)
        self.assertEqual( corr, 1)

        x = [1, 2, 3]
        y = [-1, -2, -3]
        corr = find_corr_x_y(x,y)
        self.assertEqual( corr, -1)


        x = [1, 2, 3]
        y = [1, -2, 3]
        corr = find_corr_x_y(x,y)
        self.assertEqual( corr, 0.39735970711951313)

if __name__ == '__main__':
    unittest.main()
```

### 3.6 散布図

```python {cmd=true matplotlib=true}
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

import seaborn as sns
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()
```

#### [アンスコムの４つ組](http://blog.livedoor.jp/oyajieng_memo/archives/1677707.html)

```python {cmd=true matplotlib=true}
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
anscombe=sns.load_dataset("anscombe",engine="python")
sns.lmplot(x="x",y="y",data=anscombe,fit_reg=False)
plt.show()

sns.lmplot(x="x",y="y",data=anscombe,fit_reg=False,hue="dataset",col="dataset",col_wrap=2)
plt.show()
```

### ファイルからデータを読み込む
#### テキストファイルからデータを読み込む

```python {cmd=true}
import unittest
from functions import sum_data

if __name__ == '__main__':
    sum_data('mydata.txt')
```

```python {cmd=true}
import unittest
from functions import read_data
from functions import calculate_mean

class TestReadData(unittest.TestCase):

    def test_01(self):
        data = read_data('mydata.txt')
        mean = calculate_mean(data)
        self.assertEqual( mean, 477.75)

if __name__ == '__main__':
    unittest.main()
```

#### 3.7.2 CSVファイルからデータを読み込む

```python {cmd=true matplotlib=true}
import seaborn as sns
from functions import read_csv
from functions import scatter_plot

if __name__ == '__main__':
    numbers, squared = read_csv('numbers.csv')
    scatter_plot(numbers,squared)
```

https://www.google.com/trends/correlate/
```python {cmd=true  matplotlib=true}
import seaborn as sns
from functions import read_csv2
from functions import find_corr_x_y
from functions import scatter_plot

if __name__ == '__main__':
    summer, highest_correlated = read_csv2('correlate-summer.csv')
    corr = find_corr_x_y(summer, highest_correlated)
    print('Highest correlation: {0}'.format(corr))
    scatter_plot(summer, highest_correlated)
```
