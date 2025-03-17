import pandas as pd
import math
import matplotlib.pyplot as plt

out = pd.read_table(
    "plot/smooth_fchh.dat",
    skiprows=4,
    header=None,
    sep="\s+"
)[[0, 1]]

main = - math.pi/2
side_right = - math.pi/4
side_left = - math.pi/4 * 3
df = pd.concat([
    out.iloc[(out[1]-main).abs().argsort()[:1]],
    out.iloc[(out[1]-side_right).abs().argsort()[:1]],
    out.iloc[(out[1]-side_left).abs().argsort()[:1]]
]).copy().reset_index(drop=True)
print(df)
print(df[0][0] / (df[0][1] - df[0][2]))
# print(out.iloc[(out[out[0].between(1, 1.5)][1]-median).abs().argsort()[:10]])
# print(out)
