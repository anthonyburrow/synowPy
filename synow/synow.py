from .physics.constants import *
from .features import ExpFeature, GaussFeature
from .features.Feature import profile_map
from .util.params import setup_params


_temp_run_script = 'runsynow_temp.sh'
_temp_synthetic_fn = 'temp.dat'


_default_params = {
    'synow_lines_path'     : '$HOME/synow/lines/',
    'kurucz_linelist_path' : '$HOME/synow/kurucz_lines/',
    'refdata_path'         : '$HOME/synow/src/',
    'spectrum_file'        : 'synthetic.dat',
    'vphot'                : 12000.0,
    'vmax'                 : 40000.0,
    'tbb'                  : 15000.0,
    'ea'                   : 4000.0,
    'eb'                   : 8000.0,
    'nlam'                 : 1000,
    'flambda'              : True,
    'taumin'               : 0.01,
    'grid'                 : 32,
    'zeta'                 : 1.0,
    'stspec'               : 3500.0,
    # 'numref'               : 1,
    'delta_v'              : 300.0,
    'debug_out'            : True,
    'do_locnorm'           : True,
}


class Synow:

    def __init__(self, *args, **kwargs):
        """Initialize the Synow model.

        Parameters
        ----------
        *args
        ----------
        **kwargs
        ----------
        params: dict
        """
        self._params = setup_params(_default_params, *args, **kwargs)
        self._features = []

        self._initialize()

    def add_feature(self, prof=0, *args, **kwargs):
        if isinstance(prof, str):
            prof = profile_map[prof]

        if prof == 0:
            feature = ExpFeature(synow_model=self, *args, **kwargs)
        elif prof == 1:
            feature = GaussFeature(synow_model=self, *args, **kwargs)

        self._features.append(feature)

    def summary(self):
        msg = ''

        for key, val in self._params.items():
            msg += f'{key} : {val}\n'

        if not self._features:
            print(msg)
            return

        msg += '\n'

        for feat in self._features:
            msg += ' | '.join([f'{key} : {val}'
                               for key, val in feat._params.items()])
            msg += '\n'

        print(msg)

    @property
    def params(self):
        return self._params

    @property
    def features(self):
        return self._features

    def _initialize(self):
        # print(hc)
        pass
