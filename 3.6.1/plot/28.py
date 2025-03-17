import pandas as pd
import math
import matplotlib.pyplot as plt

csv_ids = ["0" + str(id) if id < 10 else str(id) for id in range (1, 21)]
T = 3 # us

datas = [
    pd.read_csv(
        "data/28/28_" + csv_id + ".csv",
        skiprows=3,
        header=None,
    ) for csv_id in csv_ids
]

datas_ish = [
    pd.read_csv(
        "data/28ISHODNYISIgNal/28ISHODNYISIgNal_" + csv_id + ".csv",
        skiprows=3,
        header=None,
    ) for csv_id in csv_ids
]

outrows = []
Tout = []

outrows_ish = []
Tout_ish = []

nu = pd.DataFrame()
a = pd.DataFrame()
a_f = pd.DataFrame()

for i in range(0, 20):
    data = datas[i]
    tail = data.tail(1).iloc[0][0]
    outrows.append([])
    Tout.append(None)
    
    data_ish = datas_ish[i]
    tail_ish = data.tail(1).iloc[0][0]
    outrows_ish.append([])
    Tout_ish.append(None)
    
    n = 1
    while n * 1/T < tail and n * 1/T < tail_ish:
        slice = data[data[0].between((n - 0.1) * 1/T, (n + 0.1) * 1/T)]
        outrows[i].append(slice[1].idxmax())
        
        slice_ish = data_ish[data_ish[0].between((n - 0.1) * 1/T, (n + 0.1) * 1/T)]
        outrows_ish[i].append(slice_ish[1].idxmax())
        n += 1

    Tout[i] = data.iloc[outrows[i]].copy().reset_index(drop=True)
    Tout_ish[i] = data_ish.iloc[outrows_ish[i]].copy().reset_index(drop=True)

    nu[2 * i] = Tout[i][0]
    nu[2 * i + 1] = Tout_ish[i][0]
    a_f[i] = Tout[i][1]
    a[i] = Tout_ish[i][1]

nu.index += 1
a.index += 1
a_f.index += 1

out = pd.DataFrame()
    
a = a.transpose()
a_f = a_f.transpose()
nu = nu.transpose()

out["nu_mean"] = nu.mean()
out["nu_dd"] = nu.std() / math.sqrt(len(nu.index))
out["nu_ed"] = out["nu_dd"] / out["nu_mean"] * 100
out["a_mean"] = a.mean() * 1000
out["a_dd"] = a.std() / math.sqrt(len(a.index)) * 1000
out["a_ed"] = out["a_dd"] / out["a_mean"] * 100
out["a_f_mean"] = a_f.mean() * 1000
out["a_f_dd"] = a_f.std() / math.sqrt(len(a_f.index)) * 1000
out["a_f_ed"] = out["a_f_dd"] / out["a_f_mean"] * 100
out["K(%)"] = out["a_f_mean"] / out["a_mean"] * 100
out["K_ed"] = (out["a_ed"].pow(2) + out["a_f_ed"].pow(2)).pow(0.5)
out["K_dd"] = out["K(%)"] * out["K_ed"] / 100
out["1/K^2"] = 1 / (out["K(%)"] / 100).pow(2)
out["1/K^2_dd"] = out["1/K^2"] * 2 * out["K_ed"] / 100
out["omega^2"] = 4 * math.pi ** 2 * out["nu_mean"].pow(2)
out["omega^2_dd"] = out["omega^2"] * 2 * out["nu_ed"] / 100

# print(out)
# print(out.to_csv())
# print(out.iloc[[i for i in range(0, 11)]])
# print(out.iloc[[i for i in range(0, 7)]].to_csv())

# stylin

nu_l = "$\\nu$, кГц"
nu_dd_l = "$\\delta_{\\nu}$, кГц"
a_l = "$a^0$, мВ"
a_f_l = "$a^{\\mathrm{f}}$, мВ"
k_l = "$K$, \\%"
klin_l = "$\\sfrac{1}{K^2}$" 
klin_dd_l = "$\\delta_{\\sfrac{1}{K^2}}$"
omega_l = "$\\omega^2 \\cdot 10^{-6}$"
omega_dd_l = "$\\delta_{\\omega^2} \\cdot 10^{-6}$"

print(
    out.iloc[[i for i in range(0, 7)]][["nu_mean", "nu_dd", "a_mean", "a_f_mean", "K(%)", "1/K^2", "1/K^2_dd", "omega^2", "omega^2_dd"]]
    .rename(columns={
        "nu_mean": nu_l,
        "nu_dd": nu_dd_l,
        "a_mean": a_l,
        "a_f_mean": a_f_l,
        "K(%)": k_l,
        "1/K^2": klin_l,
        "1/K^2_dd": klin_dd_l,
        "omega^2": omega_l,
        "omega^2_dd": omega_dd_l,
    })
    .style

    .format(subset=nu_l, precision=5, decimal=",")
    .format(subset=nu_dd_l, precision=5, decimal=",")
    .format(subset=a_l, precision=1, decimal=",")
    .format(subset=a_f_l, precision=2, decimal=",")
    .format(subset=k_l, precision=2, decimal=",")
    .format(subset=klin_l, precision=0, decimal=",")
    .format(subset=klin_dd_l, precision=0, decimal=",")
    .format(subset=omega_l, precision=3, decimal=",")
    .format(subset=omega_dd_l, precision=3, decimal=",")

    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        # column_format="|c|c|c|c|c|",        
        column_format="|c|c|c|c|c|c|c|c|c|c|",
        label="tbl:7",
        # caption="Седьмой пункт",
        clines="all;data",
        position_float="centering",
    ))
