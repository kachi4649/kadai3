#!/usr/bin/python3
# SPDX-FileCopyright: 2023 Takuma Kachi
# SPDX-License-Identifier: BSD-3-Clause

import random

i = 0
list1 = list(range(1,100+1))
list2 = ["+", "-", "*", "/"]
j = random.choices(list1,k=2)
m = random.choice(list2)

if m == "+":
    a = j[0] + j[1]
    print("{}+{}".format(j[0], j[1]))

elif m == "-":
    a = j[0] - j[1]
    print("{}-{}".format(j[0], j[1]))

elif m == "*":
    a = j[0] * j[1]
    print("{}*{}".format(j[0], j[1]))

else:
    a = j[0] / j[1]
    if a % 0.5 == 0:
        a += 0.5
#round()は四捨五入するときに.5の値を偶数の値にしてしまうため。
    a = round(a)
    print("{}/{}".format(j[0], j[1]))
    print("(答えは四捨五入)")

while True:
    i += 1
    s = input("答え＝")
    n = int(s)
    if a == n:
        print("正解")
        break
    elif i == 6:
        print("6回失敗したため終わります。")
        break
    else:
        print("答えが違うよ")

