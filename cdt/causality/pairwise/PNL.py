# ToDo : Implement
from .model import PairwiseModel


class PNL(PairwiseModel):
    def __init__(self):
        super(PNL, self).__init__()

    def predict_proba(self, a, b):
        return 0
