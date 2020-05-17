from src.runner.runner import Runner


def test_019():
    p = Runner(19)
    # p.run("auto_fill_rot")
    # self.assertEqual(p.eval_distance(), 0)


def test_26():
    p = Runner(26, verbose=True)
    # p.run("auto_fill_rot")
    # p.run("diff_color")


def test_61():
    p = Runner(61, verbose=True)


def test_64():
    p = Runner(64, verbose=True)


def test_134():
    p = Runner(134, verbose=True)


def test_140():
    p = Runner(140, verbose=True)


def test_217():
    p = Runner(217, verbose=True)


def test_221():
    p = Runner(221, verbose=True)


def test_261():
    p = Runner(261, verbose=True)


def test_507():
    p = Runner(107, "eval", verbose=True)
    p.run("auto_fill_line_symmetry_del")


def test_576():
    p = Runner(176, "eval", verbose=True)
    p.run("trim_background")


def test_588():
    p = Runner(188, "eval", verbose=True)
    p.run("trim_background")


def test_598():
    p = Runner(198, "eval", verbose=True)


def test_599():
    p = Runner(199, "eval", verbose=True)


def test_711():
    p = Runner(311, "eval", verbose=True)


def test_814():
    p = Runner(314, "eval", verbose=True)


def test_819():
    p = Runner(319, "eval", verbose=True)


def test_825():
    p = Runner(325, "eval", verbose=True)


def test_827():
    p = Runner(327, "eval", verbose=True)


def test_783():
    p = Runner(383, "eval", verbose=True)
    p.run("fusion")
    p.run("auto_fill_line_symmetry_del")


if __name__ == "__main__":
    test_019()
    test_26()
    test_61()
    test_140()
    test_261()
    test_507()
    test_783()
