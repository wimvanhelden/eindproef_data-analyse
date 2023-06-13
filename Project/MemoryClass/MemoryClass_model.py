from .MemoryClass_controller import mmc
from .MemoryClass_viewer import mcv

class MemoryClass():
    _listExperimentData = []  #central list of this class. Hold all the data in memory
    _listIonNames = []
    _listGelatinNames = []
    _listEset = []
    controller = mmc  #set controller to default 
    _dictIonGelPeak = {}
    viewer = mcv  #set the viewer to instance of standard mcv

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

    @property
    def listEset(self):
        return self._listEset
    
    @listEset.setter
    def listEset(self, value):
        self._listEset = value



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

    def set_ionnames_gels_peakdata_Eset(self):
        self.set_all_seriesCPS()
        self.set_all_seriesCorrectedBackground()
        self.set_all_peak_signals()

        #loop over all experimentdata's 
        #put all IonNames (f.e. "[23Na]+ mmass 14.0025)" in list_IonNames
        #put all Gelnames (f.e. "gel1" in list_gelNames)
        #check if peak values are calculated, if not: calculate
        for Experimentdata in self.listExperimentData:
            if Experimentdata.gelatinName not in self.listGelatinNames:
                self.listGelatinNames.append(Experimentdata.gelatinName)
            if Experimentdata.E_setpoint_procent not in self.listEset:
                self.listEset.append(Experimentdata.E_setpoint_procent)
            for Iondata in Experimentdata.listIonData:
                if Iondata.name not in self.listIonNames:
                    self.listIonNames.append(Iondata.name)
                if Iondata.totalIntegratedSignal is None:
                    Iondata.set_peak_signals()
        #sort the list of gelatinnames alpahbetically:            
        self.listGelatinNames.sort()
        self.listEset.sort()

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

    def calculate_gel_per_ionname(self):
        for experimentdata in self.listExperimentData:
            for iondata in experimentdata.listIonData:
                self.dictIonGelPeak[iondata.name]["GelTotal"][experimentdata.gelatinName] += iondata.totalIntegratedSignal

        for ionname in self.dictIonGelPeak:
            self.dictIonGelPeak[ionname]["BestGel"] = max(self.dictIonGelPeak[ionname]["GelTotal"], key=self.dictIonGelPeak[ionname]["GelTotal"].get)

        
    def set_IonOfEset_dict(self):
        for ionname in self.listIonNames:
            self.dictIonGelPeak[ionname]["IonOfEset"] = {}
            gelchosen = self.dictIonGelPeak[ionname]["BestGel"]
            for Eset in self.listEset:
                for experimentdata in self.listExperimentData:
                    if experimentdata.gelatinName == gelchosen and experimentdata.E_setpoint_procent == Eset:
                        for iondata in experimentdata.listIonData:
                            if iondata.name == ionname:
                                self.dictIonGelPeak[ionname]["IonOfEset"][Eset] = iondata
                                break

    def make_excel(self):
        self.initialise_dictIonGelPeak()
        self.calculate_gel_per_ionname()
        self.set_IonOfEset_dict()
        mcv.create_excel(self.listIonNames, self.dictIonGelPeak)



        

    
mc = MemoryClass()







    