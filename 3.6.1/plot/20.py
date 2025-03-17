import pandas as pd
import math
import matplotlib.pyplot as plt

csv_ids = ["0" + str(id) if id < 10 else str(id) for id in range (1, 21)]

datas = [pd.read_csv(
            "data/20/20_" + csv_id + ".csv",
            skiprows=3,
            header=None,
        ) for csv_id in csv_ids]

nu_0 = 50
nu_mod = 2
m = 0.5

result_df = pd.DataFrame()

for i in range(0,20):
    data = datas[i]
    tail = data.tail(1).iloc[0][0]
    head = data.head(1).iloc[0][0]
    
    outrows = []
    local_exs = None
    global_mins = None
    global_maxs = None

    id_first_max = data[data[0].between(head, head + 1/nu_0)][1].idxmax()
    t_first_max = data[0][id_first_max]

    n = 1

    while t_first_max + n * 1/nu_0 < tail:
        slice = data[data[0].between(t_first_max + (n - 0.5) * 1/nu_0, t_first_max + (n + 0.5) * 1/nu_0)]
        outrows.append(slice[1].idxmax())
        n += 1

    local_exs = data.iloc[outrows].copy().reset_index(drop=True)

    n = 0
    mins = []
    maxs = []
    while t_first_max + n * 1/nu_mod < tail:
        slice = local_exs[local_exs[0].between(t_first_max + n * 1/nu_mod, t_first_max + (n + 1) * 1/nu_mod)]
        maxs.append(slice[1].idxmax())
        mins.append(slice[1].idxmin())
        n += 1

    global_mins = local_exs.iloc[mins].copy().reset_index(drop=True)
    global_maxs = local_exs.iloc[maxs].copy().reset_index(drop=True)

    globals = pd.concat([global_mins, global_maxs], axis=1)
    result_df = pd.concat([result_df, globals])

result_df.columns = ["min_t", "min_A", "max_t", "max_A"]

result_df["sum_A"] = result_df["max_A"] + result_df["min_A"]
result_df["diff_A"] = result_df["max_A"] - result_df["min_A"]
result_df["m"] = result_df["diff_A"] / result_df["sum_A"]

m_mean = result_df["m"].mean()
A_min = result_df["min_A"].mean()
A_max = result_df["max_A"].mean()
A_min_dd = result_df["min_A"].std() / math.sqrt(len(result_df.index))
A_max_dd = result_df["max_A"].std() / math.sqrt(len(result_df.index))
m_dd = result_df["m"].std() / math.sqrt(len(result_df.index))
m_ed = m_dd / m_mean * 100
m_diff_ed = (m - m_mean) / m * 100

print(
    "A_max = " + str(A_max) + "\n" +
    "delta_A_max = " + str(A_max_dd) + "\n" +
    "A_min = " + str(A_min) + "\n" +
    "delta_A_min = " + str(A_min_dd) + "\n" +
    "m(теор.) = 0.5\n" +
    "m = " + str(m_mean) + "\n" +
    "delta_m = " + str(m_dd) + "\n" +
    "e(%) = " + str(m_ed) + "\n" +
    "diff(%) = " + str(m_diff_ed) 
)
