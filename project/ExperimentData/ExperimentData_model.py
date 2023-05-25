from FilenameParser import FilenameParser


class ExperimentData(): #class build around the total (all of the ions) readout from an experiment
    _listIonData = []  #list holding all the IonData's for this experiment
    _seriesTimeValues = None #pandas series holding the time values (interval values) for an experiment
    _extractionRate = 1000000/46 #rate of 1 extraction per 46 microseconds
    _tubeLenght = None #length of the tube connecting laser and massaspectrometer, in cm. for example: 90cm
    _E_setpoint_procent = None  #percentage of laser power used. for example: 85%
    _fluency = None  #laser energy, per time per surface area, in [J/cm²]  . for example: 1.26 J/cm²
    _laserSpotDiameter = None  #surface of laser spot opening in µm (micrometer). For example: 20µm 
    _gelatinName = None  #string value containing info about which gelatin is used in the experiment
    _dataSource = None  #string holding the data source (filename+location) mentioned IN the CSV file (!= actual file location)
    _timestamp = None  #string holding timestamp of when the experiment happened. Normaly parsed from filename of experiment result txt




    @property
    def listIonData(self):
        return self._listIonData
    
    @listIonData.setter
    def listIonData(self, value):
        self._listIonData = value

    @property
    def seriesTimeValues(self):
        return self._seriesTimeValues
    
    @seriesTimeValues.setter
    def seriesTimeValues(self, value):
        self._seriesTimeValues = value

    @property
    def extractionRate(self):
        return self._extractionRate
    
    @extractionRate.setter
    def extractionRate(self, value):
        self._extractionRate = value

    @property
    def tubeLength(self):
        return self._tubeLenght
    
    @tubeLength.setter
    def tubeLengts(self, value):
        self._tubeLenght = value

    @property
    def E_setpoint_procent(self):
        return self._E_setpoint_procent
    
    @E_setpoint_procent.setter
    def E_setpoint_procent(self, value):
        self._E_setpoint_procent = value

    @property
    def fluency(self):
        return self._fluency
    
    @fluency.setter
    def fluency(self, value):
        self._fluency = value

    @property
    def laserSpotDiameter(self):
        return self._laserSpotDiameter
    
    @laserSpotDiameter.setter
    def laserSpotDiameter(self, value):
        self._laserSpotDiameter = value

    @property
    def gelatinName(self):
        return self._gelatinName
    
    @gelatinName.setter
    def gelatinName(self, value):
        self._gelatinName = value

    @property
    def datasource(self):
        return self._datasource
    
    @datasource.setter
    def datasource(self, value):
        self._datasource = value

    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    def parse_from_filename(self, filename):
        fnp = FilenameParser(filename)
        self.timestamp =fnp.give_timestamp()
        self.gelatinName = fnp.give_gelatinname()
        self.fluency = fnp.give_fluency()
        self.laserSpotDiameter = fnp.give_laser_spot_diameter()


#DEBUG REMOVE LATER
if __name__ == "__main__":
    ed = ExperimentData()
    filename = file_location = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/project/15h25m19s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average"
    ed.parse_from_filename(filename)
    print(ed.fluency)
    print(ed.timestamp)
    print(ed.gelatinName)
    print(ed.laserSpotDiameter)





    





