
from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.ExperimentData.TSV_Parser import TSV_Standard_Parser

if __name__ == "__main__":
    filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/15h33m42s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average.txt"
    
    ed = ExperimentData()
    ed.parse_from_file(filename)
    print(ed.listIonData[12].seriesCPS)
    print(ed.listIonData[12].seriesCorrectedBackground)
    ed.set_all_seriesCPS()
    ed.set_all_seriesCorrectedBackground()
    print(ed.listIonData[12].seriesCPS)
    print(ed.listIonData[12].seriesCorrectedBackground)
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
