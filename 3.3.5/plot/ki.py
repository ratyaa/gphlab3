import pandas as pd
import math
import matplotlib.pyplot as plt

out = pd.read_csv(
    "plot/Cu_KI.csv"
)

# stylin

i_l = "$I$, А"
i_dd_l = "$\\delta_I$, А"
k_l = "$k$, нВ / мТл"
k_dd_l = "$\\delta_k$, нВ / мТл"

out.index += 1

# print(out)
print(
    out
    .rename(columns={
        "I, A": i_l,
        "k, нВ/мТл": k_l,
        "dk": k_dd_l,
        "dA": i_dd_l,
    })
    .style

    .format(subset=i_l, precision=2, decimal=",")
    .format(subset=i_dd_l, precision=2, decimal=",")
    .format(subset=k_l, precision=3, decimal=",")
    .format(subset=k_dd_l, precision=3, decimal=",")


    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|",
        # label="tbl:7",
        caption="ВСЕМ ПОХУЙ))))",
        clines="all;data",
        position_float="centering",
    ))
