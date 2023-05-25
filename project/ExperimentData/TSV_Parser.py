class TSV_Standard_Parser():
    _fileLocation = None  #string holding the filelocation of the CSV file
    _skiprows = 7  # integer value marking where which line the data starts in the file
    def get_datasource(self):
        
        #file_content = open('../input/test1.txt',"r")
        #print(file_content.getlines())
        
        with open('../input/test1.txt') as f:
            lines = f.readlines()
            print(lines[1])