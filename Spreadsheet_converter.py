from pandas import read_excel
class sheet_converter :
    def __init__(self) :
        """okay"""
        pass
    def converter(source) :
        for file_name in source :
            df = read_excel(file_name, sheet_name=None)
            df[list(df.keys())[0]].to_csv(file_name +".csv" ,index = False)
           