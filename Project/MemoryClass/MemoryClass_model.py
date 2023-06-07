from .MemoryClass_controller import mmc

class MemoryClass():
    _listExperimentData = []  #central list of this class. Hold all the data in memory
    _listIonNames = []
    _listGelatinNames = []
    controller = mmc  #set controller to default 
    _dictIonGelPeak = {}

    @property
    def listExperimentData(self):
        return self._listExperimentData
    
    @listExperimentData.setter
    def listExperimentData(self, value):
        self._listExperimentData = value

    @property
    def listIonNames(self):
        return self._listIonNames
    
    @listIonNames.setter
    def listIonNames(self, value):
        self._listIonNames = value

    @property
    def listGelatinNames(self):
        return self._listGelatinNames
    
    @listGelatinNames.setter
    def listGelatinNames(self, value):
        self._listGelatinNames = value

    @property
    def dictIonGelPeak(self):
        return self._dictIonGelPeak
    
    @dictIonGelPeak.setter
    def dictIonGelPeak(self, value):
        self._dictIonGelPeak = value



    def load_from_directory(self, location):
        self.listExperimentData = self.controller.get_from_directory(location)

    def set_all_seriesCPS(self):
        for experimentdata in self.listExperimentData:
            experimentdata.set_all_seriesCPS()

    def set_all_seriesCorrectedBackground(self):
        for experimentdata in self.listExperimentData:
            experimentdata.set_all_seriesCorrectedBackground()

    def set_all_peak_signals(self):
        for experimentdata in self.listExperimentData:
            experimentdata.set_all_peak_signals()

    def set_ionnames_gels_peakdata(self):
        #loop over all experimentdata's 
        #put all IonNames (f.e. "[23Na]+ mmass 14.0025)" in list_IonNames
        #put all Gelnames (f.e. "gel1" in list_gelNames)
        #check if peak values are calculated, if not: calculate
        for Experimentdata in self.listExperimentData:
            if Experimentdata.gelatinName not in self.listGelatinNames:
                self.listGelatinNames.append(Experimentdata.gelatinName)
            for Iondata in Experimentdata.listIonData:
                if Iondata.name not in self.listIonNames:
                    self.listIonNames.append(Iondata.name)
                if Iondata.totalIntegratedSignal is None:
                    Iondata.set_peak_signals()
        #sort the list of gelatinnames alpahbetically:            
        self.listGelatinNames.sort()

    def initialise_dictIonGelPeak(self):
        #clear dictIonGelpeak:
        self.dictIonGelPeak = {}
        #check if ionnames and gelnames are set
        if len(self.listGelatinNames) == 0 or len(self.listIonNames) == 0:
            raise Exception("error initialising dictIonGelPeak in memoryclass")
        #create a dictionary per Ionname. Key = Ionname, value = dictionary
        for IonName in self.listIonNames:
            self.dictIonGelPeak[IonName] = {}
            #in the "ionname" value (dict) create a subdictionary with key "GelTotal"
            self.dictIonGelPeak[IonName]["GelTotal"]={}
            for gelname in self.listGelatinNames:
                # in the "geltotal" value populate with a dictionary with gelnames as key and 0 as value
                # that 0 will be used as a rolling sum value later in the summation
                self.dictIonGelPeak[IonName]["GelTotal"][gelname] = 0

    def choose_gel_per_ionname(self):
        for experimentdata in self.listExperimentData:
            for iondata in experimentdata.listIonData:
                self.dictIonGelPeak[iondata.name]["GelTotal"][experimentdata.gelatinName] += iondata.totalIntegratedSignal

        for ionname in self.dictIonGelPeak:
            self.dictIonGelPeak[ionname]["BestGel"] = max(self.dictIonGelPeak[ionname]["GelTotal"], key=self.dictIonGelPeak[ionname]["GelTotal"].get)

        

    








    