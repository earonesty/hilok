import pytest
from hilok import HiLok, HiLokError


def test_wr_no_lev():
    h = HiLok(recursive=False)
    lk = h.write("/a/b")
    lk.release()
    lk = h.write("/a/b")

    with pytest.raises(HiLokError):
        lk = h.write("/a/b", block=False)


def test_with_wr():
    h = HiLok(recursive=False)
    with h.write("/a/b"):
        with pytest.raises(HiLokError):
            h.write("/a/b", block=False)

    with h.write("/a/b", block=False) as hh:
        pass


def test_with_rd():
    h = HiLok(recursive=False)
    with h.read("/a/b"):
        with h.read("/a/b", block=False):
            pass
        with pytest.raises(HiLokError):
            h.write("/a/b", block=False)
    with h.write("/a/b", block=False):
        pass


def test_other_sep():
    h = HiLok(":", recursive=False)
    with h.read("a:b"):
        with pytest.raises(HiLokError):
            h.write("a", block=False)
