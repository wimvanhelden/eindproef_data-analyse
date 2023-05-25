
import pandas as pd
import numpy as np


class BackGroundCorrectingSettings():
    bool_calculate_automaticly = False  #set to true to calculate the non-peak intervals automaticly
    non_peak_intervals = [[0,2],[54,66]]
    

# initialise a setter
bgcs = BackGroundCorrectingSettings()


class IonData(): #class build around one Ion readout from an experiment
    _name = ""  #string that hold the name of the ion, as outputted by massaspectrometer, for example: [63Cu]+
    _seriesIon = None  #pandas series holding the numbers of ions per extraction (same as CSV output of massaspectrometer)
    _seriesCPS = None  #pandas series that facors in extraction rate. seriesIon *(1000000/46)(number of of ions per extraction multiplied by 1 extraction per 46 microseconds). 
    _seriesCorrectedBackground = None  #seriesCPS where the background (= average of non-peak-areas) is filtered out. = seriesCPS - average value of non-peak range(s)
    _integratedPeakSignal1 = None  #integrated signal of the first peak (sum of values from seriesCorrectedBackground)
    _integreatedPeakSignal2 = None #integrated signal of the second peak (sum of values from seriesCorrectedBackground)
    _totalIntegratedSignal = None  # sum of IntegratedPeakSignals
    bgcs = BackGroundCorrectingSettings()
    
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


    











#function for getting a pandas data set from csv
def read_data(filename:str, relative_location:str="./input", skiprows:int=7):
    try: 
        build_file_location=relative_location + "/" + filename
        df = pd.read_table('../input/test1.txt', skiprows=7)
        return(df)
    except Exception as e:
        print(e)
        return None
    
#get the pandas data set: 
df = read_data("test1.txt")

#get a series out of that data set
series = df['[127I]+ mass 126.904']



def getSeriesCorrectedForBackground(pandaseries, settings):
    #ADD LATER : set intervals automaticly, or use findpeaks
    #ADD later: try... except... , 
    #ADD later: 

    
    #add: check that there are intervals marked as background... 
    # set total_length and total_sum variables. average will be total_sum / total_length
    total_length = 0
    total_sum = 0
    #loop over all the intervals and calculate rolling sum and total length... 
    for interval in settings.non_peak_intervals:
        #check for logical interval values
        try: 
            if interval[0]<interval[1]:
                for index in range(interval[0], interval[1]):
                    total_sum += pandaseries[index]
                    total_length +=1
        except: 
            print(ValueError("valueerror in getSeriesCorrectedForBackground ... most likely the values in non_peak_intervals are not integers "))
    #calculate the average. average will return 0 if no calculation could be made (len interval is 0 or incorrect values)
    try:
        average = total_sum / total_length
    except: 

        average = 0
    #initialise new series
    new_series = pandaseries.copy()
    #detract the previously calculated average from every value in the new pandas series
    try:
        new_series -= average
    except: 
        raise ValueError("valueerror in getSeriesCorrectedForBackground ... could not detract background average from new pandas series ")

    print("old series:")
    print(pandaseries)
    print("new series")
    print(new_series)

    return new_series


#series_corrected = getSeriesCorrectedForBackground(series, BackGroundCorrectingSettings)

class TSV_Standard_Parser():
    _fileLocation = None  #string holding the filelocation of the CSV file
    _skiprows = 7  # integer value marking where which line the data starts in the file
    def get_datasource(self):
        
        #file_content = open('../input/test1.txt',"r")
        #print(file_content.getlines())
        
        with open('../input/test1.txt') as f:
            lines = f.readlines()
            print(lines[1])



"""
parser = CSV_Standard_Parser()
parser.get_datasource()    
"""    

"""
#return all filenames in a directory
import os
list_files = os.listdir("C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/project")
print(list_files)
"""

#parse properties (stringvalues) from filename
string_filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/project/15h25m19s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average" #DEVELOPMENT REMOVE LATER
list_string_filename_split = string_filename.split("/")
#get the last element from that list
string_filename = list_string_filename_split[len(list_string_filename_split)-1]
print(string_filename)
list_filename_split = string_filename.split("_")
print(list_filename_split)
#set index values for each property (the location of those strings in list_filename_split)
index_timestamp = 0
index_gelatinName = 1





