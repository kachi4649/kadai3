#!/bin/bash -xv
# SPDX-FileCopyrightText: 2023 Takuma Kachi
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo NG at Line $1
      res=1
}

res=0

### I/O TEST ###
out=$(./junban.py そら あいな たいち 12 a たくま)
[ "${out}" = "NO1:あいな" ] || ng ${LINENO}

out=$(./junban.py + 12 a)
[ "${out}" = "no" ] || ng ${LINENO}

[ "$res" = 0 ] && echo OK        # &&（AND記号）は左側が成功すると右側を実行
	exit $res
