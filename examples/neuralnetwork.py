# -*- coding: utf-8 -*-

import jaeger.searchspace as S

search = S.SearchSpace()
search.add('n_hidden', S.Uniform(10, 200, intify=True))
search.add('momentum', S.Uniform(0.0, 0.99))
search.add('step_rate', S.LogUniform(0.00001, 1))
search.add('transfer_function', S.OneOf(['tanh', 'sigmoid']))

for i in range(10):
    sample = search.draw()
    print 'number of hiddens:', sample['n_hidden']
    print 'transfer function:', sample['transfer_function']
    print 'momentum:', sample['momentum']
    print 'step rate:', sample['step_rate']
    print
