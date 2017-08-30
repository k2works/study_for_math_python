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
