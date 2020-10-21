class Application:

    def __init__(self, ind, tic_quantity):
        self.ind = ind
        self.state = 0
        self.tic_quantity = tic_quantity

    @property
    def tic_quantity(self):
        return self._tic_quantity

    @tic_quantity.setter
    def tic_quantity(self, value):
        self._tic_quantity = value

    @property
    def ind(self):
        return self._ind

    @ind.setter
    def ind(self, value):
        self._ind = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


