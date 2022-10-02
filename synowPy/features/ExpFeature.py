import numpy as np

from .Feature import Feature, profile_map


class ExpFeature(Feature):

    def __init__(self, ve=1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['ve'] = ve
        self.prof = profile_map['e']

        # Scale parameters
        self._params['ve'] *= 1000.

    def calc_tau(self, synow_model, rad_steps, *args, **kwargs):
        grid = synow_model.params['grid']
        vphot = synow_model.params['vphot']

        f = (rad_steps - 1.) / grid
        tau = np.exp((self.vmine - vphot * f) / self.ve)
        return tau
