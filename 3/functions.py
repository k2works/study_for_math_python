# coding=utf-8

'''
平均を計算
'''

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # calculate the mean
    mean = s/N

    return mean

'''
中央値を計算
'''

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # 中央値を求める
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # 整数に変換、位置合わせ
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # 整数に変換、位置合わせ
        m = int(m) - 1
        median = numbers[m]

    return median

'''
最頻値を計算
'''

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

'''
数のリストに複数の最頻値があるときに最頻値を計算
'''

from collections import Counter

def calculate_modes(numbers):

    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


'''
数のリストの度数分布表
'''

from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number[1]))

'''
数のリストの度数分布表
数の順に表示するよう修正
'''

from collections import Counter
def frequency_sorted_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()

    print('Number\tFrequency')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0], number[1]))

'''
範囲を決める
'''

def find_range(numbers):

    lowest = min(numbers)
    highest = max(numbers)
    # find the range
    r = highest - lowest

    return lowest, highest, r

'''
数のリストの分散と標準偏差を求める
'''

def find_differences(numbers):
    # find the mean
    mean = calculate_mean(numbers)
    # find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):

    # 差のリストを求める
    diff = find_differences(numbers)
    # 差の2乗を求める
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # 分散を求める
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

'''
相関係数を計算するプログラム
'''

def find_corr_x_y(x,y):
    n = len(x)
    # 積の和を求める
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    # 和を求める
    x_square_sum = sum(x_square)
    y_square=[]
    for yi in y:
        y_square.append(yi**2)
    # 和を求める
    y_square_sum = sum(y_square)

    # 式を使って相関を計算
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominatior_term1 = n*x_square_sum - squared_sum_x
    denominatior_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominatior_term1*denominatior_term2)**0.5
    correlation = numerator/denominator

    return correlation

'''
ファイルに格納された数の和を求める
'''
def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
        print('Sum of the numbers: {0}'.format(s))

'''
ファイルに格納した平均を計算
'''
def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
        return numbers

'''
CSVファイルからデータを読み込む
'''
import csv
import matplotlib.pyplot as plt

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

def read_csv(filename):

    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
    return numbers, squared

def read_csv2(filename):

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))

    return summer, highest_correlated
