import pandas as pd
import math
import matplotlib.pyplot as plt

out = pd.read_csv(
    "plot/fachh.csv"
)

# stylin

t_l = "$\\Delta\\tau$, мс"
t_dd_l = "$\\delta_{\\Delta\\tau}$, мс"
u_l = "$2U$, В"
uu_l = "$U/U_0$"
uu_dd_l = "$\\delta_{U/U_0}$"
nu_l = "$\\nu$, кГц"
nu_dd_l = "$\\delta_{\\nu}$, кГц"
nunu_l = "$\\nu/\\nu_0$"
nunu_dd_l = "$\\delta_{\\nu/\\nu_0}$"
phi_l = "$\\varphi$"
phi_dd_l = "$\\delta_{\\varphi}$"

out.index += 1

# print(out)
print(
    # out[["delta_t", "2U", "nu", "dt", "dnu", "U/U", "nu/nu", "phi", "dU/U", "dnu/nu", "dphi"]]
    # out[["delta_t", "2U", "nu", "U/U", "nu/nu", "dU/U", "dnu/nu"]]
    out[["delta_t", "2U", "nu", "dt", "dnu", "phi", "dphi"]]
    .rename(columns={
        "delta_t": t_l,
        "2U": u_l,
        "nu": nu_l,
        "dt": t_dd_l,
        "dnu": nu_dd_l,
        # "U/U": uu_l,
        # "nu/nu": nunu_l,
        "phi": phi_l,
        # "dU/U": uu_dd_l,
        # "dnu/nu": nunu_dd_l,
        "dphi": phi_dd_l,
    })
    .style

    .format(subset=t_l, precision=1, decimal=",")
    .format(subset=t_dd_l, precision=1, decimal=",")
    .format(subset=u_l, precision=2, decimal=",")
    # .format(subset=uu_l, precision=4, decimal=",")
    # .format(subset=uu_dd_l, precision=4, decimal=",")
    .format(subset=nu_l, precision=3, decimal=",")
    .format(subset=nu_dd_l, precision=3, decimal=",")
    # .format(subset=nunu_l, precision=4, decimal=",")
    # .format(subset=nunu_dd_l, precision=4, decimal=",")
    .format(subset=phi_l, precision=3, decimal=",")
    .format(subset=phi_dd_l, precision=3, decimal=",")

    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|c|c|c|",
        # label="tbl:7",
        # caption="Измерения для АЧХ",
        caption="Измерения для ФЧХ",
        clines="all;data",
        position_float="centering",
    ))
