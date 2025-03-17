import pandas as pd
import math
import scipy as si

data = pd.read_csv("plot/lnu2.csv", header=None, skiprows=1)

nu = "$\\nu$, Гц"
l = "$L$, мГн"
nusq = "$\\nu^2,\\ кГц^2$"
# xi = "$\\frac{1}{\\xi^2},\\ (А \\cdot Гц / В)^2$"
ll = "$\\frac{L_{max} - L_{min}}{L - L_{min}}$"
# tan = "$\\tan{\\psi}$"

data.columns = [nu, l, "sdflj", "skdfj", nusq, ll, "lsdfjk", "owieu"]
        
print(
    data[[nu, l, nusq, ll]]
    # .rename(columns={
    #     "In": i,
    #     "k": k,
    #     "dk": dk,
    #     "e/m": em,
    #     "d(e/m)": dem,
    #     "e(e/m)": eem,
    # })
    .style

    .format(subset=nu, precision=1, decimal=",")
    .format(subset=l, precision=3, decimal=",")
    # .format(subset=u, precision=4, decimal=",")
    .format(subset=nusq, precision=2, decimal=",")
    # .format(subset=xi, precision=0, decimal=",")
    .format(subset=ll, precision=3, decimal=",")
    # .format(subset=tan, precision=2, decimal=",")

    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|",
        # label="tbl:7",
        # caption="Седьмой пункт",
        clines="all;data",
        position_float="centering",
    ))
