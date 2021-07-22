
###################
#
#   Author: Marco Foley
#   College ID: x19109865
#   emailL: x19109854@student.ncirl.ie
#    
#   Description: main file
#
#
#
#
#
#
###################


# import files and libraries
#!/usr/bin/python
import configparser
import os
import sys
sys.path.append('.')
from data.source_data import sourcedata
from src.metadata_cleaning import clean_data
from src.read_data import readData
from configparser import ConfigParser
import logging




def main():
    #1. Start the logging file   
    logging.basicConfig(filename='system.log', format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s', level=logging.DEBUG, force= True)
    logger = logging.getLogger(__name__)
    logger.info("System Started........")

    #2. Source data from Kaggle 
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    source = parser['kaggle']['url']

    data_source_1 = 'data/movies_metadata.csv'
    data_source_2 = 'data/ratings'
    readdata = readData
    readdata.read_data()

    #3. Create mapreduce




if __name__ == "__main__":
    main()




