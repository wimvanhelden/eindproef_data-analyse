
from BackgroundCorrectingSettings import BackGroundCorrectingSettings

class IonData(): #class build around one Ion readout from an experiment
    _name = ""  #string that hold the name of the ion, as outputted by massaspectrometer, for example: [63Cu]+
    _seriesIon = None  #pandas series holding the numbers of ions per extraction (same as CSV output of massaspectrometer)
    _seriesCPS = None  #pandas series that facors in extraction rate. seriesIon *(1000000/46)(number of of ions per extraction multiplied by 1 extraction per 46 microseconds). 
    _seriesCorrectedBackground = None  #seriesCPS where the background (= average of non-peak-areas) is filtered out. = seriesCPS - average value of non-peak range(s)
    _integratedPeakSignal1 = None  #integrated signal of the first peak (sum of values from seriesCorrectedBackground)
    _integreatedPeakSignal2 = None #integrated signal of the second peak (sum of values from seriesCorrectedBackground)
    _totalIntegratedSignal = None  # sum of IntegratedPeakSignals
    bgcs = BackGroundCorrectingSettings()  #class holding the settings used for correcting for background "noise"
    
    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def seriesIon(self):
        return self._seriesIon

    @seriesIon.setter
    def seriesIon(self, value):
        self._seriesIon = value

    @property
    def seriesCPS(self):
        return self._seriesCPS

    @seriesCPS.setter
    def seriesCPS(self, value):
        self._seriesCPS = value

    @property
    def seriesCorrectedBackground(self):
        return self._seriesCorrectedBackground

    @seriesCorrectedBackground.setter
    def seriesCorrectedBackground(self, value):
        self._seriesCorrectedBackground = value

    @property
    def integratedPeakSignal1(self):
        return self._integratedPeakSignal1
    
    @integratedPeakSignal1.setter
    def integratedPeakSignal1(self, value):
        self._integratedPeakSignal1 = value

    @property
    def integratedPeakSignal2(self):
        return self._integratedPeakSignal2
    
    @integratedPeakSignal2.setter
    def integratedPeakSignal2(self, value):
        self._integratedPeakSignal2 = value

    @property
    def totalIntegratedSignal(self):
        return self._totalIntegratedSignal
    
    @totalIntegratedSignal.setter
    def totalIntegratedSignal(self, value):
        self._totalIntegratedSignal = value