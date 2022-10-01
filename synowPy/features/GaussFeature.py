from .Feature import Feature, profile_map


class GaussFeature(Feature):

    def __init__(self, sigma_v=2.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['sigma_v'] = sigma_v
        self.prof = profile_map['g']

        # Scale parameters
        self._params['sigma_v'] *= 1000.
