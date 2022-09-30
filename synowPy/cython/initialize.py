import numpy as np

from ..physics.constants import *
from ..io.read_atomic import read_ref, n_elem, n_ion


def initialize(model):
    elamx, gfx, chix = read_ref(model)

    model._taux = np.zeros((n_elem, n_ion, model._nradstep))

    rmax = model.params['vmax'] / model.params['vphot']
    jrlim = int(rmax * model.params['grid'] + 0.5)
    model.params['tbb'] = model.params['tbb'] * k / hc

    # Setup radial profiles
    for feat in model.features:
        pass
