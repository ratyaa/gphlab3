import pandas as pd
import math
import scipy as si

import argparse
import locale

locale.setlocale(locale.LC_ALL, "ru_RU")


parser = argparse.ArgumentParser(
    description='bananchiki')

mode_choices = ["csv", "print", "tex"]

parser.add_argument("-m", "--mode", type=str, choices=mode_choices)

args = parser.parse_args()

data = pd.DataFrame([
    [1.6, 17.9065, 0.04714],
    [1.5, 17.4858, 0.03212],
    [1.4, 17.0398, 0.04963],
    [1.3, 16.1084, 0.04084]
])

data.columns = ["In", "k", "dk"]

def form(k):
    return (81
            * pow(k, 2)
            * pow(0.98, 2)
            * pow(9.5 * pow(10, -3), 2)) / (128
                                            * pow(math.pi, 2)
                                            * pow(9 * pow(10, -3), 2)
                                            * pow(si.constants.epsilon_0, 2)
                                            * pow(10, 12))

data["e/m"] = data["k"].apply(form) / pow(10, 11)
data["d(e/m)"] = data["dk"] / data["k"] * 2 * data["e/m"]
data["e(e/m)"] = data["d(e/m)"] / data["e/m"] * 100

def emformat(x):
    return "$" + ("%.3f" % x) + " \\cdot 10^{-11}$"

data.index += 1

match args.mode:
    case "csv":
        print(data.to_csv())
    case "print":
        print(data)
    case "tex":
        i = "$I_н$, мкА"
        k = "$k,\\ мкА / В^{\\frac{3}{2}}$"
        dk = "$\\delta_k,\\ мкА / В^{\\frac{3}{2}}$"
        em = "$\\frac{e}{m}$, Кл/кг"
        dem = "$\\delta_{\\frac{e}{m}}$, Кл/кг"
        eem = "$\\varepsilon_{\\frac{e}{m}}$, \\%"
        
        print(
            data
            .rename(columns={
                "In": i,
                "k": k,
                "dk": dk,
                "e/m": em,
                "d(e/m)": dem,
                "e(e/m)": eem,
            })
            .style

            .format(subset=i, precision=1, decimal=",")
            .format(subset=k, precision=2, decimal=",")
            .format(subset=dk, precision=2, decimal=",")
            .format(formatter=emformat, subset=em, decimal=",")
            .format(formatter=emformat, subset=dem, decimal=",")
            .format(subset=eem, precision=1, decimal=",")

            .set_table_styles([
                {"selector": "toprule", "props": ":hline;"},
                {"selector": "bottomrule", "props": ":hline;"},
                {"selector": "midrule", "props": ":hline;"},
            ], overwrite=False)
            .to_latex(
                # column_format="|c|c|c|c|c|",        
                column_format="|c|c|c|c|c|c|c|",
                label="tbl:7",
                # caption="Седьмой пункт",
                clines="all;data",
                position_float="centering",
            ))
