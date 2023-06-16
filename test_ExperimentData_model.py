import unittest
import pandas as pd

from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.IonData.IonData_model import IonData
class TestExperimentData(unittest.TestCase):
    
    def setUp(self):
        self.t_ed = ExperimentData()
        self.test_filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/test_input/09h46m01s_Gel3_Eseries_4mJ_20micron.h5__SegmentProfiles_Average_ESET-1.txt"
        self.t_ed.listIonData = []

    
    def test_parse_filename(self):
        
        test_filename = self.test_filename
        self.t_ed.parse_filename(test_filename)
        self.assertEqual(self.t_ed.name_parser.filename, "09h46m01s_Gel3_Eseries_4mJ_20micron.h5__SegmentProfiles_Average_ESET-1.txt")
        self.assertEqual(self.t_ed.timestamp, "09h46m01s")
        self.assertEqual(self.t_ed.gelatinName, "Gel3")
        self.assertEqual(self.t_ed.fluency, "4mJ")
        self.assertEqual(self.t_ed.laserSpotDiameter, "20micron")
        self.assertEqual(self.t_ed.E_setpoint_procent, 1 )

    def test_parse_TSV(self):
        self.t_ed.parse_TSV(self.test_filename)
        self.assertIsNotNone(self.t_ed.dataframe)
        self.assertEqual(self.t_ed.seriesTimeValues[3], 8.97)
        self.assertEqual(len(self.t_ed.seriesTimeValues), len(self.t_ed.listIonData[0].seriesIon))
        self.assertIsInstance(self.t_ed.listIonData[5], IonData)
        self.assertEqual(self.t_ed.listIonData[12].seriesIon[20],  1.19104)

    def test_parse_from_file(self):
        self.t_ed.parse_from_file(self.test_filename)       
        self.assertEqual(self.t_ed.name_parser.filename, "09h46m01s_Gel3_Eseries_4mJ_20micron.h5__SegmentProfiles_Average_ESET-1.txt")
        self.assertEqual(self.t_ed.timestamp, "09h46m01s")
        self.assertEqual(self.t_ed.gelatinName, "Gel3")
        self.assertEqual(self.t_ed.fluency, "4mJ")
        self.assertEqual(self.t_ed.laserSpotDiameter, "20micron")
        self.assertEqual(self.t_ed.E_setpoint_procent, 1 )
        self.assertIsNotNone(self.t_ed.dataframe)
        self.assertEqual(self.t_ed.seriesTimeValues[3], 8.97)
        self.assertEqual(len(self.t_ed.seriesTimeValues), len(self.t_ed.listIonData[0].seriesIon))
    
    def test_set_all_seriesCPS(self):
        series_muck_1 = pd.Series([5,8,9,6])
        series_muck_2 = pd.Series([8,2,0,-1])
        iondata_1 = IonData()
        iondata_2 = IonData()
        iondata_1.seriesIon = series_muck_1
        iondata_2.seriesIon = series_muck_2

        self.t_ed.listIonData.append(iondata_1)
        self.t_ed.listIonData.append(iondata_2)

        self.t_ed.set_all_seriesCPS()

        self.assertEqual(self.t_ed.listIonData[0].seriesCPS[2], 195652.1739130435)
        self.assertEqual(self.t_ed.listIonData[1].seriesCPS[2], 0)
    
    def test_set_all_seriesCorrectedBackground(self):
        
        list_muck_1 = []
        list_muck_2 = []
        for i in range(3):
            list_muck_1.append(5)
            list_muck_2.append(-10)
        for i in range(20):
            list_muck_1.append(0)
            list_muck_2.append(0)
        for i in range(80):
            list_muck_1.append(5)
            list_muck_2.append(-10)

        series_muck_1 = pd.Series(list_muck_1)
        series_muck_2 = pd.Series(list_muck_2)  

        id_1 = IonData()
        id_2 = IonData()

        id_1.seriesCPS = series_muck_1
        id_2.seriesCPS = series_muck_2
        
        self.t_ed.listIonData.append(id_1)
        self.t_ed.listIonData.append(id_2)

        self.t_ed._cps_set = True
        self.t_ed.set_all_seriesCorrectedBackground()
        self.assertEqual(self.t_ed.listIonData[0].seriesCorrectedBackground[1],0)
        self.assertEqual(self.t_ed.listIonData[0].seriesCorrectedBackground[5],-5)
        self.assertEqual(self.t_ed.listIonData[1].seriesCorrectedBackground[5],10)
        self.assertEqual(self.t_ed.listIonData[1].seriesCorrectedBackground[0],0)

    def test_set_all_peak_signals(self):
        list_muck_1 = []
        list_muck_2 = []
        for i in range(3):
            list_muck_1.append(5)
            list_muck_2.append(-10)
        for i in range(20):
            list_muck_1.append(1)
            list_muck_2.append(2)
        for i in range(80):
            list_muck_1.append(5)
            list_muck_2.append(-10)

        series_muck_1 = pd.Series(list_muck_1)
        series_muck_2 = pd.Series(list_muck_2)  

        id_1 = IonData()
        id_2 = IonData()

        id_1.seriesCorrectedBackground = series_muck_1
        id_2.seriesCorrectedBackground = series_muck_2
        
        self.t_ed.listIonData.append(id_1)
        self.t_ed.listIonData.append(id_2)

        self.t_ed.set_all_peak_signals()
        self.assertEqual(self.t_ed.listIonData[1].integratedPeakSignal2, -250)
        self.assertEqual(self.t_ed.listIonData[1].integratedPeakSignal1, 18)
        self.assertEqual(self.t_ed.listIonData[0].integratedPeakSignal1, 9)

        self.assertEqual(self.t_ed.listIonData[1].totalIntegratedSignal, -232)
if __name__ == '__main__':
    unittest.main()