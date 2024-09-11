import os
import framework.services.MyConfig

# initial var class
MyConfig = framework.services.MyConfig

def create_folder_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
