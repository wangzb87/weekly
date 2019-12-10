import os
from os import listdir

def list_weekly(weekly_path,sorted):
    weekly_name = []
    for filenames in listdir(weekly_path) :
        if  filenames.startswith('.'): continue
        if os.path.isfile(os.path.join(weekly_path, filenames)):
            weekly_name.append(os.path.join(weekly_path,filenames))
    
    weekly_name.sort(reverse=sorted)
    return weekly_name