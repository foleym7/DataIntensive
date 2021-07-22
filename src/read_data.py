
###################
#
#   Author: Marco Foley
#   College ID: x19109865
#   emailL: x19109854@student.ncirl.ie
#    
#   Description: Read Data
#
#
#
#
#
#
###################

#libraries required
from os import path
import pandas as pd
import sys
sys.path.append('.')
import numpy as np
import seaborn as sns 



class readData(): 

    def read_data(self, link):
        ## read the data into a dataframe
        raw_data = pd.read_csv(link, low_memory=False)
        print(raw_data.dtypes)
        return raw_data


    
        
        
        