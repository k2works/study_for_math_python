# coding=utf-8

'''
pyplotを使った簡単なプロット
'''

import matplotlib.pyplot as plt

def create_graph():
    x_numbers=[1,2,3]
    y_numbers=[2,4,6]
    plt.plot(x_numbers, y_numbers)
    plt.show()

'''
2物体間の万有引力と距離の関係
'''
import matplotlib.pyplot as plt
# グラフを描く
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distace')
    plt.show()

def generate_F_r():
    # generate value for r
    r = range(100, 1001, 50)
    # Fの計算値を格納数する空リスト
    F = []
    # 定数G
    G = 6.674*(10**-11)
    # two masses
    m1 = 0.5
    m2 = 1.5
    # 引力を計算しリストFに加える
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    # draw_graph関数呼び出し
    draw_graph(r, F)

'''
２つの値の間の等間隔な浮動小数点数の生成
'''
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

'''
投射運動物体の軌跡を描く
'''
from matplotlib import pyplot as plt
import math
def draw_trajectory_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projecttitle motion of a ball')

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # find time intervals
    intervals = frange(0, t_flight, 0.001)
    # list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_trajectory_graph(x, y)
