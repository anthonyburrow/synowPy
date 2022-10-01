from .Feature import Feature, profile_map


class PowerFeature(Feature):

    def __init__(self, pwrlawin=2.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['pwrlawin'] = pwrlawin
        self.prof = profile_map['p']

