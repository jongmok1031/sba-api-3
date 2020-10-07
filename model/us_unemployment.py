import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader 
import numpy as np
import pandas as pd
import folium

class UsUnemployment:
    def __init__(self):
        self.reader = FileReader()

    def show_map(self):
        reader = self.reader
        reader.context = os.path.join(basedir, 'data')
        reader.fname = 'usa_map.json' 
        reader.new_file() 
        usa_map = reader.json_load()

        reader.fname = 'us_unemployment.csv'
        reader.new_file()
        us_unemployment = reader.csv_to_dframe()
        print(f'{us_unemployment.head()}')

        map = folium.Map(location=[37, -102], zoom_start=5)
        map.choropleth(
            geo_data = usa_map,
            name = 'choropleth',
            data = us_unemployment,
            columns = ['State','Unemployment'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = 'Unemployment Rate (%)'

        )
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(basedir, 'saved_data') 
        reader.fname = 'usa.html' 
        
        map.save(reader.new_file()
        )

        
if __name__ == "__main__":
    us = UsUnemployment()
    us.show_map()