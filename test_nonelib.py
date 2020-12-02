from pytest import raises

from nonelib import nonedict, nonewrap, nonelist, noneset, noneiter, NoneInArgsError


def test_nonedict():
    assert nonedict(a=1, b=None, c=3) == {'a': 1, 'c':3}


def test_nonedict_mapping():
    assert nonedict({'a': 1, 'b': None, 'c':3}) == {'a': 1, 'c':3}


def test_nonewrap():

    @nonewrap()
    def s(lst, offset=3, limit=3):
        return lst[offset:offset+limit]

    assert s([1,2,3,4,5,6,7,8,9,10], offset=None, limit=5) == [4, 5, 6, 7, 8]  # offset=3 is in effect


def test_nonelist():
    assert nonelist([1, None, 3]) == [1, 3]


def test_noneset():
    assert noneset({1, None, 3}) == {1, 3}


def test_noneiter():
    it = noneiter([1, None, 3])
    assert next(it, "foo") == 1
    assert next(it, "foo") == 3
    assert next(it, "foo") == "foo"


def test_nonewrap_none_in_args_error():

    @nonewrap()
    def f(x=1, y=2, z=3):
        return (x, y, z)

    with raises(NoneInArgsError):
        f(10, None, 30)


def test_nonewrap_allow_none_in_args():

    @nonewrap(none_args=True)
    def f(x=1, y=2, z=3):
        return (x, y, z)

    assert f(10, None, z=None) == (10, None, 3)
