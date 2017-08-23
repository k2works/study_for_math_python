## データをグラフで視覚化する

2.1 デカルト座標平面を理解する

2.2 リストとタプルの操作

```python {cmd=true}
import unittest

class TestListTuple(unittest.TestCase):

    def test_01(self):
        simplelist = [1, 2, 3]
        self.assertEqual( simplelist[0], 1)
        self.assertEqual( simplelist[1], 2)
        self.assertEqual( simplelist[2], 3)

    def test_02(self):
        stringlist = ['a string', 'b string', 'c string']
        self.assertEqual( stringlist[0], 'a string')
        self.assertEqual( stringlist[1], 'b string')
        self.assertEqual( stringlist[2], 'c string')

    def test_03(self):
        emptylist = []
        self.assertListEqual( emptylist, [])
        emptylist.append(1)
        self.assertListEqual( emptylist, [1])
        emptylist.append(2)
        self.assertListEqual( emptylist, [1, 2])

    def test_04(self):
        simpletuple = (1, 2, 3)
        self.assertEqual( simpletuple[0], 1)
        self.assertEqual( simpletuple[1], 2)
        self.assertEqual( simpletuple[2], 3)

if __name__ == '__main__':
    unittest.main()
```

2.2.1 リストやタプルで繰り返す

```python {cmd=true}
import unittest

class TestForin(unittest.TestCase):

    def test_01(self):
        l = [1, 2, 3]
        for item in l:
            print(item)
            self.assertIn(item, [1,2,3])

    def test_02(self):
        l = [1, 2, 3]
        for index, item in enumerate(l):
            print(index, item)
            self.assertIn(index, [0, 1, 2])
            self.assertIn(item, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

2.3 matplotlibでグラフを作る

```python {cmd=true matplotlib=true}
from pylab import plot, show
x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]
plot(x_numbers, y_numbers)
show()
```

2.3.1 グラフで点を作る

```python {cmd=true matplotlib=true}
from pylab import plot, show
x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]
plot(x_numbers, y_numbers, marker='o')
show()
```

```python {cmd=true matplotlib=true}
from pylab import plot, show
x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]
plot(x_numbers, y_numbers, 'o')
show()
```

2.3.2 ニューヨーク市の年間平均気温をグラフ化する

```python {cmd=true matplotlib=true}
from pylab import plot, show
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker='o')
show()
```

```python {cmd=true matplotlib=true}
from pylab import plot, show
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker='o')
show()
```

2.3.3 ニューヨーク市の月間気温傾向を比較する

```python {cmd=true matplotlib=true}
from pylab import plot, show
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
show()
```

```python {cmd=true matplotlib=true}
from pylab import plot, show, legend
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([2000, 2006, 2012])
show()
```

2.3.4 グラフのカスタマイズ

2.3.4.1 題名と説明ラベルを追加する

```python {cmd=true matplotlib=true}
from pylab import plot, show, title, xlabel, ylabel, legend
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
title('Average monthly temperature in  NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])
show()
```

2.3.4.2 軸のカスタマイズ

```python {cmd=true matplotlib=true}
from pylab import plot, show, axis
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker='o')
axis(ymin=0)
show()
```

2.3.4.3 pyplotを使ってプロットする

```python {cmd=true matplotlib=tru}
from functions import create_graph
create_graph()
```

2.3.5 プロットの保存

```python {cmd=true matplotlib=true}
from pylab import plot, savefig
x = [1, 2, 3]
y = [2, 4, 6]
plot(x,y)
savefig('mygraph.png')
```

![]('./mygraph.png')

2.4 式をプロットする

2.4.1 ニュートンの万有引力の法則

$F = {Gm_1m_2 \over r^2}$

```python {cmd=true matplotlib=tru}
from functions import generate_F_r
generate_F_r()
```

2.4.2 投射運動

$u_y=u\sin\theta-gt$

$S_y=u(\sin\theta)t - {1 \over2}gt^2$

$t={u \sin\theta \over g}$

$t_{fly} = 2t_{fly} = 2{u\sin\theta \over g}$

```python {cmd=true matplotlib=tru}
from pylab import plot
from functions import draw_trajectory
initial_velocity = 25
angle_of_projection = 60
draw_trajectory(initial_velocity, angle_of_projection)
plt.show()
```

2.4.2.3 異なる初速の軌跡を比較する

```python {cmd=true matplotlib=tru}
from pylab import plot, legend
from functions import draw_trajectory
u_list = [20, 40, 60]
theta = 45
for u in u_list:
    draw_trajectory(u, theta)

# 凡例をつけてグラフを表示
plt.legend(['20','40','60'])
plt.show()
```
