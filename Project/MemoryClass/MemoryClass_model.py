from .MemoryClass_controller import mmc

class MemoryClass():
    _list_ExperimentData = []  #central list of this class. Hold all the data in memory
    controller = mmc  #set controller to default 

    @property
    def listExperimentData(self):
        return self._listExperimentData
    
    @listExperimentData.setter
    def listExperimentData(self, value):
        self._listExperimentData = value

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



    