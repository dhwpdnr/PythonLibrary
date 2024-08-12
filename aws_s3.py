import requests


# Presigned URL
presigned_url = "aws s3 upload url"
# Local file to upload
file_path = "test_image.png"

# Open the file in binary mode
# with open(file_path, 'rb') as file:
#     print(file)
#     # Upload the file using the presigned URL
#     response = requests.put(presigned_url, data=file)

with open(file_path, "rb") as image_file:
    files = {"file": (file_path, image_file)}
    response = requests.put(presigned_url, data=image_file)
    if response.status_code == 200:
        print("Image uploaded successfully")
    else:
        print("Failed to upload image")
        print(response.text)


# Check the response
if response.status_code == 200:
    print("Upload successful!")
else:
    print(
        f"Upload failed. Status code: {response.status_code}, Response: {response.text}"
    )
