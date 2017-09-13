[TOC]

## 集合と確率を操作する
### 5.1 集合とは何か
#### 5.1.1 集合の構成

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(2, 4, 6)
print(s)
```

```python {cmd=true}
from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1, 1.5, Fraction(1, 5))
print(s)
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 1.5, 3)
print(len(s))
```

##### 5.1.1.1 ある数が集合にあるかどうかチェックする
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 1.5, 3)
print(4 in s)
```

##### 5.1.1.2 空集合を作る
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet()
print(s)
```

##### 5.1.1.3 リストやタプルから集合を作る
```python {cmd=true}
from sympy import FiniteSet
members = [1, 2, 3]
s = FiniteSet(*members)
print(s)
```

##### 5.1.1.4 集合要素の重複と順序
```python {cmd=true}
from sympy import FiniteSet
members = [1, 2, 3, 2]
s = FiniteSet(*members)
print(s)
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
for member in s:
    print(member)
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(3, 4, 5)
t = FiniteSet(5, 4, 3)
print(s == t)
```

#### 5.1.2 部分集合、上位集合、べき集合
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1)
t = FiniteSet(1,2)
print(s.is_subset(t))
print(t.is_subset(s))
print(s.is_subset(s))
print(t.is_subset(t))

print(s.is_superset(t))
print(t.is_superset(s))
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
ps = s.powerset()
print(ps)
print(len(ps))
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
t = FiniteSet(1, 2, 3)
print(s.is_proper_subset(t))
print(t.is_proper_subset(s))

t = FiniteSet(1, 2, 3, 4)
print(s.is_proper_subset(t))
print(t.is_proper_subset(s))
```

#### 5.1.3 集合演算
##### 5.1.3.1 和と積

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
print(s.union(t))
```

$\{1, 2\}\cup\{2, 3\}$
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2)
t = FiniteSet(2, 3)
print(s.intersect(t))
```

$\{1, 2, 3\}\cup\{2, 4, 6\}\cup\{3, 5, 7\}$
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
u = FiniteSet(3, 5, 7)
print(s.union(t).union(u))
```

$\{1, 2, 3\}\cap\{2, 4, 6\}\cap\{3, 5, 7\}$
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
u = FiniteSet(3, 5, 7)
print(s.intersect(t).intersect(u))
```

##### 5.1.3.2 直積

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2)
t = FiniteSet(3, 4)
p = s*t
print(p)
for elem in p:
    print(elem)
```

```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2)
p = s**3
print(p)
for elem in p:
    print(elem)
```

##### 5.1.3.3 変数を複数集合に公式を適用する
$T = 2\pi \sqrt{\frac{L}{g}}$


```python {cmd=true}
from sympy import FiniteSet, pi
def time_period(length):
    g = 9.8
    T = 2*pi*(length/g)**0.5
    return T

if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25)
    for l in L:
        t = time_period(l/100)
        print('Length: {0} cm Time Period: {1:.3f} s'.format(float(l),float(t)))
```

##### 5.1.3.4 異なる重力、異なる結果

```python {cmd=true}
from sympy import FiniteSet, pi
def time_period(length, g):
    g = 9.8
    T = 2*pi*(length/g)**0.5
    return T

if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)','Gravity(m/s^2)', 'Time Period(s)'))
    for elem in L*g_values:
        l = elem[0]
        g = elem[1]
        t = time_period(1/100, g)

        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l),float(g),float(t)))
```

### 5.2 確率
$P(E)=\frac{n(E)}{n(S)}$
$n(E)=8$かつ$n(S)=20$
```python {cmd=true}
from sympy import FiniteSet

def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    space = FiniteSet(*range(1, 21))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)

    print('Sample space: {0}'.format(space))
    print('Event: {0}'.format(event))
    print('Probability of rolling a prime: {0:.5f}'.format(p))
```

#### 5.2.1 事象Aまたは事象Bの確率
$E = \{2, 3, 5\} \cup \{1, 3, 5 \} = \{ 1, 2, 3, 5\}$
$P(E) = \frac{n(E)}{n(S)}=\frac{4}{6}=\frac{2}{3}$
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.union(b)
print(len(e)/len(s))
```

#### 5.2.2 事象Aおよび事象Bの確率
$E = A \cap B = \{2, 3, 5\} \cup \{1, 3, 5\} = \{3, 5\}$
```python {cmd=true}
from sympy import FiniteSet
s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.intersect(b)
print(len(e)/len(s))
```

#### 5.2.3 乱数生成
##### 5.2.3.1 サイコロ投げをシミュレーションする
```python {cmd=true}
import random
for i in range(0, 10):
    print(random.randint(1, 6))
```

##### 5.2.3.2 その目を出せますか
```python {cmd=true}
'''
総和が２０になるまでサイコロをふる
'''
import matplotlib.pyplot as plt
import random

target_score = 20

def roll():
    return random.randint(1, 6)

if __name__ == '__main__':
    score = 0
    num_rolls = 0
    while score < target_score:
        die_roll = roll()
        num_rolls += 1
        print('Rolled: {0}'.format(die_roll))
        score += die_roll

    print('Score of {0} reached in {1} rolls'.format(score, num_rolls))
```

##### 5.2.3.3 目標点数は可能か
```python {cmd=true}
from sympy import FiniteSet
import random

def find_prob(targe_score, max_rolls):

    die_sides = FiniteSet(1, 2, 3, 4, 5, 6)
    # 標本空間
    s = die_sides**max_rolls
    # Find the event set
    if max_rolls > 1:
        success_rolls = []
        for elem in s:
            if sum(elem) >= targe_score:
                success_rolls.append(elem)
    else:
        if target_score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in die_sides:
                if roll >= target_score:
                    success_rolls.append(roll)
    e = FiniteSet(*success_rolls)
    # 目標点数に達する確率の計算
    return len(e)/len(s)

if __name__ == '__main__':

    target_score = 25
    max_rolls = 4
    p = find_prob(target_score, max_rolls)
    print('Probability: {0:.5f}'.format(p))

    target_score = 25
    max_rolls = 5
    p = find_prob(target_score, max_rolls)
    print('Probability: {0:.5f}'.format(p))
```

#### 5.2.4 非一様乱数
```python {cmd=true}
import random

def toss():
    # 0 -> Heads, 1 -> Tails
    if random.random() < 2/3:
        return 0
    else:
        return 1
```

```python {cmd=true}
'''
各種紙幣を異なる確率で払う空想ATMのシミュレーション
'''
import random

def get_index(probability):
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
        r = random.random()
        for index, sp in enumerate(sum_probability):
            if r <= sp:
                return index
        return len(probability)-1

def dispens():

    dollar_bills = [5, 10, 20, 50]
    probability = [1/6, 1/6, 1/3, 1/3]
    bill_index = get_index(probability)
    return dollar_bills[bill_index]

```
