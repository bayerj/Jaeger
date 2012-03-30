# -*- coding: utf-8 -*-


import numpy as np


class Numeric(object):

    def __init__(self, intify=False):
        self.intify = intify

    def draw(self, seed):
        res = self._draw(seed)
        if self.intify:
            res = int(round(res))
        return res


class Uniform(Numeric):

    def __init__(self, lower, upper, intify=False):
        self.size = 1
        self.lower = lower
        self.upper = upper
        super(Uniform, self).__init__(intify)

    def _draw(self, seed):
        # Pick only the first entry.
        seed = seed[0]
        scale = self.upper - self.lower
        return seed * scale + self.lower


class LogUniform(Numeric):

    def __init__(self, lower, upper, intify=False):
        self.size = 1
        self.lower = lower
        self.upper = upper
        self.uniform = Uniform(np.log(lower), np.log(upper))
        super(LogUniform, self).__init__(intify)

    def _draw(self, seed):
        drawn = self.uniform.draw(seed)
        print 'idrew', drawn
        return np.exp(drawn)


class OneOf(object):

    def __init__(self, choices):
        self.size = len(choices)
        self.choices = choices

    def draw(self, seed):
        return self.choices[seed.argmax()]


class SearchSpace(object):

    def __init__(self):
        self.variables = []

    def add(self, handle, var):
        self.variables.append((handle, var))

    def draw(self, seeds=None):
        n_seeds = sum(i.size for _, i in self.variables)
        if seeds is None:
            seeds = np.random.random(n_seeds)
        seeds = np.asarray(seeds)
        if seeds.shape[0] != n_seeds:
            raise ValueError('wrong dimension of seed')

        start = 0
        sample = {}
        for handle, v in self.variables:
            stop = start + v.size
            sample[handle] = v.draw(seeds[start:stop])
            start = stop
        return sample
