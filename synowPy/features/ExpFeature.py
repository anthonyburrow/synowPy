from .Feature import Feature, profile_map


class ExpFeature(Feature):

    def __init__(self, ve=1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['ve'] = ve
        self.prof = profile_map['e']

        # Scale parameters
        self._params['ve'] *= 1000.
