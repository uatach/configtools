import attr

from json import dumps

from configtools.config import load

config = load({'some': {'key': 'value'}})


def test_func():
    def func():
        return 'works'

    assert func() == config.inject(func)()


def test_func_with_param():
    @config.inject
    def func(some):
        return dumps(some)

    assert func() == '{"key": "value"}'


def test_func_with_prefix():
    @config.inject(prefix='some')
    def func(key):
        return dumps(key)

    assert func() == '"value"'


def test_class():
    @attr.s
    class Class(object):
        pass

    assert Class() == config.inject(Class)()


def test_class_with_param():
    @config.inject
    @attr.s
    class Class(object):
        some = attr.ib()

    assert dumps(config._config['some']) == dumps(Class().some)
