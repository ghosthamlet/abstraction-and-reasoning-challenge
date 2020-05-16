from src.runner.runner import Runner


def test_2():
    p = Runner(2, verbose=True)
    p.run("extend_shape")
    p.run("auto_fill_row_col_periodicity")
    p.run("keep_max_color")


def test_5():
    p = Runner(5, verbose=True)
    p.run("mesh_align")
    p.run("reduce_bitwise")


def test_5_2():
    p = Runner(5, verbose=True)
    for op in ['mesh_align', 'switch_color', 'fit_replace_rule_33']:
        p.run(op)


def test_9():
    p = Runner(9, verbose=True)
    p.run("connect")
    p.run("arg_sort")
    p.run("auto_paste")


def test_019():
    p = Runner(19)
    # p.run("auto_fill_rot")
    # self.assertEqual(p.eval_distance(), 0)


def test_26():
    p = Runner(26, verbose=True)
    # p.run("auto_fill_rot")
    # p.run("diff_color")


def test_46():
    p = Runner(46, verbose=True)
    p.run("color")
    p.run("point_cross")


def test_51():
    p = Runner(51, verbose=True)
    p.run("keep_mesh")


def test_61():
    p = Runner(61, verbose=True)


def test_64():
    p = Runner(64, verbose=True)


def test_134():
    p = Runner(134, verbose=True)


def test_140():
    p = Runner(140, verbose=True)


def test_221():
    p = Runner(221, verbose=True)


def test_243():
    p = Runner(243, verbose=True)


def test_258():
    p = Runner(258, verbose=True)
    p.run("change_background")
    p.run("trim_background")
    p.run("color_change")


def test_261():
    p = Runner(261, verbose=True)


def test_406():
    p = Runner(6, "eval", verbose=True)
    p.run("shadow_bool")
    p.run("switch_color")
    p.run("fractal")


def test_425():
    p = Runner(25, "eval", verbose=True)
    p.run("color_connect4")
    p.run("auto_add_color")


def test_433():
    p = Runner(33, "eval", verbose=True)
    p.run("shadow_mesh")
    p.run("fractal")


def test_446():
    p = Runner(46, "eval", verbose=True)
    p.run("mesh_split")
    p.run("switch_color")
    p.run("color_change")


def test_458():
    p = Runner(58, "eval", verbose=True)
    p.run("point_cross")
    p.run("interior_dir4_zero")


def test_467():
    p = Runner(67, "eval", verbose=True)
    p.run("shadow_max")
    p.run("fractal")


if __name__ == "__main__":
    test_2()
    test_5()
    test_5_2()
    test_9()
    test_019()
    test_26()
    test_46()
    test_51()
    test_61()
    test_140()
    test_258()
    test_261()
    test_406()
    test_425()
    test_433()
    test_446()
    test_458()
    test_467()
