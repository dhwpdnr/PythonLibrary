import json

# GeoJSON 파일 로드
file_path = "./data/HangJeongDong_ver20230701.geojson"
with open(file_path, "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

filtered_features = [
    feature
    for feature in geojson_data["features"]
    if feature["properties"]["sido"] == "30"
]

# 필터링된 데이터로 새로운 GeoJSON 객체 생성
filtered_geojson = {"type": "FeatureCollection", "features": filtered_features}

# 결과 확인 (필터링된 항목 수 출력)
len(filtered_features), filtered_geojson.keys()

filtered_geojson_file_path = "./data/Daejeon.geojson"
with open(filtered_geojson_file_path, "w", encoding="utf-8") as f:
    json.dump(filtered_geojson, f, ensure_ascii=False, indent=4)
