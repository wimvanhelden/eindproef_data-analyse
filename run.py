
from Project.ExperimentData.ExperimentData_model import ExperimentData
from Project.ExperimentData.TSV_Parser import TSV_Standard_Parser
from Project.MemoryClass.MemoryClass_controller import mmc
from Project.MemoryClass.MemoryClass_model import mc
from Project.ExperimentData.FilenameParser import FilenameParser
import tkinter
from tkinter import filedialog, StringVar

#TKINTER INITIATION + CONFIGURATION:
window = tkinter.Tk()
window.title("two phase analyser")
window.geometry('640x640')
window.configure(bg='#333333')

#declaring stringvar values to be used later in labels:
text_label_number_experiments = StringVar()
text_label_number_gels = StringVar()
text_status = StringVar()

def select_directory():
    """event handling function that first asks user to select a directory. Then loads all files from that directory and does first calculations.
    """
    #label_status is used to warn the user that the operation will take some time
    label_status.config(bg = "red")
    text_status.set("Please wait... Loading in progress...")

    #dialog for selecting a directory
    folder_selected = filedialog.askdirectory()

    try:
        #load all files into memoryclass (created experimentdata lists with iondata lists)
        mc.load_from_directory(folder_selected + "/")
        #first calculations for memoryclass
        mc.set_ionnames_gels_peakdata_Eset()
        #give user feedback and update label_status
        text_label_number_experiments.set(f"Number of experimentdata's succefully loaded: {len(mc.listExperimentData)}")
        text_label_number_gels.set(f"Number of gel's in dataset: {len(mc.listGelatinNames)}")
        text_status.set("")
    except:
        tkinter.messagebox.showerror("showerror", "could not read files from this directory")
        text_status.set("")


def create_excel():
    """event handling function to create the two-peak excel
    """
    #label_status is used to warn the user that the operation will take some time
    label_status.config(bg = "red")
    text_status.set("Please wait... Creating excel in progress...")
    window.update_idletasks()
    #check that there are experimentdatas loaded:
    if len(mc.listExperimentData) > 0:
        try:
            mc.make_excel()
            #give user feedback and update label_status
            tkinter.messagebox.showinfo("showinfo", "Excel succefully created!")
            text_status.set("")
        except:
            tkinter.messagebox.showerror("showerror", "error while creating excel!")
            text_status.set("")
    else:
        #give user feedback and update label_status
        tkinter.messagebox.showerror("showerror", "please load experiment data's before you make the excel!")
        text_status.set("")


#tkinter: initialise elements that will become widgets
label_status = tkinter.Label(window, textvariable=text_status)
btn_select_directory = tkinter.Button(window, text ="select directory", command=select_directory)
label_number_experiments = tkinter.Label(window, textvariable=text_label_number_experiments)
label_number_gels = tkinter.Label(window, textvariable=text_label_number_gels)
btn_create_excel = tkinter.Button(window, text ="create excel", command=create_excel)

#tkinter: set initial values for labels
text_status.set("")
text_label_number_experiments.set(f"Number of experimentdata's succefully loaded: {len(mc.listExperimentData)}")
text_label_number_gels.set(f"Number of experimentdata's succefully loaded: {len(mc.listGelatinNames)}")

#tkinter: create widgets in window
label_status.pack()
btn_select_directory.pack()
label_number_experiments.pack()
label_number_gels.pack()
btn_create_excel.pack()



if __name__ == "__main__":
    #tkinter: start window loop
    window.mainloop()


    