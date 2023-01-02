import pandas as pd

from utils import find_xy, trans_wtm2wgs84

# 1인가구 x 5대범죄 발생현황
home = pd.read_csv('./data/org/1인가구(연령별)_20230102224648.csv')
crime = pd.read_csv('./data/org/5대+범죄+발생현황_20230102224619.csv')

home = home.drop([0,1,2,3])[['자치구별(2)','2021.2']]
crime = crime.drop([0,1,2,3])[['자치구별(2)','2021']]

calc = pd.merge(home, crime, on = '자치구별(2)', how='inner')
calc.columns = ['법정구명', '여성1인가구', '범죄발생']
calc = calc.astype({'여성1인가구': int, '범죄발생': int})
calc['calc'] = calc['여성1인가구'] * calc['범죄발생']

calc.to_csv('./data/seoul_women_mul_crime.csv', index=False)

# 노인의료복지 시설 (grand_medical)
police = pd.read_csv('./data/org/경찰청_경찰관서 위치 주소 현황_20220831.csv', encoding='cp949')
police = police[police['경찰서'] == '서울강남']
find_xy(police[police['구분'] == '지구대'], '경찰_주소', '관서명').to_csv("./data/police.csv", index=False)
police_small = find_xy(police[police['구분'] == '파출소'], '경찰_주소', '관서명')
police_small[police_small['lat'] != 'x좌표없음'].to_csv("./data/police_small.csv", index=False)

# 어린이보호구역 (child)
child = pd.read_csv(
    './data/org/서울특별시_어린이_보호구역_지정현황_20201231.csv', encoding='cp949')
child = child[child['자치구명'] == '은평구']
find_xy(child, '도로명 주소(동명)', '시설명').to_csv("./data/child_safe_site.csv", index=False)

# 급경사지 (warnway)
warnway = pd.read_csv(
    './data/org/행정안전부_급경사지 현황_20211231.csv', encoding='cp949')
warnway[warnway['시군구'] == '은평구']#.to_csv("./data/warnway.csv", index=False) #수동