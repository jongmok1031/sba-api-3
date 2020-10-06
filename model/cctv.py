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
        self.show_corrcoef(pop,cctv)
        


    def get_cctv(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'cctv_in_seoul.csv'
        reader.new_file()
        cctv = reader.csv_to_dframe()
        # print(f'{cctv.head()}')
        cctv.rename(columns = {cctv.columns[0]: '구별'}, inplace = True)
        return cctv

    def get_pop(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'pop_in_seoul.xls'
        reader.new_file()
        pop = reader.xls_to_dframe(2, 'B,D,G,J,N')
        pop.rename(columns = {
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
            }, inplace = True)
        pop.drop([26], inplace=True)
        print(f'POP Null Checker: {pop["구별"].isnull()}')
        return pop
    """ 
       r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
       r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
       r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
       r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
       r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
       r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
       r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
       
       고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554]   약한 음적 선형관계
                                   [-0.28078554  1.        ]]

       외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433]    거의 무시될 수 있는
                                   [-0.13607433  1.        ]] 
    """
    
    def show_corrcoef(self, pop, cctv):
        pop['외국인비율'] = pop['외국인'] / pop['인구수'] * 100
        pop['고령자비율'] = pop['고령자'] / pop['인구수'] * 100
        cctv.drop(["2013년도 이전","2014년","2015년","2016년"], 1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on='구별')
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])

        print(f'고령자비율과 CCTV 의 상관계수 {cor1}')
        print(f'외국인비율과 CCTV 의 상관계수 {cor2}')

        reader = self.reader
        reader.context = os.path.join(basedir,'saved_data')
        reader.fname = 'cctv_pop.csv'
        cctv_pop.to_csv(reader.new_file())
 


if __name__ == "__main__":
    model = CCTV()
    model.hook_process()