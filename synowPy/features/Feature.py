from ..util.params import setup_params


_default_params = {
    'an'       :    1,
    'ai'       :    0,
    'tau1'     :  0.0,
    'vmine'    : None,
    'vmaxe'    : None,
    'vmaxg'    : 12.0,
    'temp'     : 10.0,
}

profile_map = {
    'e': 0,
    'g': 1,
    'p': 2
}


class Feature:

    def __init__(self, synow_model, *args, **kwargs):
        self._params = setup_params(_default_params, *args, **kwargs)

        # Special parameter defaults
        if 'vmine' not in kwargs:
            self._params['vmine'] = 0.001 * synow_model.params['vphot']
        if 'vmaxe' not in kwargs:
            self._params['vmaxe'] = 0.001 * synow_model.params['vmax']

        # Scale parameters
        self._params['vmine'] *= 1000.
        self._params['vmaxe'] *= 1000.
        self._params['vmaxg'] *= 1000.

        # Feature parameters
        self.elamx = None
        self.gfx = None
        self.chix = None

        self.tau = None

        # Misc
        self.valid = True

    def __getattr__(self, attr):
        return self._params[attr]
