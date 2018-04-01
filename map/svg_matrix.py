import pandas as pd
import numpy as np
from decimal import Decimal
from collections import namedtuple

# input
with open("input", "r") as f:
    data = f.read()

data = data.replace(" ", "\n")

with open("input", "w") as f:
    f.write(data)

df = pd.read_csv('input', header=None, names=['x', 'y'], dtype=str)

nadf = df.isna()
Matrix = namedtuple("Matrix", ["a", "b", "c", "d", "e", "f"])

# matrix
# parameter = ["1.3779", "0", "0", "1.28047", "999.359", "-7.1216"]
# parameter = ["7.16973e-2", "0", "0", "7.19374e-2", "417.38", "371.111"]
# parameter = ["1", "0", "0", "1", "-2.22557e-4", "0"]
# parameter = ["1", "0", "0", "1", "-731.572", "0"]
# parameter = ["1", "0", "0", "1", "-706.114", "12.7291"]
parameter = ["1", "0", "0", "1", "731.572", "0"]

for i in range(len(parameter)):
    parameter[i] = Decimal(parameter[i])

m = Matrix(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4], parameter[5])

with open("output", "w") as f:
    for (item, flag) in zip(df.values, nadf.values):
        if not flag[1]:
            x = Decimal(str(item[0]))
            y = Decimal(str(item[1]))
            x1 = x * m.a + y * m.c + m.e
            y1 = x * m.b + y * m.d + m.f
            item[0], item[1] = str(x1), str(y1)
            print(str(x1), str(y1), sep=",", end=" ", file=f)
        else:
            print(item[0], end=" ", file=f)
