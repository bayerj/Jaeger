# -*- coding: utf-8 -*-


import scipy



class Uniform(object):

    def __init__(self, lower, upper):
        self.size = 1
        self.lower = lower
        self.upper = upper

    def draw(self, seed):
        # Pick only the first entry.
        seed = seed[0]
        scale = self.upper - self.lower
        return seed * scale + self.lower


class LogUniform(object):

    def __init__(self, lower, upper):
        self.size = 1
        self.lower = lower
        self.upper = upper
        self.uniform = Uniform(scipy.log(lower), scipy.log(upper))

    def draw(self, seed):
        return scipy.exp(self.uniform.draw(seed))


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
            seeds = scipy.random.random(n_seeds)
        seeds = scipy.asarray(seeds)
        if seeds.shape[0] != n_seeds:
            raise ValueError('wrong dimension of seed')

        start = 0
        sample = {}
        for handle, v in self.variables:
            stop = start + v.size
            sample[handle] = v.draw(seeds[start:stop])
            start = stop
        return sample
