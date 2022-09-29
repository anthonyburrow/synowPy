
def setup_params(defaults, *args, **kwargs):
    params = {}

    for key in defaults:
        if key in kwargs:
            params[key] = kwargs[key]
            continue
        params[key] = defaults[key]

    return params
