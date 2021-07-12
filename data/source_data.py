###################
#
#   Author: Marco Foley
#   College ID: x19109865
#   emailL: x19109854@student.ncirl.ie
#    
#   Description: Source the data legally and ethically
#
#
#
#
#
#
###################


# libraries required 


import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
#source
class sourcedata():

    def __init__(self):
        print("class")

    def getdata(self,source):
        self.api = KaggleApi()
        self.api.authenticate() 
        print(source)
        self.api.dataset_download_files(source,path='./data', unzip=True)

    


