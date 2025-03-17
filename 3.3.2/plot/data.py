import pandas as pd
import math
import matplotlib.pyplot as plt
import argparse
import locale

locale.setlocale(locale.LC_ALL, "ru_RU")


parser = argparse.ArgumentParser(
    description='bananchiki')

data_choices = ["13", "14", "15", "16", "all"]
mode_choices = ["csv", "print", "tex"]

parser.add_argument("-i", "--inputfile", type=str, choices=data_choices)
parser.add_argument("-m", "--mode", type=str, choices=mode_choices)

args = parser.parse_args()

data = pd.DataFrame()

if args.inputfile != "all":
    data = pd.read_csv(
        "plot/" + args.inputfile + "A.csv",
        skiprows=1,
        header=None,
    )
else:
    data = pd.concat([
        pd.read_csv(
            "plot/" + str(tok) + "A.csv",
            skiprows=1,
            header=None,
        ) for tok in range(13, 17)
    ], axis=0, ignore_index=True)

data.columns = ["U", "I"]
data.index += 1

data["dI"] = data["I"] * 0.002
data["dU"] = 0.1
data["U^3/2"] = data["U"].pow(3.0 / 2.0)
data["dU^3/2"] = data["dU"] / data["U"] * (3.0 / 2.0) * data["U^3/2"]

def round_quantity_df(df, q_index, e_index):
    for index, row in df.iterrows():
        e = row[e_index]
        order = math.floor(math.log10(abs(e)))
        
        first_fig = int(str(e / math.pow(10, order))[0])
        # print(first_fig)
        if first_fig == 1 or first_fig == 2:
            order = order - 1

        if order < 0:
            df.loc[index, e_index] = locale.format_string(
                ("%." + str(-order) + "f"), round(e, -order))
            df.loc[index, q_index] = locale.format_string(
                ("%." + str(-order) + "f"), round(row[q_index], -order))
        else:
            df.loc[index, e_index] = locale.format_string("%.0f", round(e, -order))
            df.loc[index, q_index] = locale.format_string("%.0f", round(row[q_index], -order))

sigma = 0
if args.inputfile == "all":
    data = data[data["U"] > 12].reset_index(drop=True)
    data["U^3"] = data["U^3/2"].pow(2)
    data["I^2"] = data["I"].pow(2)

    xmean = data["U^3"].mean()
    ymean = data["I^2"].mean()

    sigma = math.sqrt(((ymean / xmean) - 17.2277 * 17.2277) / 30)

match args.mode:
    case "csv":
        print(data.to_csv())
    case "print":
        print(data)
        if args.inputfile == "all":
            print(sigma)
    case "tex":
        u_l = "$U$, В"
        i_l = "$I$, мкА"
        du_l = "$\\delta_U$, В"
        di_l = "$\\delta_I$, мкА"
        u32_l = "$U^{\\frac{3}{2}},\\ В^{\\frac{3}{2}}$"
        du32_l = "$\\delta_{U^{\\frac{3}{2}}},\\ В^{\\frac{3}{2}}$"
        
        round_quantity_df(data, "I", "dI")
        round_quantity_df(data, "U^3/2", "dU^3/2")
        
        print(
            data[["U", "dU", "I", "dI", "U^3/2", "dU^3/2"]]
            .rename(columns={
                "U": u_l,
                "dU": du_l,
                "I": i_l,
                "dI": di_l,
                "U^3/2": u32_l,
                "dU^3/2": du32_l,
            })
            .style

            .format(subset=du_l, precision=1, decimal=",")
            .format(subset=u_l, precision=1, decimal=",")

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
