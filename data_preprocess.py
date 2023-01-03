import pandas as pd

from utils import find_xy, trans_wtm2wgs84

# 1인가구 x 5대범죄 발생현황
home = pd.read_csv('./data/org/1인가구(연령별)_20230102224648.csv')
crime = pd.read_csv('./data/org/5대+범죄+발생현황_20230102224619.csv')

home = home.drop([0, 1, 2, 3])[['자치구별(2)', '2021.2']]
crime = crime.drop([0, 1, 2, 3])[['자치구별(2)', '2021']]

calc = pd.merge(home, crime, on='자치구별(2)', how='inner')
calc.columns = ['법정구명', '여성1인가구', '범죄발생']
calc = calc.astype({'여성1인가구': int, '범죄발생': int})
calc['calc'] = calc['여성1인가구'] * calc['범죄발생']

calc.to_csv('./data/seoul_women_mul_crime.csv', index=False)

# 경찰서 (police / police_small)
police = pd.read_csv(
    './data/org/경찰청_경찰관서 위치 주소 현황_20220831.csv', encoding='cp949')
police = police[police['경찰서'] == '서울강남']
find_xy(police[police['구분'] == '지구대'], '경찰_주소', '관서명').to_csv(
    "./data/police.csv", index=False)
police_small = find_xy(police[police['구분'] == '파출소'], '경찰_주소', '관서명')
police_small[police_small['lat'] != 'x좌표없음'].to_csv(
    "./data/police_small.csv", index=False)

# 대규모점포
department = pd.read_csv(
    './data/org/fulldata_08_25_01_P_대규모점포.csv', encoding='cp949')
department = department.dropna(axis='index', how='any', subset=['도로명전체주소'])
department = department[department['도로명전체주소'].str.contains('강남구')]
department = find_xy(department, '도로명전체주소', '사업장명')
department[department['lat'] != 'x좌표없음'].to_csv(
    "./data/department.csv", index=False)

# 지하철역

metro = pd.read_csv('./data/org/5_지하철노선위경도정보(서울 지하철 노선도 기준).csv')
g_metro = pd.read_csv(
    './data/org/서울교통공사_자치구별지하철역정보_20221130.csv', encoding='cp949')

gangnam_li = g_metro['역명(호선)'][0].split(', ')
gangnam_li = '|'.join([i.split('(')[0] for i in gangnam_li])
metro[metro.역이름.str.contains(gangnam_li)]
