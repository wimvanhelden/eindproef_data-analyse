class StandardPeakIntegrator():
    interval_1 = [3,12]
    interval_2 = [13,50]

    def give_integrated_peaks(self, pandasseries):
        peak_1 = 0
        for index in range(self.interval_1[0],self.interval_1[1]):
            peak_1 += pandasseries[index]
        peak_2 = 0
        for index in range(self.interval_2[0],self.interval_2[1]):
            peak_2 += pandasseries[index]
        return peak_1, peak_2
    
spi = StandardPeakIntegrator()