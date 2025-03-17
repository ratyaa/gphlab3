import pandas as pd
import math
import matplotlib.pyplot as plt


out = pd.read_csv(
    "plot/6.csv"
)

# stylin

i_l = "$I$, А"
i_dd_l = "$\\delta_I$, А"
b_l = "$B$, мТл"
b_dd_l = "$\\delta_B$, мТл"
isq_l = "$\\sqrt{I},\\ A^{\\frac{1}{2}}$"
isq_dd_l = "$\\delta_{\\sqrt{I}},\\ A^{\\frac{1}{2}}$"

out.index += 1

# print(out)
print(
    out[["I,A", "B,mT", "dI", "dB", "I^2", "dI^2"]]
    .rename(columns={
        "I,A": i_l,
        "B,mT": b_l,
        "dI": i_dd_l,
        "dB": b_dd_l,
        "I^2": isq_l,
        "dI^2": isq_dd_l,
    })
    .style

    .format(subset=i_l, precision=2, decimal=",")
    .format(subset=i_dd_l, precision=2, decimal=",")
    .format(subset=b_l, precision=1, decimal=",")
    .format(subset=b_dd_l, precision=1, decimal=",")
    .format(subset=isq_l, precision=3, decimal=",")
    .format(subset=isq_dd_l, precision=3, decimal=",")

    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|c|c|",
        # label="tbl:7",
        caption="ВСЕМ ПОХУЙ))))",
        clines="all;data",
        position_float="centering",
    ))
