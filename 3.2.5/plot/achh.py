import pandas as pd
import math
import matplotlib.pyplot as plt

out = pd.read_table(
    "plot/smooth_achh.dat",
    skiprows=4,
    header=None,
    sep="\s+"
)[[0, 1]]

median = 1 / math.sqrt(2)
df_sort = pd.concat([
    out[out[0].between(0.5, 1)].iloc[(out[out[0].between(0.5, 1)][1]-median).abs().argsort()[:1]],
    out[out[0].between(1, 1.5)].iloc[(out[out[0].between(1, 1.5)][1]-median).abs().argsort()[:1]]
])
print(1/df_sort.diff()[0][6912])
# print(out.iloc[(out[out[0].between(1, 1.5)][1]-median).abs().argsort()[:10]])
# print(out)
