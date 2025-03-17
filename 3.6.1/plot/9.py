import pandas as pd
import math
import matplotlib.pyplot as plt

Ts = [200, *range(500, 5001, 500)]
datas = [
    pd.read_csv(
        "data/9." + str(t) + "us/9." + str(t) + "us_01.csv",
        skiprows=3,
        header=None,
    ) for t in Ts]
tau = pow(10, -4)

out = pd.DataFrame()

for T, data in zip(Ts, datas):
    outrows = []
    tail = data.tail(1).iloc[0][0]
    n = 1
    while n * 1000/T < tail:
        slice = data[data[0].between((n - 0.12) * 1000/T, (n + 0.12) * 1000/T)]
        outrows.append(slice[1].idxmax())
        n += 1

    Tout = data.iloc[outrows].copy().reset_index(drop=True).diff()
    # if T == 1000:
    #     with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #         print(Tout)
    
    out.at[Ts.index(T), "T"] = T
    out.at[Ts.index(T), "1/T"] = 1000 / T
    out.at[Ts.index(T), "delta_freq"] = Tout[0].mean()
    out.at[Ts.index(T), "dd_freq"] = Tout[0].std() / math.sqrt(len(Tout.index))
    
out["ed_freq"] = out["dd_freq"] / out["delta_freq"] * 100
# out["dt"] = 0
out.index += 1

# styling

deltafq_l = "$\\delta\\nu$, кГц"
Tr_l = "$\\sfrac{1}{T},\\ мс^{-1}$"
T_l = "$T$, мкс"
ddfq_l = "$\\delta_{\\delta\\nu}$, кГц"
edfq_l = "$\\varepsilon_{\\delta\\nu}$, \\%"

# print(out)

# print(out.to_csv())
print(
    out#.round(3).astype(str)
    .rename(columns={
        "delta_freq": deltafq_l,
        "T": T_l,
        "1/T": Tr_l,
        "dd_freq": ddfq_l,
        "ed_freq": edfq_l,
    })
    .style
    .format(subset=deltafq_l, precision=3, decimal=",")
    .format(subset=ddfq_l, precision=3, decimal=",")
    .format(subset=edfq_l, precision=2, decimal=",")
    .format(subset=T_l, precision=0, decimal=",")
    .format(subset=Tr_l, precision=3, decimal=",")
    .set_table_styles([
        {"selector": "toprule", "props": ":hline;"},
        {"selector": "bottomrule", "props": ":hline;"},
        {"selector": "midrule", "props": ":hline;"},
    ], overwrite=False)
    .to_latex(
        column_format="|c|c|c|c|c|c|",
        label="tbl:7",
        # caption="Седьмой пункт",
        clines="all;data",
        position_float="centering",
    ))
