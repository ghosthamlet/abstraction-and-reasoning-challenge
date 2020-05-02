import os
import json
import tqdm
import datetime
import numpy as np

from src.auto_solve import auto_solve

TIME_LIMIT = 0.2


def local_eval(dir_path, time_limit=TIME_LIMIT):

    total_ac = 0
    total_wa = 0
    res_list = []

    for i, f in tqdm.tqdm(enumerate(list(sorted(os.listdir(dir_path))))):
        if f[-5:] == ".json":
            sample_data = json.load(open(f'{dir_path + f}', "r"))
            # print(sample_data)
            solved_dict = auto_solve(sample_data, time_limit=time_limit)
            for j in solved_dict.keys():
                assert len(solved_dict[j]) <= 3
                if len(solved_dict[j]) != 3:
                    print(i, j, len(solved_dict[j]))
                answer_arr = sample_data["test"][j]["output"]
                answer_str = "|" + "|".join(["".join(map(str, x)) for x in answer_arr]) + "|"
                if answer_str in solved_dict[j]:
                    # print(f'AC: {i, j}')
                    total_ac += 1
                    res_list.append(1)
                else:
                    # print(f'WA: {i, j}')
                    total_wa += 1
                    res_list.append(0)
    if "v" in dir_path:
        kbn = "evaluation"
    else:
        kbn = "training"
    pct = 1 - total_ac / (total_ac + total_wa)
    print(f'{dir_path} done, AC: {total_ac}, total: {total_ac + total_wa}, {pct}')
    np.save(f'../local_eval_log/{kbn}-{TIME_LIMIT}-{pct}-{datetime.datetime.now()}', np.array(res_list))


if __name__ == "__main__":
    local_eval("../input/training/")
    local_eval("../input/evaluation/")
