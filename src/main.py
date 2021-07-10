
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
from configparser import ConfigParser




def main():
    set_path()
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    print(parser.items())
   


def set_path():
    path = "/Users/marcofoley/Google Drive/Personal/Data Science/4. CodingProjects/DataIntensive"
    # Now change the directory
    os.chdir(path)
    retval = os.getcwd()
    print("Current working directory %s" % retval)

    




if __name__ == "__main__":
    main()




