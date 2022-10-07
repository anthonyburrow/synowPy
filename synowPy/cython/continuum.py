import numpy as np

from ..physics.constants import *


def _blackbody(synow_model):
    print('Calling continuum function')

    tbb = synow_model.params['tbb']
    ea = synow_model.params['ea']
    eb = synow_model.params['eb']
    nlam = synow_model.params['nlam']

    lam_exp = np.arange(0., nlam) / (nlam - 1.)
    xplot = ea * (eb / ea)**lam_exp

    xsto = ea + eb
    bb = (xsto / xplot)**3 * \
         (np.exp(1. / (tbb * xsto)) - 1.) / (np.exp(1. / (tbb * xplot)) - 1.)

    return xplot, bb


def _theta(synow_model):
    ctheta = np.zeros((synow_model.nradstep, 21))

    rad = grid + 1
    step = np.arange(11)

    ctheta[rad, -1] = 0.5
    ctheta[rad, step] = 1.
    ctheta[rad, step + 10] = 0.05 - 0.1 * step


def setup_continuum(synow_model):
    grid = synow_model.params['grid']
    delta_v = synow_model.params['delta_v']
    vphot = synow_model.params['vphot']
    vmax = synow_model.params['vmax']
    ea = synow_model.params['ea']

    onepvdc = 1. + delta_v / c
    rmax = vmax / vphot
    jrlim = int(rmax * grid + 0.5)

    isto = int(np.log(ea / 900.) / np.log(onepvdc) / 256.)
    synow_model.params['ea'] = 900. * (onepvdc**256)**isto

    xplot, bb = _blackbody(synow_model)
