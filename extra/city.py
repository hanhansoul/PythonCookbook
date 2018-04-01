#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from decimal import Decimal
import json

df = pd.read_csv("input", names=["x", "y", "n"], header=None, dtype=str)

# matrix = (Decimal(12), Decimal(5))

# for item in df.values:
#     item[0] = str(Decimal(item[0]) + matrix[0])
#     item[1] = str(Decimal(item[1]) + matrix[1])

# df.to_csv("output", header=None, index=None)


d = df.to_dict('record')
