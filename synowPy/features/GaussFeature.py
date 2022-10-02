import numpy as np

from .Feature import Feature, profile_map


class GaussFeature(Feature):

    def __init__(self, sigma_v=2.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['sigma_v'] = sigma_v
        self.prof = profile_map['g']

        # Scale parameters
        self._params['sigma_v'] *= 1000.

    def calc_tau(self, synow_model, rad_steps, *args, **kwargs):
        grid = synow_model.params['grid']
        vphot = synow_model.params['vphot']

        f = (rad_steps - 1.) / grid
        tau = np.exp(-0.5 * (self.vmaxg - vphot * f)**2 / self.sigma_v**2)
        return tau
