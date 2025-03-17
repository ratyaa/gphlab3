import pandas as pd
import math
import matplotlib.pyplot as plt

csv_ids = ["0" + str(id) if id < 10 else str(id) for id in range (1, 21)]

# params = [[freq, T, N], ...]
param_sets = [
    [50, 1, 5],
    [75, 1, 5],
    [50, 2, 5],
    [50, 1, 10],
]
param_cols = list(map(list, zip(*param_sets)))

data_sets = [
    [
        pd.read_csv(
            "data/13." + str(id) + "/13." + str(id) + "_" + csv_id + ".csv",
            skiprows=3,
            header=None,
        ) for csv_id in csv_ids
    ]
for id in [1, 3, 4, 5]]

Delta_nu_res = []
Delta_nu_res_dd = []
Delta_nu_res_ed = []

delta_nu_res = []
delta_nu_res_dd = []
delta_nu_res_ed = []

for params, datas in zip(param_sets, data_sets):
    outrows = []
    Tout = []
    Delta_nu = []
    
    freq = params[0]
    T = params[1]
    N = params[2]

    for i in range(0, 20):
        data = datas[i]
        tail = data.tail(1).iloc[0][0]
        outrows.append([])
        Tout.append(None)
        
        n = 1
        while n * 1/T < tail:
            slice = data[data[0].between((n - 0.1) * 1/T, (n + 0.1) * 1/T)]
            outrows[i].append(slice[1].idxmax())
            n += 1

        Tout[i] = data.iloc[outrows[i]].copy().reset_index(drop=True)

        nu_max_i = Tout[i][1].idxmax()

        nu_i = nu_max_i + 1
        slice = Tout[i][1][nu_i - 2 : nu_i + 3]
        while slice.idxmin() != nu_i:
            nu_i += 1
            slice = Tout[i][1][nu_i - 2 : nu_i + 3]
        nu_right_min_i = nu_i

        nu_i = nu_max_i - 1
        slice = Tout[i][1][nu_i - 2 : nu_i + 3]
        while slice.idxmin() != nu_i:
            nu_i -= 1
            slice = Tout[i][1][nu_i - 2 : nu_i + 3]
        nu_left_min_i = nu_i
        
        Delta_nu.append(Tout[i][0][nu_right_min_i] - Tout[i][0][nu_left_min_i])

    Delta_nu_df = pd.DataFrame(Delta_nu)

    Delta_nu_mean = Delta_nu_df[0].mean()
    Delta_nu_std = Delta_nu_df[0].std() / math.sqrt(len(Delta_nu_df.index))
    
    Delta_nu_res.append(Delta_nu_mean)
    Delta_nu_res_dd.append(Delta_nu_std)
    Delta_nu_res_ed.append(Delta_nu_std / Delta_nu_mean * 100)

    delta_nu_df = pd.concat([Tout[i][0].diff() for i in range(0, 20)])
    delta_nu_mean = delta_nu_df.mean()
    delta_nu_std = delta_nu_df.std() / math.sqrt(len(delta_nu_df.index))

    delta_nu_res.append(delta_nu_mean)
    delta_nu_res_dd.append(delta_nu_std)
    delta_nu_res_ed.append(delta_nu_std / delta_nu_mean * 100)

param_sets_t = list(map(list, zip(*param_sets)))
out = pd.DataFrame()

out['freq'] = param_sets_t[0]
out['T'] = param_sets_t[1]
out['N'] = param_sets_t[2]
out['Delta_nu'] = Delta_nu_res
out['Delta_nu_dd'] = Delta_nu_res_dd
out['Delta_nu_ed'] = Delta_nu_res_ed
out['delta_nu'] = delta_nu_res
out['delta_nu_dd'] = delta_nu_res_dd
out['delta_nu_ed'] = delta_nu_res_ed

out.index += 1

# styling

fq_l = "$\\nu_0$, кГц"
T_l = "$T$, мс"
N_l = "$N$"

Dn_l = "$\\Delta\\nu$, кГц"
Dndd_l = "$\\delta_{\\Delta\\nu}$, кГц"
Dned_l = "$\\varepsilon_{\\Delta\\nu}$, \\%"

dn_l = "$\\delta\\nu$, кГц"
dndd_l = "$\\delta_{\\delta\\nu}$, кГц"
dned_l = "$\\varepsilon_{\\delta\\nu}$, \\%"

print(
    out#.round(3).astype(str)
    .rename(columns={
        "freq": fq_l,
        "T": T_l,
        "N": N_l,

        "Delta_nu" : Dn_l,
        "Delta_nu_dd" : Dndd_l,
        "Delta_nu_ed" : Dned_l,

        "delta_nu" : dn_l,
        "delta_nu_dd" : dndd_l,
        "delta_nu_ed" : dned_l,
    })
    # .transpose()
    .style

    .format(subset=fq_l, precision=0, decimal=",")
    .format(subset=T_l, precision=0, decimal=",")
    .format(subset=N_l, precision=0, decimal=",")
    
    .format(subset=Dn_l, precision=3, decimal=",")
    .format(subset=Dndd_l, precision=3, decimal=",")
    .format(subset=Dned_l, precision=2, decimal=",")

    .format(subset=dn_l, precision=4, decimal=",")
    .format(subset=dndd_l, precision=4, decimal=",")
    .format(subset=dned_l, precision=2, decimal=",")
    
    # .format(subset=pd.IndexSlice[[fq_l], :], precision=0, decimal=",")
    # .format(subset=pd.IndexSlice[[T_l], :], precision=0, decimal=",")
    # .format(subset=pd.IndexSlice[[N_l], :], precision=0, decimal=",")
    
    # .format(subset=pd.IndexSlice[[Dn_l], :], precision=3, decimal=",")
    # .format(subset=pd.IndexSlice[[Dndd_l], :], precision=3, decimal=",")
    # .format(subset=pd.IndexSlice[[Dned_l], :], precision=2, decimal=",")

    # .format(subset=pd.IndexSlice[[dn_l], :], precision=4, decimal=",")
    # .format(subset=pd.IndexSlice[[dndd_l], :], precision=4, decimal=",")
    # .format(subset=pd.IndexSlice[[dned_l], :], precision=2, decimal=",")

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
