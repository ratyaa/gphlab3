import pandas as pd
import math
import matplotlib.pyplot as plt

csv_ids = ["0" + str(id) if id < 10 else str(id) for id in range (1, 21)]
ms = [10, 15, 30, 45, 60, 75, 90, 100]

A_base = []
A_side = []
A_base_dd = []
A_side_dd = []

data_sets = [
    [
        pd.read_csv(
            "data/22." + str(id) + "p/22." + str(id) + "p_" + csv_id + ".csv",
            skiprows=3,
            header=None,
        ) for csv_id in csv_ids
    ]
    for id in ms]

for m, datas in zip(ms, data_sets):
    outrows = []
    Tout = []

    for i in range(0, 20):
        data = datas[i]
        outrows.append([])
        Tout.append([])
        
        for n in range (20, 81):
            slice = data[data[0].between(n - 0.5, n + 0.5)]
            outrows[i].append(slice[1].idxmax())

        exs = data.iloc[outrows[i]].copy().reset_index(drop=True)
        outexs = []
        for n in range (0, 3):
            idxmax = exs[1].idxmax()
            Tout[i].append(exs[1][idxmax])
            exs.drop(axis=0, index=idxmax, inplace=True)


    Toutdf = pd.DataFrame(Tout)
    base = Toutdf.iloc[:, 0] * 1000
    side = pd.concat([Toutdf.iloc[:, 1], Toutdf.iloc[:, 2]]) * 1000

    A_base.append(base.mean())
    A_base_dd.append(base.std() / math.sqrt(len(base.index)))

    A_side.append(side.mean())
    A_side_dd.append(side.std() / math.sqrt(len(side.index)))

out = pd.DataFrame([ms, A_base, A_base_dd, A_side, A_side_dd]).transpose()
out.columns = ["m", "A_base", "A_base_dd", "A_side", "A_side_dd"]
out["A_base_ed"] = out["A_base_dd"] / out["A_base"] * 100
out["A_side_ed"] = out["A_side_dd"] / out["A_side"] * 100
out["A_ratio"] = out["A_side"] / out["A_base"] * 100
out["A_ratio_ed"] = (out["A_base_ed"].pow(2) + out["A_side_ed"].pow(2)).pow(0.5)
out["A_ratio_dd"] = out["A_ratio_ed"] * out["A_ratio"] / 100
out["m(в ед.)"] = out["m"]
out["dummy"] = 0

# print(out.to_csv())
# print(out)

out.index += 1

# styling
m_l = "$m$, \\%"
A_base_l = "$a_{\\mathrm{base}}$, мВ"
A_base_ed_l = "$\\varepsilon_{a_{\\mathrm{base}}}$, \\%"
A_side_l = "$a_{\\mathrm{side}}$, мВ"
A_side_ed_l = "$\\varepsilon_{a_{\\mathrm{side}}}$, \\%"
A_ratio_l = "$a_{\\mathrm{side}} / a_{\\mathrm{base}}$, \\%"
A_ratio_ed_l = "$\\varepsilon_{(a_{\\mathrm{side}} / a_{\\mathrm{base}})}$, \\%"

print(
    out[["m", "A_base", "A_base_ed", "A_side", "A_side_ed", "A_ratio", "A_ratio_ed"]]
    .rename(columns={
        "m": m_l,
        "A_base": A_base_l,
        "A_base_ed": A_base_ed_l,
        "A_side": A_side_l,
        "A_side_ed": A_side_ed_l,
        "A_ratio": A_ratio_l,
        "A_ratio_ed": A_ratio_ed_l,
    })
    .style

    .format(subset=m_l, precision=0, decimal=",")
    .format(subset=A_base_l, precision=2, decimal=",")
    .format(subset=A_base_ed_l, precision=3, decimal=",")
    .format(subset=A_side_l, precision=2, decimal=",")
    .format(subset=A_side_ed_l, precision=3, decimal=",")
    .format(subset=A_ratio_l, precision=3, decimal=",")
    .format(subset=A_ratio_ed_l, precision=3, decimal=",")

    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|c|c|c|",
        label="tbl:7",
        # caption="Седьмой пункт",
        clines="all;data",
        position_float="centering",
    ))
