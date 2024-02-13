import pandas as pd
import os

# 결과 CSV 파일이 저장된 폴더
output_folder = "./processed_data"

# 병합할 DataFrame을 저장할 리스트 초기화
dfs = []

# output_folder 내 모든 CSV 파일을 순회하며 DataFrame으로 로드
for filename in os.listdir(output_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(output_folder, filename)
        df = pd.read_csv(file_path)
        dfs.append(df)

# 모든 DataFrame 병합
merged_df = pd.concat(dfs, ignore_index=True)

# 병합된 데이터프레임을 새로운 CSV 파일로 저장
merged_csv_path = os.path.join(output_folder, "merged_avg_tamax_by_region.csv")
merged_df.to_csv(merged_csv_path, index=False)

print(f"Merged CSV saved to: {merged_csv_path}")
