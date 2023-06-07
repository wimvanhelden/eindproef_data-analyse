
from .BackgroundCorrectingSettings import BackGroundCorrectingSettings
from .IonData_controller import idc
from .StandardPeakIntegrator import spi

class IonData(): #class build around one Ion readout from an experiment
    _name = ""  #string that hold the name of the ion, as outputted by massaspectrometer, for example: [63Cu]+
    _seriesIon = None  #pandas series holding the numbers of ions per extraction (same as CSV output of massaspectrometer)
    _seriesCPS = None  #pandas series that facors in extraction rate. seriesIon *(1000000/46)(number of of ions per extraction multiplied by 1 extraction per 46 microseconds). 
    _seriesCorrectedBackground = None  #seriesCPS where the background (= average of non-peak-areas) is filtered out. = seriesCPS - average value of non-peak range(s)
    _integratedPeakSignal1 = None  #integrated signal of the first peak (sum of values from seriesCorrectedBackground)
    _integratedPeakSignal2 = None #integrated signal of the second peak (sum of values from seriesCorrectedBackground)
    _totalIntegratedSignal = None  # sum of IntegratedPeakSignals
    bgcs = BackGroundCorrectingSettings()  #class holding the settings used for correcting for background "noise"
    idc = idc  #set the iondatacontroller
    _extraction_rate = 46 #number of milliseconds per extraction, used to calculate seriesCPS
    peak_integrator = spi  #set peak integrator helper class to the standard peak integrator


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
        #use the setter to also update the total integrated value:
        self.updateTotalIntegratedSignal()

    @property
    def integratedPeakSignal2(self):
        return self._integratedPeakSignal2
        
    @integratedPeakSignal2.setter
    def integratedPeakSignal2(self, value):
        self._integratedPeakSignal2 = value
        #use the setter to also update the total integrated value:
        self.updateTotalIntegratedSignal()

    @property
    def totalIntegratedSignal(self):
        return self._totalIntegratedSignal
    
    @totalIntegratedSignal.setter
    def totalIntegratedSignal(self, value):
        self._totalIntegratedSignal = value

    def set_seriesCPS(self):
        self.seriesCPS = self.idc.get_seriesCPS(self.seriesIon, self._extraction_rate)

    def set_seriesCorrectedBackground(self):
        #check that seriesCPS is calculated: 
        if self.seriesCPS is None:
            self.set_seriesCPS()
        self.seriesCorrectedBackground = self.idc.get_seriesCorrectedForBackground(self.seriesCPS, self.bgcs)

    def set_peak_signals(self):
        #check that seriesCorrectedBackground is calculated: 
        if self.seriesCorrectedBackground is None:
            self.set_seriesCorrectedBackground()
        self.integratedPeakSignal1, self.integratedPeakSignal2 = spi.give_integrated_peaks(self.seriesCorrectedBackground)
        self.updateTotalIntegratedSignal()

    def updateTotalIntegratedSignal(self):
        total_signal = 0
        if self.integratedPeakSignal1 is not None:
            total_signal += self.integratedPeakSignal1
        if self.integratedPeakSignal2 is not None:
            total_signal += self.integratedPeakSignal2
        self.totalIntegratedSignal = total_signal

    

    

