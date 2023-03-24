import pandas as pd


class Experiment():
    _filename = None
    _result = pd.DataFrame
    _fluency = None  #energy/surface: J/cm²
    _tubing_length = None  #legth of the tube between laser and spectrometer. unit: cm
    _spot_size = None  #surface area of the laser beam. Unit: cm²


    
