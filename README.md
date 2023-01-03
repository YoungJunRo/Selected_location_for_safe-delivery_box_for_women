# Selected_location_for_safe_delivery_box_for_women

## Data update with refactoring date : 2023-01-01 ~ 2023-01-03

## How To use

- Run data_preprocess.py (Check warnway.csv > fixed manually)
- Run status.py (For check now status)
- Run mclp.ipynb (Need Jupyter notebook)

## Model

### MCLP

Gurobi Solver를 활용하여 Simple MIP(Mixed Integer Linear Programming)를 통해 Maximum Coverage Location Problem 해결


## Requirements

- `geopandas==0.9.0`
- `branca==0.5.0`
- `folium==0.13.0`
- `gurobipy==9.1.2`
- `mip==1.13.0`
- `numpy==1.19.5`
- `pandas==1.1.5`
- `scipy==1.5.4`
- `shapley==1.0.3`
- `selenium==3.141.0`
- `tqdm==4.64.1`

## Data

### Data list

- [경찰청_경찰관서 위치 주소 현황_20220831.csv](https://www.data.go.kr/data/15054711/fileData.do?recommendDataYn=Y)
- [서울시 안심택배함 설치 장소.csv](http://data.seoul.go.kr/dataList/OA-20922/S/1/datasetView.do;jsessionid=57F0975A52DB16E1382B130AA281E7AF.new_portal-svr-11)
- [1인가구(연령별)_20230102224648.csv](https://data.seoul.go.kr/dataList/10995/S/2/datasetView.do)
- [5대+범죄+발생현황_20230102224619.csv](https://data.seoul.go.kr/dataList/316/S/2/datasetView.do)
- [5_지하철노선위경도정보(서울 지하철 노선도 기준).csv](https://www.data.go.kr/data/15099316/fileData.do?recommendDataYn=Y)
- [fulldata_08_25_01_P_대규모점포.csv](https://www.data.go.kr/data/15045013/fileData.do)
- [서울교통공사_자치구별지하철역정보_20221130.csv](https://www.data.go.kr/data/15045013/fileData.do)
