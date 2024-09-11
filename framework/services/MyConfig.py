import framework.services.PropertiesService

# initial var class
PropertiesService = framework.services.PropertiesService

properties = PropertiesService.read_properties_file('resources/configuration/excelConfig.properties')

strFullPathDatatable = properties.get('strPathDatatable')
strPathDatatable = ''
if '.xlsx' or '.xlsm' in strFullPathDatatable :
    folder = strFullPathDatatable.split("/")
    count = 0
    for x in folder:
        count += 1
        if count < len(folder):
            strPathDatatable += x + "/"
else:
    strPathDatatable = strFullPathDatatable

# get variable from properties
strPathReport = properties.get('strPathReport')
strMainSheet = properties.get('strMainSheet')
strInfoSheet = properties.get('strInfoSheet')
strColumnActionSheet = properties.get('strColumnActionSheet')

# print(strFullPathDatatable)
# print(strPathDatatable)