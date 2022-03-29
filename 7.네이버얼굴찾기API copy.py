import os
import sys
import requests
client_id = "WVd65SBOdMplzMN8Gala"
client_secret = "8WTnG3EJIg"
url = "https://openapi.naver.com/v1/vision/celebrity"
files = {'image': open('KakaoTalk_20211027_024806348.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
print(response)

rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)