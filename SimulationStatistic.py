class SimulationStatistic:

    SimulationStates = {

        '2000': 0,
        '1000': 0,
        '2100': 0,
        '1001': 0,
        '2101': 0,
        '1011': 0,
        '1101': 0,
        '2111': 0,
        '0101': 0,
        '1X11': 0,
        '0X11': 0,
        '2011': 0,
        '1100': 0,
        '0100': 0,
        '1111': 0,
        '0111': 0,
        '2001': 0,

    }

    def __init__(self, A, K1, K2, Loch, Lc, Pbl):
        self.A = A
        self.K1 = K1
        self.K2 = K2
        self.Loch = Loch
        self.Lc = Lc
        self.L1 = 0
        self.Pbl = Pbl
        self.Potkz = 0
        self.Pblk = 0
        self.Wc = 0

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    @property
    def K1(self):
        return self._K1

    @property
    def K2(self):
        return self._K2

    @property
    def Loch(self):
        return self._Loch

    @K1.setter
    def K1(self, value):
        self._K1 = value

    @K2.setter
    def K2(self, value):
        self._K2 = value

    @Loch.setter
    def Loch(self, value):
        self._Loch = value

    @property
    def Pbl(self):
        return self._Pbl

    @property
    def Lc(self):
        return self._Lc

    @Lc.setter
    def Lc(self, value):
        self._Lc = value

    @Pbl.setter
    def Pbl(self, value):
        self._Pbl = value

    @property
    def Potkz(self):
        return self._Potkz

    @Potkz.setter
    def Potkz(self, value=0):
        self._Potkz = value

    @property
    def Woch(self):
        return self.Loch / self.A

    @property
    def Wc(self):
        return self._Wc

    @property
    def Q(self):
        return 1 - self.Potkz

    @property
    def Pblk(self):
        return self._Pblk

    @Pblk.setter
    def Pblk(self, value):
        self._Pblk = value

    @property
    def L1(self):
        return self._L1

    @L1.setter
    def L1(self, value):
        self._L1 = value

    @Wc.setter
    def Wc(self, value):
        self._Wc = value
