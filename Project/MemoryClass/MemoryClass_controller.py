import os
from..ExperimentData.ExperimentData_model import ExperimentData

class MemoryClassController():

    def get_list_file_adress_directory(self, location, only_files = True):
        if only_files == False:
            pass #finish this later... recursive function to dig through subdirectories
        else: 
            list_file_adress = []
            for path in os.listdir(location):
                # check if current path is a file
                if os.path.isfile(os.path.join(location, path)):
                      list_file_adress.append(location+path)
            #print(list_file_adress)
            return list_file_adress




    def get_from_directory(self, location):
        list_files = self.get_list_file_adress_directory(location)
        #add verification later...
        list_experimentdata = []
        for filename in list_files:
            ed = ExperimentData()
            ed.parse_from_file(filename)
            list_experimentdata.append(ed)
        return list_experimentdata


mmc = MemoryClassController()

