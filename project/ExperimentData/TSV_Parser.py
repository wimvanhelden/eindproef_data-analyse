import pandas as pd
from ..IonData.IonData_model import IonData
#from ExperimentData_model import ExperimentData


class TSV_Standard_Parser():
    _fileLocation = None  #string holding the filelocation of the CSV file
    _skiprows = 7  # integer value marking where which line the data starts in the file
    _list_names_non_ION_series = ["index", "time (ms)"]

    """
    def get_datasource(self, filename):
        
        #file_content = open('../input/test1.txt',"r")
        #print(file_content.getlines())
        

        with open(filename) as f:
            lines = f.readlines()
            print(lines[8])
    """

    def get_dataframe(self, file_name_location):
        #add: check if file_name_location exists
        try:
            df = pd.read_table(file_name_location, skiprows=self._skiprows)
            return df
        except Exception as e:
            print("error in parsing TSV")
            print(e)
            return None

    def get_seriesTimeValues(self, dataframe):
        try:
            series = dataframe['time (ms)']
            return series
        except Exception as e:
            print("problem getting seriesTimeValues from dataframe")
            print(e)
            return None
        
    def get_listIonData(self, dataframe):
        try: 
            all_columnnames = dataframe.columns
            listIonData = []
            for columnname in all_columnnames:
                
                if columnname not in self._list_names_non_ION_series:
                    id = IonData()
                    id.seriesIon = dataframe[columnname]
                    id.name = columnname
                    listIonData.append(id)
                
            return listIonData
        except Exception as e:
            print("problem getting listIonData from dataframe")
            print(e)
            return None

          
    #function for getting a pandas data set from csv
    def read_data(filename:str, relative_location:str="./input", skiprows:int=7):
        try: 
            build_file_location=relative_location + "/" + filename
            df = pd.read_table('../input/test1.txt', skiprows=7)
            return(df)
        except Exception as e:
            print(e)
            return None
    

#DEBUG REMOVE LATER
if __name__ == "__main__":
    """
    tsp = TSV_Standard_Parser()
    filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/input/test1.txt"
    df = tsp.get_dataframe(filename)
    #list_ion = tsp.get_listIonData(df)
    
    #tsp.get_listIonData(df)
    list_ion_data = tsp.get_listIonData(df)
    #print(list_ion_data[5])
    """
