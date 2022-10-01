import numpy as np


# n_elem = 92
# n_ion = 5


def read_ref(synow_model):
    dt = [('alam', np.float64), ('agf', np.float64), ('an', int), ('ai', int),
          ('aelow', np.float64)]
    fn = f'{synow_model.params["refdata_path"]}/ref.dat'

    return np.loadtxt(fn, dtype=dt)

    # alam *= 10.
    # agf *= np.log(10.)

    # elamx = np.zeros((n_elem, n_ion))
    # gfx = np.zeros((n_elem, n_ion))
    # chix = np.zeros((n_elem, n_ion))

    # for i in range(len(an)):
    #     j, k = int(an[i] - 1), int(ai[i])

    #     elamx[j, k] = alam[i]
    #     gfx[j, k] = agf[i]
    #     chix[j, k] = aelow[i]

    # return elamx, gfx, chix
