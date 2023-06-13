
from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.ExperimentData.TSV_Parser import TSV_Standard_Parser
from Project.MemoryClass.MemoryClass_controller import mmc
from Project.MemoryClass.MemoryClass_model import mc
from Project.ExperimentData.FilenameParser import FilenameParser
import tkinter
from tkinter import filedialog, StringVar

def select_directory():
    pass


window = tkinter.Tk()
window.title("two phase analyser")
window.geometry('640x640')
window.configure(bg='#333333')
text_label_number_experiments = StringVar()
text_label_number_gels = StringVar()
text_status = StringVar()

def select_directory():
    label_status.config(bg = "red")
    text_status.set("Please wait... Loading in progress...")
    folder_selected = filedialog.askdirectory()

    try:

        mc.load_from_directory(folder_selected + "/")
        mc.set_ionnames_gels_peakdata_Eset()
        
        text_label_number_experiments.set(f"Number of experimentdata's succefully loaded: {len(mc.listExperimentData)}")
        text_label_number_gels.set(f"Number of experimentdata's succefully loaded: {len(mc.listGelatinNames)}")
        text_status.set("")
    except:
        tkinter.messagebox.showerror("showerror", "could not read files from this directory")
        text_status.set("")


def create_excel():
    label_status.config(bg = "red")
    text_status.set("Please wait... Creating excel in progress...")
    window.update_idletasks()
    if len(mc.listExperimentData) > 0:
        try:
            mc.make_excel()
            tkinter.messagebox.showinfo("showinfo", "Excel succefully created!")
            text_status.set("")
        except:
            tkinter.messagebox.showerror("showerror", "error while creating excel!")
            text_status.set("")
    else:
        tkinter.messagebox.showerror("showerror", "please load experiment data's before you make the excel!")
        text_status.set("")







label_status = tkinter.Label(window, textvariable=text_status)
btn_select_directory = tkinter.Button(window, text ="select directory", command=select_directory)
label_number_experiments = tkinter.Label(window, textvariable=text_label_number_experiments)
label_number_gels = tkinter.Label(window, textvariable=text_label_number_gels)
btn_create_excel = tkinter.Button(window, text ="create excel", command=create_excel)

text_status.set("")
text_label_number_experiments.set(f"Number of experimentdata's succefully loaded: {len(mc.listExperimentData)}")
text_label_number_gels.set(f"Number of experimentdata's succefully loaded: {len(mc.listGelatinNames)}")

label_status.pack()
btn_select_directory.pack()
label_number_experiments.pack()
label_number_gels.pack()
btn_create_excel.pack()





#window.withdraw()
#folder_selected = filedialog.askdirectory()





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
    """
    """
    #testing new flenameparser:
    filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/15h25m19s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average_ESET-1.txt"
    fnp = FilenameParser()
    fnp.filename = filename
    print(fnp._list_filename_split)
    print(fnp.give_E_percent())
    """

    #testing out the memoryclass
    directory = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/"
    #test = mmc.get_list_file_adress_directory(directory)
    
    #mc.load_from_directory(directory)
    #mc.set_all_seriesCorrectedBackground()
    #print(mc.listExperimentData[2].listIonData[10].seriesIon)
    """
    print(mc.listExperimentData[2].listIonData[10].seriesCorrectedBackground)
    mc.set_all_peak_signals()
    print(mc.listExperimentData[2].listIonData[10].integratedPeakSignal1)
    print(len(mc.listExperimentData))
    """
    #mc.set_ionnames_gels_peakdata_Eset()
    """
    for experimentdata in mc.listExperimentData:
        print(f"{experimentdata.gelatinName} - {experimentdata.E_setpoint_procent}")
        for IonData in experimentdata.listIonData:
            print(f"{IonData.name} - {IonData.totalIntegratedSignal}")
    """
    
    #mc.initialise_dictIonGelPeak()
   # mc.calculate_gel_per_ionname()
    #mc.set_IonOfEset_dict()
    #print(mc.dictIonGelPeak)
    #print(mc.dictIonGelPeak["[6Li]+ mass 6.01546"]["IonOfEset"])
    #mc.make_excel()
    window.mainloop()


    