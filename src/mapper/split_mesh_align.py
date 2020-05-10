from typing import List
import numpy as np
from src.data import Problem, Case, Matter


class SplitMeshAlign:

    def __init__(self):
        pass

    @classmethod
    def find_mesh(cls, x_arr):
        """
        :param x_arr: np.array(int)
        :return: int, color, -1 if no mesh
        """
        for c in range(9, -1, -1):
            compare = np.zeros(x_arr.shape, dtype=np.int)
            # row
            sum_r = (x_arr == c).sum(axis=1)
            for i in range(x_arr.shape[0]):
                if sum_r[i] == x_arr.shape[1]:
                    compare[i, :] = 1
            # col
            sum_c = (x_arr == c).sum(axis=0)
            for j in range(x_arr.shape[1]):
                if sum_c[j] == x_arr.shape[0]:
                    compare[:, j] = 1

            if np.abs((compare == 1) ^ (x_arr == c)).sum() == 0 and compare.sum() > 0:
                return c
        return -1

    @classmethod
    def split_by_mesh(cls, x_arr, background=0):
        """
        :param x_arr: np.array(int)
        :param background: int
        :return: List[np.array], mesh split array
        """
        c = cls.find_mesh(x_arr)
        mesh = x_arr.copy()
        mesh[mesh != c] = background
        res_list = []
        row_split = np.where((x_arr == c).sum(axis=1) == x_arr.shape[1])[0]
        col_split = np.where((x_arr == c).sum(axis=0) == x_arr.shape[0])[0]
        # rows
        if row_split.shape[0] == 0:
            r0_list = [0]
            r1_list = [x_arr.shape[0]]
        elif row_split[0] != 0:
            if row_split[-1] != x_arr.shape[0] - 1:
                r0_list = [0] + list(row_split + 1)
                r1_list = list(row_split) + [x_arr.shape[0]]
            else:
                r0_list = [0] + list(row_split[:-1] + 1)
                r1_list = list(row_split)
        else:
            if row_split[-1] != x_arr.shape[0] - 1:
                r0_list = list(row_split + 1)
                r1_list = list(row_split[1:]) + [x_arr.shape[0]]
            else:
                r0_list = list(row_split[:-1] + 1)
                r1_list = list(row_split[1:])
        # cols
        if col_split.shape[0] == 0:
            c0_list = [0]
            c1_list = [x_arr.shape[1]]
        elif col_split[0] != 0:
            if col_split[-1] != x_arr.shape[1] - 1:
                c0_list = [0] + list(col_split + 1)
                c1_list = list(col_split) + [x_arr.shape[1]]
            else:
                c0_list = [0] + list(col_split[:-1] + 1)
                c1_list = list(col_split)
        else:
            if col_split[-1] != x_arr.shape[1] - 1:
                c0_list = list(col_split + 1)
                c1_list = list(col_split[1:]) + [x_arr.shape[1]]
            else:
                c0_list = list(col_split[:-1] + 1)
                c1_list = list(col_split[1:])

        for r0, r1 in zip(r0_list, r1_list):
            for c0, c1 in zip(c0_list, c1_list):
                res_list.append((x_arr[r0:r1, c0:c1], (r0, c0)))

        return res_list, mesh

    @classmethod
    def matter(cls, m: Matter) -> List[Matter]:
        """
        function to split a matter by mesh
        others aligned and drop mesh
        :param m: matter to split
        :return: List[Matter]
        """
        assert cls.find_mesh(m.values) != -1
        arr_list, mesh_arr = cls.split_by_mesh(m.values, m.background_color)
        res_list = []

        # split and align
        arr_0 = arr_list[0][0]
        for arr, _ in arr_list:  # drop position
            assert arr.shape == arr_0.shape
            new_matter = Matter(arr, np.int(0), np.int(0), m.background_color, new=True)
            res_list.append(new_matter)

        return res_list

    @classmethod
    def case(cls, c: Case) -> Case:
        assert len(c.matter_list) == 1
        new_case = c.copy()
        new_case.matter_list = cls.matter(c.matter_list[0])
        new_case.shape = new_case.matter_list[0].shape
        return new_case

    @classmethod
    def problem(cls, p: Problem) -> Problem:
        q: Problem = p.copy()
        q.train_x_list = [cls.case(c) for c in p.train_x_list]
        q.test_x_list = [cls.case(c) for c in p.test_x_list]
        return q


if __name__ == "__main__":
    x = np.array([[0, 2, 0], [2, 2, 2], [4, 2, 9]])
    print(SplitMeshAlign.find_mesh(x))
    print(SplitMeshAlign.split_by_mesh(x))
