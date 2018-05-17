import yaml
import wrapt
import inspect

from functools import partial


def load(path):
    return Config(path)


@wrapt.decorator
def optional_kwargs(wrapped, instance, args, kwargs):
    if args:
        return wrapped(*args, **kwargs)
    return partial(wrapped, **kwargs)


class Config(object):
    def __init__(self, value):
        if isinstance(value, Config):
            self._config = dict(value._config)
        elif isinstance(value, dict):
            self._config = dict(value)
        else:
            with open(value, 'rt') as infile:
                self._config = yaml.load(infile)

    def __repr__(self):
        return str(self._config)

    def dump(self, path):
        with open(path, 'wt') as outfile:
            outfile.write(yaml.dump(self._config))

    @optional_kwargs
    def inject(self, func, prefix=None):
        config = self._config.get(prefix, self._config)
        spec = inspect.getfullargspec(
            func.__init__ if isinstance(func, type) else func)
        params = {}
        for k in spec.args:
            if k in config:
                params[k] = config[k]
            elif k != 'self':
                raise Exception(k)
        return partial(func, **params)
