
from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.ExperimentData.TSV_Parser import TSV_Standard_Parser
from Project.MemoryClass.MemoryClass_controller import mmc
from Project.MemoryClass.MemoryClass_model import MemoryClass

if __name__ == "__main__":
    filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/15h33m42s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average.txt"
    """
    ed = ExperimentData()
    ed.parse_from_file(filename)
    print(ed.listIonData[12].seriesCPS)
    print(ed.listIonData[12].seriesCorrectedBackground)
    ed.set_all_seriesCPS()
    ed.set_all_seriesCorrectedBackground()
    print(ed.listIonData[12].seriesCPS)
    print(ed.listIonData[12].seriesCorrectedBackground)
    """
    """
    print(ed.fluency)
    print(ed.listIonData[12])
    print(ed.listIonData[12].seriesIon)
    print(ed.listIonData[12].seriesCPS)
    ed.listIonData[12].set_seriesCPS()
    print(ed.listIonData[12].seriesCPS)
    print(ed.listIonData[12].seriesCorrectedBackground)
    ed.listIonData[12].set_seriesCorrectedBackground()
    print(ed.listIonData[12].seriesCorrectedBackground)
    """
    #testing out the memoryclass
    directory = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/"
    #test = mmc.get_list_file_adress_directory(directory)
    mc = MemoryClass()
    mc.load_from_directory(directory)
    mc.set_all_seriesCorrectedBackground()
    #print(mc.listExperimentData[2].listIonData[10].seriesIon)
    print(mc.listExperimentData[2].listIonData[10].seriesCorrectedBackground)
    mc.set_all_peak_signals()
    print(mc.listExperimentData[2].listIonData[10].integratedPeakSignal1)

