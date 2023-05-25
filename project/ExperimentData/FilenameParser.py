class FilenameParser():
    #parse properties (stringvalues) from filename
    _index_timestamp = 0
    _index_gelatinName = 1
    _index_fluency = 3
    _index_laser_spot_diameter = 4
    #_string_filename = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/project/15h25m19s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average" #DEVELOPMENT REMOVE LATER
    _string_filename = None
    _seperator_symbol_1 = "/"
    _seperator_symbol_2 = "."
    

    def __init__(self, filename):
        self.filename = filename
        self.__list_string_filename_split = self.filename.split(self._seperator_symbol_1)
        #get the last element from that list
        self.__string_filename = self.__list_string_filename_split[len(self.__list_string_filename_split)-1]
        self.__list_filename_split = self.__string_filename.split("_")
        

    @property
    def filename(self):
        if self._string_filename is not None:
            return self._string_filename
        else:
            raise AttributeError("filename is not set in FilenameParser")
    
    @filename.setter
    def filename(self, value):
        if isinstance(value, str):
            self._string_filename = value
        else:
            raise ValueError("filename in FilenameParser can only be set to a string value")
        
#set index values for each property (the location of those strings in list_filename_split)
    def give_timestamp(self):
        return self.__list_filename_split[self._index_timestamp]
    
    def give_gelatinname(self):
        return self.__list_filename_split[self._index_gelatinName]
    
    def give_fluency(self):
        return self.__list_filename_split[self._index_fluency]
    
    def give_laser_spot_diameter(self):
        full_string = self.__list_filename_split[self._index_laser_spot_diameter]
        list_split = full_string.split(self._seperator_symbol_2)
        return list_split[0]
        



#DEBUG REMOVE LATER
if __name__ == "__main__":
    file_location = "C:/Users/wimva/Documents/GitHub/eindproef_data-analyse/project/15h25m19s_Gel1_Eseries_4mJ_20micron.h5__SegmentProfiles_Average"
    fp = FilenameParser(file_location)
    print(fp.give_timestamp())
    print(fp.give_gelatinname())
    print(fp.give_fluency())
    print(fp.give_laser_spot_diameter())

