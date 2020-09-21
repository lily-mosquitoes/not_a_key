from .halving import halving_score
from .abundance import abundance_score


class Algorithms(object):
    def __init__(self):
        self.available_algorithms = {
            'fastest any': halving_score,
            'top percent': abundance_score,

        }
        self.use_percent = ['top percent', ]
