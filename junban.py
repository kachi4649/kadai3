#!/usr/bin/python3
# SPDX-FileCopyright: 2023 Takuma Kachi
# SPDX-License-Identifier: BSD-3-Claus

import sys
import re

argv = sys.argv
argv.pop(0)
argv.sort()
number = 1
n = 0
for s in argv:
    h = re.search(r'[ぁ-んァ-ン]', s)
    if h == None:
        n += 1
del argv[0:n]
list1 = len(argv)
if list1 > 0:
    print("NO{}:{}".format(number ,argv[0]))
else:
    print("no")
