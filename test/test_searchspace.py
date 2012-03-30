# -*- coding: utf-8 -*-

import numpy as np

from jaeger.searchspace import Uniform, LogUniform, OneOf, SearchSpace


def test_uniform():
    x = Uniform(0, 1)
    seeds = np.random.random((1000, 1))
    draws = [x.draw(s) for s in seeds]
    assert all(0 <= i < 1 for i in draws)


def test_uniform_int():
    x = Uniform(0, 2, intify=True)
    seeds = np.random.random((1000, 1))
    draws = [x.draw(s) for s in seeds]
    assert all(i in (0, 1, 2) for i in draws)


def test_loguniform():
    x = LogUniform(1, 2)
    seeds = np.random.random((10, 1))
    draws = [x.draw(s) for s in seeds]
    print draws
    assert all(1 <= i < 2 for i in draws)


def test_loguniform_int():
    x = LogUniform(1, 2, intify=True)
    seeds = np.random.random((1000, 1))
    draws = [x.draw(s) for s in seeds]
    print draws
    assert all(i in (1, 2) for i in draws)
