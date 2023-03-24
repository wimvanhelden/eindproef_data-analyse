import pandas as pd


def read_data(filename:str, relative_location:str="./input", skiprows:int=7):
    try: 
        build_file_location=relative_location + "/" + filename
        df = pd.read_table('../input/test1.txt', skiprows=7)
        return(df)
    except Exception as e:
        print(e)
        return None


df_test1 = read_data("test1.txt")

print(df_test1)

def data_to_excel(dataframe, filename:str, relative_location:str):
    df_test1.to_excel('test1.xlsx')