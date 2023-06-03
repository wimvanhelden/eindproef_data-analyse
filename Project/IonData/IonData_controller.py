
class IonDataController():
    def get_seriesCPS(self, seriesIon, samplerate):
        new_series = seriesIon.copy()
        seriesCPS = new_series*(1000000)/samplerate
        return seriesCPS
    
    def get_seriesCorrectedForBackground(self, seriesCPS, BackGroundCorrectingSettings):
            #add: check that there are intervals marked as background... 
        # set total_length and total_sum variables. average will be total_sum / total_length
        total_length = 0
        total_sum = 0
        #loop over all the intervals and calculate rolling sum and total length... 
        for interval in BackGroundCorrectingSettings.non_peak_intervals:
            #check for logical interval values
            try: 
                if interval[0]<interval[1]:
                    for index in range(interval[0], interval[1]):
                        total_sum += seriesCPS[index]
                        total_length +=1
            except: 
                raise ValueError("valueerror in getSeriesCorrectedForBackground ... most likely the values in non_peak_intervals are not integers ")
        #calculate the average. average will return 0 if no calculation could be made (len interval is 0 or incorrect values)
        try:
            average = total_sum / total_length
        except: 

            average = 0
        #initialise new series
        new_series = seriesCPS.copy()
        #detract the previously calculated average from every value in the new pandas series
        try:
            new_series -= average
        except: 
            raise ValueError("valueerror in getSeriesCorrectedForBackground ... could not detract background average from new pandas series ")
        
        return new_series
    

idc = IonDataController()  #singleton pattern
