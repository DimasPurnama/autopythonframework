def read_properties_file(filePath):
    properties = {}

    with open(filePath) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=',1)
                properties[key.strip()] = value.strip()

    return properties

# filePath = 'resources/configuration/excelConfig.properties'
# properties = read_properties_file(filePath)
# print(properties.get('strMainSheet'))