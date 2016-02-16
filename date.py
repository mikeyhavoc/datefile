#!python3
# date.py
# Author Michael Williams
# Date: 2/11/16
# program: updates the date on program files.
# version 1. gets date file.
# version 2. name files if want too.
# version 3. get creation date for file.
# update: 2/16/16
# Version: 2.0

import datetime, os

#Get year, month, day, minutes
year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day
minute = datetime.datetime.today().minute

def file_type():
    '''Lets the user select the file type for which they will be replacing the date on'''
    kind = input('search for what kind of file: ')
    ext = '.'
    ext += kind
    return ext


#Gets files in folder, replaces files with yyyy-mm-dd-filename.ext
def file_change(folder):
    for filenames in os.listdir(folder):
        date_name = str(year) + '-' + str(month) + '-' + str(day) + "_" + filenames

        if filenames.startswith('date') and filenames.endswith('.py'):
            continue    # skip date.py file
        if filenames.startswith('.git') and filenames.endswith('.git'):
            continue    # skips git repository
        if filenames.startswith(str(year)):
            continue    # skips previously dated files.
        if filenames.endswith('.txt'):
            os.rename(filenames, date_name)



file_change('C:\\Users\\mjwil\\Documents\\portfolio\\python\\date')
#TODO version3.direct folder change files with ext to yyyy-mm-dd-min-filename.ext.
