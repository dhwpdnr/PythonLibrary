from netCDF4 import Dataset
import geopandas as gpd
import pandas as pd

# 파일 경로
ncfile_path = "./data/MKPRISM_MKPRISMv21_skorea_TAMAX_gridraw_daily_2000.nc"
csv_file_path = "./data/region_code.csv"

# CSV 파일 읽기
df_csv = pd.read_csv(csv_file_path)

# .nc 파일 열기
ncfile = Dataset(ncfile_path)

ncfile.close()

# .shp 파일 경로
shp_file_path = "./data/emd.shp"

# 파일 읽기
gdf = gpd.read_file(shp_file_path, encoding="euc-kr")

# 데이터 확인
print(gdf.head())

# '법정동코드' 열을 문자열로 변환
df_csv["법정동코드"] = df_csv["법정동코드"].astype(str)

# 이제 '법정동코드' 열의 뒤 두 자리를 제거할 수 있음
df_csv["법정동코드_수정"] = df_csv["법정동코드"].str[:-2]

# 다시 필터링 시도
filtered_gdf = gdf[gdf["EMD_CD"].isin(df_csv["법정동코드_수정"])]

# 데이터 확인
print(filtered_gdf.head())
