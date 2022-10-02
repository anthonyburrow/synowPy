import numpy as np

from ..physics.constants import *
from ..io.read_atomic import read_ref
from ..features.Feature import profile_map


def _setup_radial(feature, synow_model):
    grid = synow_model.params['grid']
    delta_v = synow_model.params['delta_v']
    vphot = synow_model.params['vphot']
    vmax = synow_model.params['vmax']
    tbb = synow_model.params['tbb']
    zeta = synow_model.params['zeta']

    onepvdc = 1. + delta_v / c
    rmax = vmax / vphot
    jrlim = int(rmax * grid + 0.5)

    if feature.vmine <= vphot * onepvdc:
        begin = grid
        wzone = 0.5
        feature.vmine = vphot
    else:
        begin = int(1.5 + grid * feature.vmine / vphot)
        begin = min(begin, jrlim) - 1
        wzone = 0.5 * (1. - np.sqrt(1. - (vphot / feature.vmine)**2))

    stop = int(1.5 + grid * feature.vmaxe / vphot)
    stop = min(stop, jrlim)

    # Setup optical depth profiles & anticorrect for stimulated emission
    feature.taux = np.zeros(synow_model.nradstep)

    wk = 1. + (np.exp(1. / (tbb * feature.elamx)) - 1.) / (wzone * zeta**2)
    wk = 1. - 1. / wk

    # tauxold = feature.taux[0]
    feature.taux[0] = feature.tau1 / wk
    feature.taux[1] = feature.temp * 1000. * k

    rad_steps = np.linspace(begin, stop - 1, stop - begin)
    if feature.prof == profile_map['p']:
        # TODO: Check this because it seems like a bug (xsto cancels in orig)
        # xsto = max(1., vphot / feature.vmine)
        # tau = (xsto * (i - 1))**(-feature.pwrlawin) * (xsto * (begin - 1))**feature.pwrlawin
        tau = ((begin - 1.) / (rad_steps - 1.))**feature.pwrlawin
    elif feature.prof == profile_map['g']:
        f = (rad_steps - 1.) / grid
        tau = np.exp(-0.5 * (feature.vmaxg - vphot * f)**2 / feature.sigma_v**2)
    elif feature.prof == profile_map['e']:
        f = (rad_steps - 1.) / grid
        tau = np.exp((feature.vmine - vphot * f) / feature.ve)

    feature.taux[begin:stop] = feature.taux[0] * tau
    # TODO: Write to file command

    # feature.taux[0] += tauxold


def initialize(synow_model):
    # Consolidate with ref.dat
    ref_data = read_ref(synow_model)
    ref_data['alam'] *= 10.
    ref_data['agf'] *= np.log(10.)

    taumin = synow_model.params['taumin']
    synow_model.features = [f for f in synow_model.features
                            if f.tau1 < 0.0001 * taumin]

    for feature in synow_model.features:
        mask = (ref_data['an'] == feature.an) & (ref_data['ai'] == feature.ai)
        if not np.any(mask):
            # TODO: Error handling
            print(f'Ion {feature.an} - {feature.ai} has no reference in ref.dat')
            feature.valid = False
            continue

        feature.elamx = ref_data[mask]['alam']
        feature.gfx = ref_data[mask]['agf']
        feature.chix = ref_data[mask]['aelow']

        if feature.elamx < 1000.:
            print(f'Ion {feature.an} - {feature.ai} has no reference in ref.dat')
            feature.valid = False
            continue

    synow_model.features = [f for f in synow_model.features if f.valid]

    # Setup profiles
    synow_model.params['tbb'] = synow_model.params['tbb'] * k / hc

    for feature in synow_model.features:
        _setup_radial(feature, synow_model)

    n_feat = len(synow_model.features)
    print(f'Initialization complete for {n_feat} species')

    # Synow does this...but what's the point?
    # for feature in synow_model.features:
    #     feature.tau1 = 0.
