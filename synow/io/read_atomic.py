import numpy as np


n_elem = 92
n_ion = 5


def read_ref(fn):
    alam, agf, an, ai, aelow = np.loadtxt(fn, unpack=True)

    elamx = np.zeros((n_elem, n_ion))
    gfx = np.zeros((n_elem, n_ion))
    chix = np.zeros((n_elem, n_ion))

    for i in range(len(an)):
        _an, _ai = an[i], ai[i]

        elamx[_an, _ai] = alam
        gfx[_an, _ai] = agf
        chix[_an, _ai] = aelow

    elamx *= 10.
    gfx *= np.log(10.)

    return elamx, gfx, chix
