import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import numpy as np
import pandas as pd

class CCTV:
    def __init__(self):
        # print(f'basedir ====={basedir}') 
        self.reader = FileReader()
    
    def hook_process(self): #처리하는 순서들을 적어놓는다고 생각해... 그러면 나머지 메소드 들이 감춰지는거야
        print('------------ cctv & pop -------------')
        cctv = self.get_cctv()
        pop = self.get_pop()
        cctv = self.rename_cctv(cctv)
        pop = self.rename_pop(pop)
        print(f'CCTV NULL checker: {cctv.isnull()}')
        print(f'CCTV HEAD: {cctv.head()}')
        print(f'POP NULL checker: {pop.isnull()}')
        print(f'POP HEAD: {pop.head()}')


    def get_cctv(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_dframe()
        # print(f'{cctv.head()}')
        return cctv

    def get_pop(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'pop_in_seoul.xls'
        reader.new_file()
        pop=reader.xls_to_dframe(2, 'B,D,G,J,N')
        # print(f'{pop.head()}')
        return pop

    def rename_cctv(self,cctv):
        return cctv.rename(columns = {cctv.columns[0]: '구별'}, inplace = True)

    def rename_pop(self,pop):
        return pop.rename(columns = 
        {pop.columns[0]: '구별',
        pop.columns[1]: '인구수',
        pop.columns[2]: '한국인',
        pop.columns[3]: '외국인',
        pop.columns[4]: '고령자'},
         inplace = True)




if __name__ == "__main__":
    model = CCTV()
    model.hook_process()