import numpy as np
import timeit
from functools import partial


# a = np.arange(1, 7).reshape((3, 2))
# a_view = a[:2]
# a_copy = a[:2].copy()

# a_copy[1, 1] = 0
# print(a)
# 直接改动a
# a_view[1, 1] = 0
# print(a)


def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number


# a = np.random.rand(1000, 1000)
# b = np.random.rand(1000, 1000)

# copy
# def f1():
#     global b
#     b = 2 * b
#
# def f2():
#     global a
#     a *= 2

# print('%.6f - b = 2*b' % get_run_time(f1))
# print('%.6f - a *= 2' % get_run_time(f2))


# copy
# def f3():
#     a.flatten()
#
# def f4():
#     b.ravel()
#
# print('%.6f - flatten' % get_run_time(f3))
# print('%.6f- ravel' % get_run_time(f4))


# 使用take获取数据
# a = np.random.rand(1000000, 10)
# indices = np.random.randint(0, len(a), size=10000)
# print(indices)
#
#
# def f1():
#     _a = a[indices]
#
#
# def f2():
#     _ = np.take(a, indices, axis=0)
#
#
# print('%.6f-[indices]', get_run_time(f1))
# print('%.6f-take', get_run_time(f2))


# 使用compress
# a = np.random.rand(10000, 10)
# mask = a[:, 0] < 0.5
#
#
# def f1():
#     _ = a[mask]
#
#
# def f2():
#     _ = np.compress(mask, a, axis=0)
#
#
# print('%.6f-[mask]', get_run_time(f1))
# print('%.6f-compress', get_run_time(f2))


# out
# a = np.zeros([10000, 10])
#
# def f1(a):
#     a = a + 1
#
# def f2(a):
#     a = np.add(a, 1)
#
# print("%.6f - a+1 " % get_run_time(f1, a))
# print("%.6f - add " % get_run_time(f2, a))


# a = np.zeros([2, ])
# # copy
# a_copy = np.add(a, 1)
# print(a, a_copy)
#
# b = np.zeros([2, ])
# # copy
# c = np.zeros_like(b)
# # out赋值回原本的c，不用重新创建 a
# np.add(b, 1, out=c)
# print(b, c)

a = np.zeros([1000, 1000])
b = np.zeros_like(a)
c = np.zeros_like(a)


def f1():
    a[:] = np.add(a, 1)


def f2():
    np.add(b, 1, out=b)


def f3():
    _c = np.add(c, 1)


print('%.6f - without out' % get_run_time(f1))
print('%.6f - out' % get_run_time(f2))
print('%.6f - new data' % get_run_time(f3))