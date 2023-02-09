#!/usr/bin/python3
# SPDX-FileCopyright: 2023 Takuma Kachi
# SPDX-License-Identifier: BSD-3-Claus

import sys

argv = sys.argv
argv.pop(0)
print(argv)
argv.sort()
number = 1
for name in argv:
    #for number in i:
    print("NO{}:{}".format(number ,name))
    number += 1
