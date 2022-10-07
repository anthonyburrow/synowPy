from .features import ExpFeature, GaussFeature
from .features.Feature import profile_map
from .util.params import setup_params
from .cython.initialize import initialize
from .cython.continuum import setup_continuum


_synow_dir = 'C:/dev/synowPy'

_temp_run_script = './runsynow_temp.sh'
_temp_synthetic_fn = './temp.dat'


_default_params = {
    'synow_lines_path'     : f'{_synow_dir}/lines/',
    'kurucz_linelist_path' : f'{_synow_dir}/kurucz_lines/',
    'refdata_path'         : f'{_synow_dir}/src_orig/',
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

    def __init__(self, nradstep=10000, nwavestep=1024, *args, **kwargs):
        """Initialize the Synow model.

        Parameters
        ----------
        *args
        ----------
        **kwargs
        ----------
        params: dict
        """
        self.params = setup_params(_default_params, *args, **kwargs)
        self.features = []

        self.nradstep = nradstep
        self._nwavestep = nwavestep

        self._taux = None

    def add_feature(self, prof=0, *args, **kwargs):
        if isinstance(prof, str):
            prof = profile_map[prof]

        if prof == 0:
            feature = ExpFeature(synow_model=self, *args, **kwargs)
        elif prof == 1:
            feature = GaussFeature(synow_model=self, *args, **kwargs)

        self.features.append(feature)

    def gen_spectrum(self, output=False, *args, **kwargs):
        initialize(self)
        setup_continuum(self)

    def summary(self):
        msg = ''

        for key, val in self.params.items():
            msg += f'{key} : {val}\n'

        if not self.features:
            print(msg)
            return

        msg += '\n'

        for feat in self.features:
            msg += ' | '.join([f'{key} : {val}'
                               for key, val in feat._params.items()])
            msg += '\n'

        print(msg)

    @property
    def n_feat(self):
        return len(self._features)
