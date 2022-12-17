import requests
from bs4 import BeautifulSoup
url ='https://www.filgoal.com/championships/1111/%D9%82%D8%B7%D8%B1-2022'
response = requests.get(url)
content = response.text
soup =BeautifulSoup(content,"html.parser")

matches =soup.find_all("div",{"class":"c-i-next"})
for match in matches:
   print(match.find("div",{"class":"f"}).get_text())
   print(match.find("div", {"class": "m"}).get_text())
   print(match.find("div", {"class": "s"}).get_text())