import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search" # subscription use
headers = {"Ocp-Apim-Subscription-Key": API_KEY}
MAX_RESULTS = 100
members = [  
    "MEMBER_NAME"
]
columns = ["member", "title", "url"]
df = pd.DataFrame(columns=columns)

for member in members:
  print("{}を取得しています".format(member))
  params = {"q": member, "count": MAX_RESULTS,
            "imageType": "Photo", "color": "ColorOnly"}
  search_json = requests.get(URL, headers=headers, params=params).json()

for json in search_json["value"]:
  name = json["name"]
  url = json["contentUrl"]
  se = pd.Series([member, name, url], columns)
  df = df.append(se, ignore_index=True)

from google.colab import files
filename = "akb.csv"
df.to_csv("akb.csv")
files.download(filename)
