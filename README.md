Jaeger
------

Jaeger is a small package for performing random search on parameter spaces for
functions with a nice interface. I hope to extend it with Bayesian optimization
and distributed evaluation techniques.

The approach is that the user defines a function which all the parameters that
should vary as inputs. In the next step, he defines a search space consisting
of several random variables. She can then sample from that search space in order
to pass those parameters into the function of interest.

For an example, see examples/neuralnetwork.py.
