import synowPy


global_params = {'tbb': 14000., 'vphot': 11000.}
syn = synowPy.Synow(**global_params)

feat_params = {'an': 10, 'ai': 0, 've': 2.}
syn.add_feature(prof='e', **feat_params)

feat_params = {'an': 9, 've': 2.}
syn.add_feature(prof='g', **feat_params)

syn.gen_spectrum(output=True)

syn.summary()
