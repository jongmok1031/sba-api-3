import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import numpy as np
import pandas as pd

class Crime:
    def __init__(self):
        # print(f'basedir ====={basedir}') 
        self.reader = FileReader()

    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        print(f'{crime.head()}')
        return crime

if __name__ == "__main__":
    cr = Crime()
    cr.get_crime()