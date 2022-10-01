import numpy as np

from ..physics.constants import *
from ..io.read_atomic import read_ref


def _setup_radial(feature):
    pass


def _setup_tau(feature):
    # model._taux = np.zeros(model._nradstep)

    pass


def initialize(model):
    # alam, agf, an, ai, aelow = read_ref(model)
    ref_data = read_ref(model)
    ref_data['alam'] *= 10.
    ref_data['agf'] *= np.log(10.)

    for feature in model.features:
        mask = (ref_data['an'] == feature.an) & (ref_data['ai'] == feature.ai)
        if not np.any(mask):
            print(f'Ion {feature.an} - {feature.ai} has no reference in ref.dat')
            continue

        feature.elamx = ref_data[mask]['alam']
        feature.gfx = ref_data[mask]['agf']
        feature.chix = ref_data[mask]['aelow']

    rmax = model.params['vmax'] / model.params['vphot']
    jrlim = int(rmax * model.params['grid'] + 0.5)
    model.params['tbb'] = model.params['tbb'] * k / hc

    # Setup radial profiles
    for feature in model.features:
        _setup_radial(feature)
        _setup_tau(feature)
