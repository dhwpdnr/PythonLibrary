from pymongo.mongo_client import MongoClient
import json

# secret.json 파일을 읽어서 mongoUrl 가져오기
with open("../secret.json") as f:
    secret = json.loads(f.read())
    mongoUrl = secret["mongoUrl"]

uri = mongoUrl

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print("Connected to MongoDB Atlas!")

# use a database named "Recipe"
my_db = client.Recipe
video_collection = my_db["video"]
url = "https://www.youtube.com/watch?v=Q3JZ4Z3jXJ8"
# url 에서 youtube key 추출
url_split = url.split("v=")
youtube_key = url_split[1]  # url 에서 가져온 youtube key

# collection 에서 조회
my_doc = video_collection.find_one({"key": youtube_key})

# collection 에 있으면 리턴
if my_doc is not None:
    print(my_doc["detail"])

# collection 에 없으면 insert
else:
    # recipe documents 생성
    # gpt 로직 추가
    recipe_documents = {
        "key": youtube_key,
        "detail": {
            "ingredients": [
                "corn",
                "mayonnaise",
                "cotija cheese",
                "sour cream",
                "lime",
            ],
            "steps": ["step1", "step2", "step3"],
        },  # gpt response
    }
    # insert
    try:
        result = video_collection.insert_one(recipe_documents)
    except Exception as e:
        print(e)
