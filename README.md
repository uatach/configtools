# configtools

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](http://choosealicense.com/licenses/mit/)
[![Build Status](https://travis-ci.org/uatach/configtools.svg?branch=master)](https://travis-ci.org/uatach/configtools)
[![codecov](https://codecov.io/gh/uatach/configtools/branch/master/graph/badge.svg)](https://codecov.io/gh/uatach/configtools)

A simple configuration management library for Python.

## Simple Example

```python
from configtools.config import load

config = load({'answer': 42})

@config.inject
def think(answer):
    print(answer)

think()
```

## Installation

```bash
$ pip install -U git+https://github.com/uatach/configtools.git#egg=configtools
```
