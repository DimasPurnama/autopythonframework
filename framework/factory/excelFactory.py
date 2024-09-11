import pandas as pd
import framework.services.MyConfig

#   initial var class
MyConfig = framework.services.MyConfig

sheet_data_info = pd.read_excel(MyConfig.strFullPathDatatable, sheet_name=MyConfig.strInfoSheet)

data_start = sheet_data_info.at[0,'A']
data_end = sheet_data_info.at[0,'B']
print(data_start)
print(data_end)