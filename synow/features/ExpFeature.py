from .Feature import Feature


class ExpFeature(Feature):

    def __init__(self, ve=1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['ve'] = ve
