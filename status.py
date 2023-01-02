import json
import pandas as pd
import folium
from folium.plugins import MarkerCluster

j_map = json.load(
    open('./data/org/skorea_municipalities_geo_simple.json', encoding='utf-8'))

people = pd.read_csv('./data/seoul_women_mul_crime.csv', encoding='utf-8')

# 서울 위경도
lat_c, lon_c = 37.53165351203043, 126.9974246490573

m = folium.Map(location=[lat_c, lon_c], zoom_start=11)

m.choropleth(geo_data=j_map,
             data=people,
             columns=['법정구명', 'calc'],
             fill_color='PuRd',
             key_on='feature.id')

postbox = pd.read_csv('./data/org/서울시 안심택배함 설치 장소.csv', encoding='cp949')

marker_cluster = MarkerCluster().add_to(m)

for idx, row in postbox.iterrows():

    lat_ = row['WGS Y 좌표']
    lon_ = row['WGS X 좌표']

    folium.Marker(location=[lat_, lon_],
                  radius=10
                  ).add_to(marker_cluster)

m #m.save('./map/status_visualization.html)