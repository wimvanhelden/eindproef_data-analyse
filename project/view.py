import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def read_data(filename:str, relative_location:str="./input", skiprows:int=7):
    try: 
        build_file_location=relative_location + "/" + filename
        df = pd.read_table('../input/test1.txt', skiprows=7)
        return(df)
    except Exception as e:
        print(e)
        return None

"""
df = read_data("test1.txt")
print(df)

#df.set_index('time (ms)')
#print(df)
#df.plot(y = '[127I]+ mass 126.904', x='time (ms)')
#plt.show()
"""

"""

#df_test1.plot(kind = 'scatter', x = 'time (ms)', y = '[127I]+ mass 126.904')
df_test1.plot(kind = 'scatter', x = 'time (ms)')

#df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
"""
"""
def data_to_excel(dataframe, filename:str, relative_location:str):
    df_test1.to_excel('test1.xlsx')
"""
"""
#test scipy
df = read_data("test1.txt")
column = df['[127I]+ mass 126.904']
print(column)
print(type(column))

peaks, properties = find_peaks(column, height=0.05, prominence=0.1, threshold=0.1, rel_height=0.3, width=3 )
print(peaks)
print(properties)
plt.plot(column)
for x_peak in peaks:
    plt.axvline(x=x_peak, color='red')
for x_left in properties['left_bases']:
    plt.axvline(x=x_left, color='purple')

for x_right in properties['right_bases']:
    plt.axvline(x=x_right, color='blue')
plt.show()
"""
"""
#test skippy iterate over all columns: 
df = read_data("test1.txt")
for columnname in df.columns:
    column = df[columnname]    
    peaks, properties = find_peaks(column, height=0.05, prominence=0.1, threshold=0.1, rel_height=0.3 )
    print(peaks)
    print(properties)
    plt.plot(column)
    for x_peak in peaks:
        plt.axvline(x=x_peak, color='red')
    for x_left in properties['left_bases']:
        plt.axvline(x=x_left, color='purple')

    for x_right in properties['right_bases']:
        plt.axvline(x=x_right, color='blue')
    plt.show()
    
"""

