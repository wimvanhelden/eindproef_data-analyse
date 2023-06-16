import unittest
import pandas as pd

from Project.MemoryClass.MemoryClass_model import MemoryClass
from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.IonData.IonData_model import IonData
class TestExperimentData(unittest.TestCase):
    
    def setUp(self):
        self.t_mc = MemoryClass()
        self.test_folder = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/test_input/"
        self.t_mc.listExperimentData = []
        self.t_mc.load_from_directory(self.test_folder)

    @classmethod
    def tearDownClass(cls) -> None:
        #add a function to remove the excel that is created in the test
        return super().tearDownClass()

    """
    def test_load_from_directory(self):
        self.t_load = MemoryClass()
        self.t_load.load_from_directory(self.test_folder)

        self.assertEqual(len(self.t_load.listExperimentData),90)
        self.assertEqual(len(self.t_load.listExperimentData[5].listIonData),316)
        self.assertEqual(self.t_load.listExperimentData[5].listIonData[12].seriesIon[20], 1.1956)
        
    def test_set_all_seriesCPS(self):
        self.t_mc.set_all_seriesCPS()
        self.assertEqual(len(self.t_mc.listExperimentData[5].listIonData[10].seriesIon),
                         len(self.t_mc.listExperimentData[5].listIonData[10].seriesCPS))
        self.assertEqual(self.t_mc.listExperimentData[5].listIonData[10].seriesCPS[12],
                         37.32782608695652)
        
    def test_set_all_seriesCorrectedBackground(self):
        self.t_mc.set_all_seriesCorrectedBackground()
        self.assertEqual(len(self.t_mc.listExperimentData[5].listIonData[10].seriesIon),
                         len(self.t_mc.listExperimentData[5].listIonData[10].seriesCorrectedBackground))
        self.assertEqual(self.t_mc.listExperimentData[5].listIonData[10].seriesCorrectedBackground[12],
                         17.106938198757756)
        
    def test_set_all_peak_signals(self):
        self.t_mc.set_all_seriesCorrectedBackground()
        self.t_mc.set_all_peak_signals()
        self.assertEqual(self.t_mc.listExperimentData[5].listIonData[10].integratedPeakSignal1,
                         9.36190031055895)
        self.assertEqual(self.t_mc.listExperimentData[5].listIonData[10].integratedPeakSignal2,
                         43.72036552795011)
        self.assertEqual(self.t_mc.listExperimentData[5].listIonData[10].totalIntegratedSignal,
                         53.08226583850906)
    

    def test_set_ionnames_gels_peakdata_Eset(self):
        self.t_mc.set_ionnames_gels_peakdata_Eset()
        self.assertEqual(len(self.t_mc.listIonNames), 316)
        self.assertEqual(self.t_mc.listIonNames[5],"[12C]+ mass 11.9994")
        self.assertEqual(len(self.t_mc.listGelatinNames), 3)
        self.assertEqual(self.t_mc.listGelatinNames[2],"Gel3")
        self.assertEqual(len(self.t_mc.listEset), 30)
        self.assertEqual(self.t_mc.listEset[5],6)
    

    def test_initialise_dictIonGelPeak(self):
        self.t_mc.set_ionnames_gels_peakdata_Eset()
        self.t_mc.initialise_dictIonGelPeak()
        self.assertEqual(len(self.t_mc.dictIonGelPeak), 316)
        self.assertEqual(len(self.t_mc.dictIonGelPeak["[27Al]+ mass 26.981"]["GelTotal"]),3)
        self.assertEqual(self.t_mc.dictIonGelPeak["[23Na]+ mass 22.9892"]["GelTotal"]["Gel2"], 0)
        

    def test_calculate_gel_per_ionname(self):
        self.t_mc.set_ionnames_gels_peakdata_Eset()
        self.t_mc.initialise_dictIonGelPeak()
        self.t_mc.calculate_gel_per_ionname()
        self.assertEqual(self.t_mc.dictIonGelPeak["[23Na]+ mass 22.9892"]["GelTotal"]["Gel2"],8183507.000621119 )
        self.assertEqual(self.t_mc.dictIonGelPeak["[23Na]+ mass 22.9892"]["BestGel"],"Gel3")

    def test_set_IonOfEset_dict(self):
        self.t_mc.set_ionnames_gels_peakdata_Eset()
        self.t_mc.initialise_dictIonGelPeak()
        self.t_mc.calculate_gel_per_ionname()
        self.t_mc.set_IonOfEset_dict()
        self.assertEqual(len(self.t_mc.dictIonGelPeak["[23Na]+ mass 22.9892"]["IonOfEset"]),30)
        self.assertIsInstance(self.t_mc.dictIonGelPeak["[23Na]+ mass 22.9892"]["IonOfEset"][5],IonData)
    """
    def test_make_excel(self):
        self.t_mc.set_ionnames_gels_peakdata_Eset()
        self.t_mc.make_excel()

if __name__ == '__main__':
    unittest.main()