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

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi


class sourcedata():

    def __init__(self) -> None:
        self.api = KaggleApi()
        self.api.authenticate()

    def getdata(self, source):
        data = self.api.dataset_download_file(source)
