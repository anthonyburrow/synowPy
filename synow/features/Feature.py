from ..util.params import setup_params


_default_params = {
    'an'       :   14,   # Si II as default
    'ai'       :    1,
    'tau1'     :  0.0,
    'vmine'    : None,
    'vmaxe'    : None,
    'vmaxg'    : 12.0,
    'temp'     : 10.0,
}

profile_map = {
    'e': 0,
    'g': 1
}


class Feature:

    def __init__(self, synow_model, *args, **kwargs):
        self._params = setup_params(_default_params, *args, **kwargs)

        # Special parameter defaults
        if 'vmine' not in kwargs:
            self._params['vmine'] = synow_model.params['vphot']
        if 'vmaxe' not in kwargs:
            self._params['vmaxe'] = synow_model.params['vmax']

    def __getattr__(self, attr):
        return self._params[attr]
