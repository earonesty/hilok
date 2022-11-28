from hilok import HiLok


def test_wr_no_lev():
    h = HiLok()
    lk = h.write("/a/b")
    lk.release()
    lk = h.write("/a/b")
    lk = h.write("/a/b", block=False)


def test_with_wr():
    h = HiLok()
    with h.write("/a/b"):
        h.write("/a/b", block=False)
    with h.write("/a/b", block=False):
        pass

