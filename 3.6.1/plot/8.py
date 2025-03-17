import pandas as pd
import math
import matplotlib.pyplot as plt

tau = [*range(20, 201, 10)]
data = [
    pd.read_csv(
        "data/8." + str(t) + "us/8." + str(t) + "us_01.csv",
        skiprows=3,
        header=None,
    ) for t in tau]
T = pow(10, -3)

for t in tau:
    for n in range(1, 1000)

# for x in range(1, 11):
#      slice = data[data[0].between(x - 0.5, x + 0.5)]
#      outrows.append(slice[1].idxmax())

# out = data.iloc[outrows].copy().reset_index(drop=True)
# out.columns = ["v_n", "a_n"]
# out.index += 1

# out["n"] = out["v_n"].round()
# out["v_n theor"] = out.index * 1.0
# out["a_n theor"] = out["n"].apply(theor_v)
# out["a_n/a_1"] = out["a_n"] / out["a_n"][1]
# out["a_n/a_1 theor"] = out["a_n theor"] / out["a_n theor"][1]
# out["a_n/a_1 exp/theor ratio"] = ((out["a_n/a_1"] / out["a_n/a_1 theor"] - 1)*100)

# # styling

# adiff_l = "$\\Delta_{\%}\\left(\\sfrac{a_n}{a_1}\\right)$"
# ath_l = "$\\left(\\sfrac{a_n}{a_1}\\right)^{т}$"
# aexp_l = "$\\sfrac{a_n}{a_1}$"
# freqe_l = "$\\nu_n$, кГц"
# freqt_l = "$\\nu_n^{т}$, кГц"

# out = out[["v_n theor", "v_n", "a_n/a_1", "a_n/a_1 theor", "a_n/a_1 exp/theor ratio"]]

# print(
#     out#.round(3).astype(str)
#     .rename(columns={
#         "v_n": freqe_l,
#         "v_n theor": freqt_l,
#         "a_n/a_1": aexp_l,
#         "a_n/a_1 theor": ath_l,
#         "a_n/a_1 exp/theor ratio": adiff_l,
#     })
#     .style
#     .format(subset=freqe_l, precision=1, decimal=",")
#     .format(subset=freqt_l, precision=1, decimal=",")
#     .format(subset=aexp_l, precision=3, decimal=",")
#     .format(subset=ath_l, precision=3, decimal=",")
#     .format(subset=adiff_l, precision=1, decimal=",")
#     .set_table_styles([
#         {"selector": "toprule", "props": ":hline;"},
#         {"selector": "bottomrule", "props": ":hline;"},
#         {"selector": "midrule", "props": ":hline;"},
#     ], overwrite=False)
#     .to_latex(
#         column_format="|c|c|c|c|c|c|",
#         label="tbl:7",
#         # caption="Седьмой пункт",
#         clines="all;data",
#         position_float="centering",
#     ))
