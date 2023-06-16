import unittest
import pandas as pd
from Project.IonData.IonData_model import IonData

class TestIonData(unittest.TestCase):
    
    def setUp(self):
        
        #test series made with data from Eseries_90cm_20µm_gel1_1%
        #for seriesIon: data from "[23Na]+ mass 22.9892"
        list_ion = [0.0444911, 0.0514376 ,0.0493114 ,0.049905 ,0.0521619 ,0.631607, 0.302822 ,0.0588857
                    ,0.0502117 ,0.0527633 ,0.050867 ,0.044715 ,0.0491617 ,0.0489509 ,0.0500744 ,0.0491243
                    ,0.048312 ,0.0427195 ,0.0449357 ,0.0469804 ,0.051647 ,0.0509655 ,0.0434169 ,0.0500304
                    ,0.0506418 ,0.052477 ,0.0476068 ,0.0479653 ,0.046524 ,0.043627 ,0.0513568 ,0.0524744
                    ,0.0511802 ,0.0479725 ,0.0503535 ,0.0546912 ,0.0525598 ,0.0505761 ,0.0505288 ,0.0511171
                    ,0.0465437 ,0.0511257 ,0.0513404 ,0.0490284 ,0.0491236 ,0.047616 ,0.0477099 ,0.0482772
                    ,0.046943 ,0.0503384 ,0.0480967 ,0.0541192 ,0.0529176 ,0.0506555 ,0.0456501 ,0.0450624
                    ,0.0510567 ,0.0494729 ,0.0519694 ,0.0474 ,0.0492825 ,0.0515538 ,0.0507291 ,0.0441398
                        ,0.0454859 ,0.0541199 ,0.0503259]
        s_ion = pd.Series(list_ion)
        
        #for seriesCPS: data from [28Si]+ mass 27.9764
        list_cps = [0.26464, 0.270797, 0.276592, 0.254742, 0.273474, 0.269443, 0.262013, 0.262739, 0.271598, 
                    0.267033, 0.270511, 0.265419, 0.264694, 0.266519, 0.263695, 0.260264, 0.256888, 0.26269, 
                    0.25112, 0.268038, 0.264865, 0.27635, 0.254926, 0.266371, 0.271427, 0.258711, 0.257498, 
                    0.263884, 0.262353, 0.255138, 0.244899, 0.264224, 0.260874, 0.262581, 0.264986, 0.258367, 
                    0.271394, 0.261895, 0.272336, 0.281593, 0.274851, 0.267987, 0.260728, 0.271342, 0.260819, 
                    0.269233, 0.254813, 0.269756, 0.260222, 0.26628, 0.258333, 0.267586, 0.266648, 0.25557, 
                    0.262618, 0.270135, 0.25721, 0.251431, 0.267538, 0.256127, 0.25118, 0.27183, 0.259401, 
                    0.263422, 0.254016, 0.260476, 0.268058]
        s_CPS = pd.Series(list_ion)

        #for seriesCorrctedBackground:: data from [27Al]+ 
        list_cb = [8.070456522, 5.929282609, -7.845630435, 13.75171739, 12.7525869, 36.4195434, 8.29884782, 
                1.41852173,4.473282609, 2.631869565, -2.54978260, -1.265086957, 7.29963043, 16.4782391, 
                2.446304348, 0.64769565, 14.07997826, 5.94354347, -5.90430434, 7.970521739, 3.773826087,
                 -4.748065217, -1.95026087, 20.38932609, 3.020847826, -11.98523913, 8.19106522, -11.9852391, 
                14.23715217, 5.4867608, 22.34497826, 0.64769565, 10.7112826, 4.287717391, 2.5605, 11.639108, 
                -3.449086957, 0.40504347, -0.47997826, 7.02841304, 4.773043478 , 0.212413043, -11.9852391, 
                -5.090652174, 7.52802173, 37.4758478, 8.29884782,5.31547826, 9.88323913, 1.36143478, 
                -6.675108696, 8.69854347, -0.165934783, 8.441586957, -3.092217391, -2.3927608, -1.807521739, 8.94119565, 
                -0.165934783, 0.471695652, -11.9852391, -1.736130435, 2.07515217, -4.662413043, 0.43358695, 
                -2.592608696 ,4.359086957]
        s_cb = pd.Series(list_cb)


        
        #assign to test instance:
        self.t_ion = IonData()
        self.t_ion.seriesIon = s_ion
        self.t_ion.seriesCPS = s_CPS
        self.t_ion.seriesCorrectedBackground = s_cb
                

        
    @classmethod
    def tearDownClass(cls):
        pass

    def test_set_seriesCPS(self):

        self.t_ion.set_seriesCPS()
        self.assertEqual(self.t_ion.seriesCPS[0],  967.1978260869565)
        self.assertEqual(self.t_ion.seriesCPS[10],  1105.804347826087)
        
        self.t_ion.seriesIon[0]=0.005
        self.t_ion.set_seriesCPS()
        self.assertEqual(self.t_ion.seriesCPS[0],  108.69565217391305)

    def test_set_seriesCorrectedBackground(self):
        self.t_ion.set_seriesCorrectedBackground()
        self.assertEqual(self.t_ion.seriesCorrectedBackground[0],   -0.0042125571428571346)
        self.assertEqual(self.t_ion.seriesCorrectedBackground[10],  0.0021633428571428692)
        
        self.t_ion.seriesCPS[0]=9000
        self.t_ion.set_seriesCorrectedBackground()
        self.assertEqual(self.t_ion.seriesCorrectedBackground[0],  8357.097331421428)

    def test_set_peak_signals(self):
        self.t_ion.set_peak_signals()
        self.assertEqual(self.t_ion.integratedPeakSignal1, 75.931499857)
        self.assertEqual(self.t_ion.integratedPeakSignal2,   179.56026006399998)
        self.assertEqual(self.t_ion.totalIntegratedSignal,    255.49175992099998)

    def test_updateTotalIntegratedSignal(self):
        self.t_ion.integratedPeakSignal1 = 2.5
        self.t_ion.integratedPeakSignal2 = 3
        self.t_ion.updateTotalIntegratedSignal()
        self.assertEqual(self.t_ion.totalIntegratedSignal, 5.5)

        self.t_ion.integratedPeakSignal2 = 0
        self.assertEqual(self.t_ion.totalIntegratedSignal, 2.5)

        self.t_ion.integratedPeakSignal2 = None
        self.assertEqual(self.t_ion.totalIntegratedSignal, 2.5)




if __name__ == '__main__':
    unittest.main()