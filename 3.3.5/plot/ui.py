import pandas as pd
import math
import matplotlib.pyplot as plt

names = [
    "Cu_0.2A",
    "Cu_0.4A",
    "Cu_0.6A",
    "Cu_0.81A",
    "Cu_1.03A",
    "Cu_1.16A",
    "Zn_1.00A",
]



outs = [pd.read_csv(
    "plot/" + name + ".csv"
) for name in names]

# stylin


u_l = "$U$, нВ"
u_dd_l = "$\\delta_U$, нВ"
i_l = "$I_M$, А"
i_dd_l = "$\\delta_{I_M}$, А"
b_l = "$B$, мТл"
b_dd_l = "$\\delta_B$, мТл"

for out, name in zip(outs, names):
    out.index += 1
    out[["u real talk", "dU", "I_m,A", "dA", "B, mT", "dB"]].rename(columns={
        "I_m,A": i_l,
        "B, mT": b_l,
        "dA": i_dd_l,
        "dB": b_dd_l,
        "u real talk": u_l,
        "dU": u_dd_l,
    }).style.format(subset=i_l, precision=2, decimal=",").format(subset=i_dd_l, precision=2, decimal=",").format(subset=b_l, precision=1, decimal=",").format(subset=b_dd_l, precision=1, decimal=",").format(subset=u_l, precision=0, decimal=",").format(subset=u_dd_l, precision=0, decimal=",").set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False).to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|c|c|",
        # label="tbl:7",
        caption="AXAXAXAXAXAXAXAXAXA $" + name + "$",
        clines="all;data",
        position_float="centering",
        buf="tex/" + name + ".tex"
    )
