from .Feature import Feature, profile_map


class PowerFeature(Feature):

    def __init__(self, pwrlawin=2.0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._params['pwrlawin'] = pwrlawin
        self.prof = profile_map['p']

    def calc_tau(self, rad_steps, begin, *args, **kwargs):
        # TODO: Check this because it seems like a bug (xsto cancels in orig)
        # xsto = max(1., vphot / self.vmine)
        # tau = (xsto * (rad_steps - 1))**(-self.pwrlawin) \
        #     * (xsto * (begin - 1))**self.pwrlawin
        tau = ((begin - 1.) / (rad_steps - 1.))**self.pwrlawin
        return tau
